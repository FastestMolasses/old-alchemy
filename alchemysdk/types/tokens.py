from typing import Literal
from typing import TypedDict


Token = Literal['ERC721', 'ERC1155']


class TokenObject(TypedDict):
    contractAddress: str
    tokenId: str | int
    tokenType: Token | None
