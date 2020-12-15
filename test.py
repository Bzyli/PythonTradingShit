# import the libraries we need
import shrimpy
import plotly.graph_objects as go

# insert your public and secret keys here
public_key = '8x71n32d8cfbnnn1xzimjustkeyboardmashing8xn1t8jyv5098'
secret_key = '771dc5nxct4709672v4n09xn0morekeyboardmashing9475c029374n0xx4n50'

# create the client
client = shrimpy.ShrimpyApiClient(public_key, secret_key)

# get the candles
candles = client.get_candles(
    'binance',  # exchange
    'XLM',      # base_trading_symbol
    'BTC',      # quote_trading_symbol
    '15m'       # interval
)

# create lists to hold our different data elements
dates = []
open_data = []
high_data = []
low_data = []
close_data = []

# convert from the Shrimpy candlesticks to the plotly graph objects format
for candle in candles:
    dates.append(candle['time'])
    open_data.append(candle['open'])
    high_data.append(candle['high'])
    low_data.append(candle['low'])
    close_data.append(candle['close'])

# construct the figure
fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])

# display our graph
fig.show()