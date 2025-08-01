# bitmex-python
Python SDK (sync and async) for Bitmex cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bitmex)
- You can check Bitmex's docs here: [Docs](https://www.google.com/search?q=google+bitmex+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/bitmex-python
- Pypi package: https://pypi.org/project/bitmex-api


## Installation

```
pip install bitmex-api
```

## Usage

### Sync

```Python
from bitmex import BitmexSync

def main():
    instance = BitmexSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from bitmex import BitmexAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitmexAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from bitmex import BitmexWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BitmexWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `fetch_balance(self, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverages(self, symbols: Strings = None, params={})`
- `fetch_liquidations(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `amount_to_precision(self, symbol, amount)`
- `calculate_rate_limiter_cost(self, api, method, path, params, config={})`
- `cancel_all_orders_after(self, timeout: Int, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `convert_from_raw_cost(self, symbol, rawQuantity)`
- `convert_from_raw_quantity(self, symbol, rawQuantity, currencySide='base')`
- `convert_from_real_amount(self, code, amount)`
- `convert_to_real_amount(self, code: Str, amount: Str)`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `nonce(self)`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `public_get_announcement(request)`
- `public_get_announcement_urgent(request)`
- `public_get_chat(request)`
- `public_get_chat_channels(request)`
- `public_get_chat_connected(request)`
- `public_get_chat_pinned(request)`
- `public_get_funding(request)`
- `public_get_guild(request)`
- `public_get_instrument(request)`
- `public_get_instrument_active(request)`
- `public_get_instrument_activeandindices(request)`
- `public_get_instrument_activeintervals(request)`
- `public_get_instrument_compositeindex(request)`
- `public_get_instrument_indices(request)`
- `public_get_instrument_usdvolume(request)`
- `public_get_insurance(request)`
- `public_get_leaderboard(request)`
- `public_get_liquidation(request)`
- `public_get_orderbook_l2(request)`
- `public_get_porl_nonce(request)`
- `public_get_quote(request)`
- `public_get_quote_bucketed(request)`
- `public_get_schema(request)`
- `public_get_schema_websockethelp(request)`
- `public_get_settlement(request)`
- `public_get_stats(request)`
- `public_get_stats_history(request)`
- `public_get_stats_historyusd(request)`
- `public_get_trade(request)`
- `public_get_trade_bucketed(request)`
- `public_get_wallet_assets(request)`
- `public_get_wallet_networks(request)`
- `private_get_address(request)`
- `private_get_apikey(request)`
- `private_get_execution(request)`
- `private_get_execution_tradehistory(request)`
- `private_get_globalnotification(request)`
- `private_get_leaderboard_name(request)`
- `private_get_order(request)`
- `private_get_porl_snapshots(request)`
- `private_get_position(request)`
- `private_get_user(request)`
- `private_get_user_affiliatestatus(request)`
- `private_get_user_checkreferralcode(request)`
- `private_get_user_commission(request)`
- `private_get_user_csa(request)`
- `private_get_user_depositaddress(request)`
- `private_get_user_executionhistory(request)`
- `private_get_user_getwallettransferaccounts(request)`
- `private_get_user_margin(request)`
- `private_get_user_quotefillratio(request)`
- `private_get_user_quotevalueratio(request)`
- `private_get_user_staking(request)`
- `private_get_user_staking_instruments(request)`
- `private_get_user_staking_tiers(request)`
- `private_get_user_tradingvolume(request)`
- `private_get_user_unstakingrequests(request)`
- `private_get_user_wallet(request)`
- `private_get_user_wallethistory(request)`
- `private_get_user_walletsummary(request)`
- `private_get_useraffiliates(request)`
- `private_get_userevent(request)`
- `private_post_address(request)`
- `private_post_chat(request)`
- `private_post_guild(request)`
- `private_post_guild_archive(request)`
- `private_post_guild_join(request)`
- `private_post_guild_kick(request)`
- `private_post_guild_leave(request)`
- `private_post_guild_sharestrades(request)`
- `private_post_order(request)`
- `private_post_order_cancelallafter(request)`
- `private_post_order_closeposition(request)`
- `private_post_position_isolate(request)`
- `private_post_position_leverage(request)`
- `private_post_position_risklimit(request)`
- `private_post_position_transfermargin(request)`
- `private_post_user_addsubaccount(request)`
- `private_post_user_cancelwithdrawal(request)`
- `private_post_user_communicationtoken(request)`
- `private_post_user_confirmemail(request)`
- `private_post_user_confirmwithdrawal(request)`
- `private_post_user_logout(request)`
- `private_post_user_preferences(request)`
- `private_post_user_requestwithdrawal(request)`
- `private_post_user_unstakingrequests(request)`
- `private_post_user_updatesubaccount(request)`
- `private_post_user_wallettransfer(request)`
- `private_put_guild(request)`
- `private_put_order(request)`
- `private_delete_order(request)`
- `private_delete_order_all(request)`
- `private_delete_user_unstakingrequests(request)`

### WS Unified

- `describe(self)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_liquidations(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_liquidations_for_symbols(self, symbols: List[str] = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `authenticate(self, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_heartbeat(self, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.