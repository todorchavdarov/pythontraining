# Import WebSocket client library
import time
from websocket import create_connection
import json
import pandas as pd
import numpy as np

# Connect to WebSocket API and subscribe to trade feed for XBT/USD and XRP/USD
ws = create_connection("wss://ws.finnhub.io?token=c4mes2aad3iak0au8hj0")
ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
payload_list = []
output = pd.DataFrame()

# how long to collect data for in minute, currently sitting at 3 minutes  (60 seconds * 3)
timeout = time.time() + 60 * 3


#  weighted average price

def wavg(group):
    p = group['p']
    v = group['v']
    return (p * v).sum() / v.sum()


# Loop for certain amount of minutes defined and collect data
while time.time() < timeout:
    if output.empty:
        datadict = json.loads(ws.recv())
        output = pd.DataFrame(datadict["data"][0], index=[0])
    else:
        datadict = json.loads(ws.recv())
        try:
            output2 = pd.DataFrame(datadict["data"][0], index=[0])
        # passing exception since recv() could return a ping json response
        except Exception:
            pass
        output = output.append(output2)

output['t'] = pd.to_datetime(output['t'], unit='ms')
output['t'] = pd.to_datetime(output['t'], unit='ms')

# set the timestamp as an index
output = output.set_index('t')
output.drop(['c', 's'], axis=1, inplace=True)

# return volume weighted average price to a new column in the dataframe
groupedoutput = output.groupby(output.index.to_period('T')).apply(wavg).reset_index(name="VWAP")


print(groupedoutput)
