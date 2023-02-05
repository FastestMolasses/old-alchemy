def getNFTs(apiKey: str) -> str:
    """
        Gets all NFTs currently owned by a given address.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getNFTs'


def getContractsForOwner(apiKey: str) -> str:
    """
        Gets all NFT contracts held by an owner address.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getContractsForOwner'


def getOwnersForToken(apiKey: str) -> str:
    """
        Get the owner(s) for a token.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getOwnersForToken'


def getOwnersForCollection(apiKey: str) -> str:
    """
        Gets all owners for a given NFT contract.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getOwnersForCollection'


def isHolderOfCollection(apiKey: str) -> str:
    """
        Checks whether a wallet holds a NFT in a given collection.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/isHolderOfCollection'


def getNFTMetadata(apiKey: str) -> str:
    """
        Gets the metadata associated with a given NFT.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getNFTMetadata'


def getNFTMetadataBatch(apiKey: str) -> str:
    """
        Gets the metadata associated with the given NFTs.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getNFTMetadataBatch'


def getContractMetadata(apiKey: str) -> str:
    """
        Queries NFT high-level collection/contract level information.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getContractMetadata'


def getContractMetadataBatch(apiKey: str) -> str:
    """
        Gets the metadata associated with the given list of contract addresses.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getContractMetadataBatch'


def searchContractMetadata(apiKey: str) -> str:
    """
        Search for a keyword across metadata of all ERC-721 and ERC-1155 smart contracts.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/searchContractMetadata'


def reingestContract(apiKey: str) -> str:
    """
        Triggers metadata refresh for an entire NFT collection and refreshes stale
        metadata after a collection reveal/collection changes.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/reingestContract'


def getNFTsForCollection(apiKey: str) -> str:
    """
        Gets all NFTs for a given NFT contract.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getNFTsForCollection'


def getSpamContracts(apiKey: str) -> str:
    """
        Returns a list of all spam contracts marked by Alchemy.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getSpamContracts'


def isSpamContract(apiKey: str) -> str:
    """
        Returns whether a contract is marked as spam or not by Alchemy.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/isSpamContract'


def getFloorPrice(apiKey: str) -> str:
    """
        Returns the floor prices of a NFT collection by marketplace.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getFloorPrice'


def getNFTSales(apiKey: str) -> str:
    """
        Gets NFT sales that have happened through on-chain marketplaces.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/getNFTSales'


def computeRarity(apiKey: str) -> str:
    """
        Computes the rarity of each attribute of an NFT.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/computeRarity'


def summarizeNFTAttributes(apiKey: str) -> str:
    """
        Generate a summary of attribute prevalence for an NFT collection.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}/summarizeNFTAttributes'
