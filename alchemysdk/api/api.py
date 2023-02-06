from typing import Any, Literal, Union, Callable

import json
import aiohttp

from alchemysdk.endpoints import nft, transfers
from alchemysdk.types import nfts as nft_types
from alchemysdk.types import tokens as token_types
from alchemysdk.types import transfers as transfer_types


class AlchemyAPI:
    def __init__(self,
                 apiKey: str,
                 session: aiohttp.ClientSession | None = None,
                 jsonDecoder: Callable[[str], Any] = json.loads):
        self.apiKey = apiKey
        self.headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }
        self.session = session
        self.jsonDecoder = jsonDecoder

    # ========================================= NFTs ========================================
    async def getNFTs(self,
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
        return await self._makeRequest(url=nft.getNFTs(self.apiKey), params=params)

    async def getContractsForOwner(self,
                                   owner: str,
                                   pageKey: str | None = None,
                                   pageSize: int = 100,
                                   excludeFilters: list[nft_types.NFTFilters] | None = None,
                                   includeFilters: list[nft_types.NFTFilters] | None = None,
                                   orderBy: Literal['transferTime',
                                                    'null'] | None = None
                                   ) -> dict[Any, Any]:
        params = {
            'owner': owner,
            'pageKey': pageKey,
            'pageSize': pageSize,
            'excludeFilters': excludeFilters,
            'includeFilters': includeFilters,
            'orderBy': orderBy,
        }
        return await self._makeRequest(url=nft.getContractsForOwner(self.apiKey), params=params)

    async def getOwnersForToken(self, contractAddress: str, tokenId: str | int) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'tokenId': tokenId,
        }
        return await self._makeRequest(url=nft.getOwnersForToken(self.apiKey), params=params)

    async def getOwnersForCollection(self,
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
        return await self._makeRequest(url=nft.getOwnersForCollection(self.apiKey), params=params)

    async def isHolderOfCollection(self, wallet: str, contractAddress: str) -> dict[Any, Any]:
        params = {
            'wallet': wallet,
            'contractAddress': contractAddress,
        }
        return await self._makeRequest(url=nft.isHolderOfCollection(self.apiKey), params=params)

    async def getNFTMetadata(self,
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
        return await self._makeRequest(url=nft.getNFTMetadata(self.apiKey), params=params)

    async def getNFTMetadataBatch(self,
                                  tokens: list[token_types.TokenObject],
                                  tokenUriTimeoutInMs: int | None = None,
                                  refreshCache: bool = False) -> dict[Any, Any]:
        payload = {
            'tokens': tokens,
            'tokenUriTimeoutInMs': tokenUriTimeoutInMs,
            'refreshCache': refreshCache,
        }
        return await self._makeRequest(url=nft.getNFTMetadataBatch(self.apiKey),
                                       data=payload,
                                       method='POST')

    async def getContractMetadataBatch(self, contractAddresses: list[str]) -> dict[Any, Any]:
        payload = {
            'contractAddresses': contractAddresses,
        }
        return await self._makeRequest(url=nft.getContractMetadataBatch(self.apiKey),
                                       data=payload,
                                       method='POST')

    async def searchContractMetadata(self, query: str) -> dict[Any, Any]:
        params = {
            'query': query,
        }
        return await self._makeRequest(url=nft.searchContractMetadata(self.apiKey), params=params)

    async def reingestContract(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return await self._makeRequest(url=nft.reingestContract(self.apiKey), params=params)

    async def getNFTsForCollection(self,
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
        return await self._makeRequest(url=nft.getNFTsForCollection(self.apiKey), params=params)

    async def isSpamContract(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return await self._makeRequest(url=nft.isSpamContract(self.apiKey), params=params)

    async def getFloorPrice(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return await self._makeRequest(url=nft.getFloorPrice(self.apiKey), params=params)

    async def getNFTSales(self,
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
        return await self._makeRequest(url=nft.getNFTSales(self.apiKey), params=params)

    async def computeRarity(self, contractAddress: str, tokenId: str | int) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
            'tokenId': tokenId,
        }
        return await self._makeRequest(url=nft.computeRarity(self.apiKey), params=params)

    async def summarizeNFTAttributes(self, contractAddress: str) -> dict[Any, Any]:
        params = {
            'contractAddress': contractAddress,
        }
        return await self._makeRequest(url=nft.summarizeNFTAttributes(self.apiKey), params=params)

    # ====================================== Transfers ======================================
    async def getAssetTransfers(self,
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
        payload['params'] = {k: v for k,
                             v in payload['params'].items() if v is not None}

        return await self._makeRequest(
            url=transfers.getAssetTransfers(self.apiKey),
            data=payload,
            method='POST')

    async def _makeRequest(self,
                           url: str,
                           params: Union[dict[Any, Any], None] = None,
                           method: Literal['GET', 'POST'] = 'GET',
                           data: Union[dict[Any, Any], None] = None) -> dict[Any, Any]:
        if self.session:
            response = await self.session.request(
                url=url,
                json=data,
                method=method,
                params=params,
                headers=self.headers,
            )

        else:
            async with aiohttp.ClientSession() as session:
                response = await session.request(
                    url=url,
                    json=data,
                    method=method,
                    params=params,
                    headers=self.headers,
                )

        if response.status == 400:
            raise ValueError(response.text)

        elif response.status == 401:
            raise ValueError('Invalid API key')

        elif response.status == 403:
            raise ConnectionError('Access denied')

        elif response.status == 404:
            raise ValueError('Not found')

        elif response.status == 429:
            raise ConnectionError('Rate limit exceeded')

        elif response.status == 500:
            raise ConnectionError('Internal server error')

        return await response.json(encoding='utf-8', loads=self.jsonDecoder)
