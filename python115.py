import numpy
import websocket
import json
from datetime import datetime
import pandas as pd
import numpy as np

df_trades = pd.DataFrame()
payload_list = []


def on_message(ws, message):
    datadict = json.loads(message)
    global df_trades
    # payload_list.append(datadict.copy())

    output = pd.DataFrame(datadict["data"][0], index=[0])
    output['t'] = pd.to_datetime(output['t'], unit='ms')
    output = output.set_index('t')

    date = datetime.fromtimestamp(datadict["data"][0]["t"] // 1000)
    print("Timestamp", date, "Price: ", datadict["data"][0]["p"], "Volume", datadict["data"][0]["v"])
    # if df_trades.empty:
    #     df_trades = output
    # else:
    #     df_trades = df_trades.append(output)

    # print(payload_list)
    # print(datadict)
    # return datadict


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


# def func(df):
#     timestep = 60
#     seconds = (df.index.minute*60+df.index.second)-timestep
#     weight = [k/timestep if n == 0 else (seconds[n] - seconds[n - 1])/timestep
#               for n, k in enumerate(seconds)]
#     return np.sum(weight*df.values)
#
#
# df_trades.resample('1min', closed='right').apply(func)

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c4mes2aad3iak0au8hj0",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    #df_trades = pd.DataFrame(payload_list)
    #print(payload_list)
    ws.on_open = on_open
    ws.run_forever()
