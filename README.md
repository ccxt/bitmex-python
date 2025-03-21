# bitmex-python
Python SDK (sync and async) for Bitmex with Rest and WS capabilities.

You can check Bitmex's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitmex)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install bitmex-api
```

## Usage

### Async

```Python
from bitmex_api import BitmexAsync

async def main():
    instance = BitmexAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from bitmex_api import BitmexSync

def main():
    instance = BitmexSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from bitmex_api import BitmexWs

async def main():
    instance = BitmexWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

