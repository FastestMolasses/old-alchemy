import requests

from typing import Union, Any, Literal
from pyalchemy.endpoints import transfers, nft

from pyalchemy.types import nfts as nft_types
from pyalchemy.types import transfers as transfer_types


class AlchemyAPI:
    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self.headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }

    # ========================================= NFTs ========================================
    def getNFTs(self,
                owner: str,
                pageKey: str | None = None,
                pageSize: int = 100,
                contractAddresses: list[str] | None = None,
                withMetadata: bool = False,
                tokenUriTimeoutInMs: int | None = None,
                excludeFilters: list[nft_types.NFTFilters] | None = None,
                includeFilters: list[nft_types.NFTFilters] | None = None,
                orderBy: Literal['transferTime', 'null'] | None = None) -> dict[Any, Any]:
        params = {
            'owner': owner,
            'pageKey': pageKey,
            'pageSize': pageSize,
            'contractAddresses': contractAddresses,
            'withMetadata': withMetadata,
            'tokenUriTimeoutInMs': tokenUriTimeoutInMs,
            'excludeFilters': excludeFilters,
            'includeFilters': includeFilters,
            'orderBy': orderBy,
        }
        return self._makeRequest(url=nft.getNFTs(self.apiKey), params=params)

    # ====================================== Transfers ======================================
    def getAssetTransfers(self,
                          id: int,
                          category: list[transfer_types.TransferTypes],
                          jsonrpc: str = '2.0',
                          method: str = 'alchemy_getAssetTransfers',
                          fromBlock: str | int | Literal['latest'] = '0x0',
                          toBlock: str | int | Literal['latest'] = 'latest',
                          fromAddress: str | None = None,
                          toAddress: str | None = None,
                          contractAddresses: list[str] | None = None,
                          order: Literal['asc', 'desc'] = 'asc',
                          withMetadata: bool = False,
                          excludeZeroValue: bool = True,
                          maxCount: str = '0x3e8',
                          pageKey: str | None = None) -> dict[Any, Any]:
        payload = {
            'id': id,
            'jsonrpc': jsonrpc,
            'method': method,
            'params': {
                'fromBlock': fromBlock,
                'toBlock': toBlock,
                'category': category,
                'fromAddress': fromAddress,
                'toAddress': toAddress,
                'contractAddresses': contractAddresses,
                'order': order,
                'withMetadata': withMetadata,
                'excludeZeroValue': excludeZeroValue,
                'maxCount': maxCount,
                'pageKey': pageKey,
            },
        }
        # Remove None values inside params
        payload['params'] = {k: v for k, v in payload['params'].items() if v is not None}

        return self._makeRequest(
            url=transfers.getAssetTransfers(self.apiKey),
            data=payload,
            method='POST')

    def _makeRequest(self,
                     url: str,
                     params: Union[dict[Any, Any], None] = None,
                     method: Literal['GET', 'POST'] = 'GET',
                     data: Union[dict[Any, Any], None] = None) -> dict[Any, Any]:
        response = requests.request(
            url=url,
            json=data,
            method=method,
            params=params,
            headers=self.headers,
        )

        print(response.url)

        if response.status_code == 400:
            raise ValueError(response.text)

        elif response.status_code == 401:
            raise ValueError('Invalid API key')

        elif response.status_code == 403:
            raise ConnectionError('Access denied')

        elif response.status_code == 429:
            raise ConnectionError('Rate limit exceeded')

        elif response.status_code == 500:
            raise ConnectionError('Internal server error')

        return response.json()
