from typing import Any, Literal, Union

import requests

from pyalchemy.endpoints import nft, transfers
from pyalchemy.types import nfts as nft_types
from pyalchemy.types import tokens as token_types
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

    def getContractsForOwner(self,
                             owner: str,
                             pageKey: str | None = None,
                             pageSize: int = 100,
                             excludeFilters: list[nft_types.NFTFilters] | None = None,
                             includeFilters: list[nft_types.NFTFilters] | None = None,
                             orderBy: Literal['transferTime', 'null'] | None = None
                             ) -> dict[Any, Any]:
        params = {
            'owner': owner,
            'pageKey': pageKey,
            'pageSize': pageSize,
            'excludeFilters': excludeFilters,
            'includeFilters': includeFilters,
            'orderBy': orderBy,
        }
        return self._makeRequest(url=nft.getContractsForOwner(self.apiKey), params=params)

    def getOwnersForToken(self, contractAddress: str, tokenId: str | int) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'tokenId': tokenId,
        }
        return self._makeRequest(url=nft.getOwnersForToken(self.apiKey), params=params)

    def getOwnersForCollection(self,
                               contractAddress: str,
                               withTokenBalances: bool = False,
                               block: str | None = None,
                               pageKey: str | None = None) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'withTokenBalances': withTokenBalances,
            'block': block,
            'pageKey': pageKey,
        }
        return self._makeRequest(url=nft.getOwnersForCollection(self.apiKey), params=params)

    def isHolderOfCollection(self, wallet: str, contractAddress: str) -> dict[Any, Any]:
        params = {
            'wallet': wallet,
            'contractAddress': contractAddress,
        }
        return self._makeRequest(url=nft.isHolderOfCollection(self.apiKey), params=params)

    def getNFTMetadata(self,
                       contractAddress: str,
                       tokenId: str | int,
                       tokenType: token_types.Token | None = None,
                       tokenUriTimeoutInMs: int | None = None,
                       refreshCache: bool = False) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'tokenId': tokenId,
            'tokenType': tokenType,
            'tokenUriTimeoutInMs': tokenUriTimeoutInMs,
            'refreshCache': refreshCache,
        }
        return self._makeRequest(url=nft.getNFTMetadata(self.apiKey), params=params)

    def getNFTMetadataBatch(self,
                            tokens: list[token_types.TokenObject],
                            tokenUriTimeoutInMs: int | None = None,
                            refreshCache: bool = False) -> dict[Any, Any]:
        payload = {
            'tokens': tokens,
            'tokenUriTimeoutInMs': tokenUriTimeoutInMs,
            'refreshCache': refreshCache,
        }
        return self._makeRequest(url=nft.getNFTMetadataBatch(self.apiKey),
                                 data=payload,
                                 method='POST')

    def getContractMetadataBatch(self, contractAddresses: list[str]) -> dict[Any, Any]:
        payload = {
            'contractAddresses': contractAddresses,
        }
        return self._makeRequest(url=nft.getContractMetadataBatch(self.apiKey),
                                 data=payload,
                                 method='POST')

    def searchContractMetadata(self, query: str) -> dict[Any, Any]:
        params = {
            'query': query,
        }
        return self._makeRequest(url=nft.searchContractMetadata(self.apiKey), params=params)

    def reingestContract(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return self._makeRequest(url=nft.reingestContract(self.apiKey), params=params)

    def getNFTsForCollection(self,
                             contractAddress: str,
                             withMetadata: bool = False,
                             startToken: str | int | None = None,
                             limit: int = 100,
                             tokenUriTimeoutInMs: int | None = None) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'withMetadata': withMetadata,
            'startToken': startToken,
            'limit': limit,
            'tokenUriTimeoutInMs': tokenUriTimeoutInMs,
        }
        return self._makeRequest(url=nft.getNFTsForCollection(self.apiKey), params=params)

    def isSpamContract(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return self._makeRequest(url=nft.isSpamContract(self.apiKey), params=params)

    def getFloorPrice(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return self._makeRequest(url=nft.getFloorPrice(self.apiKey), params=params)

    def getNFTSales(self,
                    fromBlock: str | int | Literal['latest'] = 0,
                    toBlock: str | int | Literal['latest'] = 'latest',
                    order: Literal['asc', 'desc'] = 'desc',
                    marketplace: nft_types.Marketplace | None = None,
                    contractAddress: str | None = None,
                    tokenId: str | int | None = None,
                    buyerAddress: str | None = None,
                    sellerAddress: str | None = None,
                    taker: Literal['buyer', 'seller'] | None = None,
                    limit: int = 1000,
                    pageKey: str | None = None) -> dict[Any, Any]:
        params = {
            'fromBlock': fromBlock,
            'toBlock': toBlock,
            'order': order,
            'marketplace': marketplace,
            'contractAddress': contractAddress,
            'tokenId': tokenId,
            'buyerAddress': buyerAddress,
            'sellerAddress': sellerAddress,
            'taker': taker,
            'limit': limit,
            'pageKey': pageKey,
        }
        return self._makeRequest(url=nft.getNFTSales(self.apiKey), params=params)

    def computeRarity(self, contractAddress: str, tokenId: str | int) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'tokenId': tokenId,
        }
        return self._makeRequest(url=nft.computeRarity(self.apiKey), params=params)

    def summarizeNFTAttributes(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return self._makeRequest(url=nft.summarizeNFTAttributes(self.apiKey), params=params)

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

        if response.status_code == 400:
            raise ValueError(response.text)

        elif response.status_code == 401:
            raise ValueError('Invalid API key')

        elif response.status_code == 403:
            raise ConnectionError('Access denied')

        elif response.status_code == 404:
            raise ValueError('Not found')

        elif response.status_code == 429:
            raise ConnectionError('Rate limit exceeded')

        elif response.status_code == 500:
            raise ConnectionError('Internal server error')

        return response.json()
