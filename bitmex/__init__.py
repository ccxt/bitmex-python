import sys
import bitmex.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from bitmex.ccxt import bitmex as BitmexSync
from bitmex.ccxt.async_support.bitmex import bitmex as BitmexAsync
from bitmex.ccxt.pro.bitmex import bitmex as BitmexWs
