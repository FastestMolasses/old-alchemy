def getAssetTransfers(apiKey: str) -> str:
    """
        The Transfers API allows you to easily fetch historical transactions for
        any address across Ethereum and supported L2s including Polygon, Arbitrum,
        and Optimism.
    """
    return f'https://eth-mainnet.g.alchemy.com/v2/{apiKey}'
