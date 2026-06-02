import pandas as pd
import openpyxl as xl
from binance.client import Client
from src.settings import API_KEY
from src.settings import SECRET_KEY


def download():
    try:

        client = Client(API_KEY, SECRET_KEY)

        ticker = client.get_klines(
            symbol = "WLDUSDT",
            interval = Client.KLINE_INTERVAL_1MINUTE,
            limit = 1000
        )

        df = pd.DataFrame(ticker)

        # df.column ==> [0] open time, [1] open, [2] high, [3] low, [4] close, [5] volume, [6] close time

        df = df[
            [0, 1, 2, 3, 4, 5, 6]
        ]

        df.columns = [
            'open_time',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'close_time'
        ]
    except Exception as e:
        print('ERROR', e)

    df.to_excel('../crypto/data/WLDUSDT_m1.xlsx')

    return
