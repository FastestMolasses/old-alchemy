# Python SDK for the Alchemy API

![python](https://github.com/FastestMolasses/alchemy-sdk/actions/workflows/main.yaml/badge.svg) [![PyPI version](https://badge.fury.io/py/alchemysdk.svg)](https://badge.fury.io/py/alchemysdk)

An unofficial Python SDK for the [Alchemy API](https://docs.alchemy.com/).


## Features

- Async requests
- Full static typing
- orjson / ujson support


## Installation

Requirements: Python 3.9+

Pip:
```bash
pip install alchemy-sdk
```

Poetry:
```bash
poetry add alchemy-sdk
```

### Upgrade

Pip:
```bash
pip install alchemy-sdk -U
```

Poetry:
```bash
poetry update alchemy-sdk
```

## Usage

```python
from alchemysdk import AlchemyAPI


async def main():
    api = AlchemyAPI('API_KEY')
    # Function names correspond to the API endpoint names
    # https://docs.alchemy.com/reference/api-overview
    # Currently all NFT endpoints are supported
    response = await api.getOwnersForToken('0xe785E82358879F061BC3dcAC6f0444462D4b5330', tokenId=5)
    print(response)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```

A new `aiohttp.ClientSession` is created on each request. If you want to use a single session, you can pass it in as an argument:

```python
import aiohttp

from alchemysdk import AlchemyAPI


async def main():
    async with aiohttp.ClientSession() as session:
        api = AlchemyAPI('API_KEY', session)
        ...
```

You can also pass in a custom `json` module to use for serialization/de-serialization:

```python
import orjson
import aiohttp

from alchemysdk import AlchemyAPI


async def main():
    # Use the orjson serializer
    async with aiohttp.ClientSession(json_serialize=orjson.dumps) as session:
        # Pass in the orjson deserializer
        api = AlchemyAPI('API_KEY', session, orjson.loads)
        ...
```


## Contributing

1. Fork it (<https://github.com/FastestMolasses/alchemy-sdk/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
