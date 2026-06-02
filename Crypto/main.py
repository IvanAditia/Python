from src.download import download
from src.loaders import loader
from src.indicator import indicator
from src.candle import candle
from src.signals import signal
import sys

mode = sys.argv[1]

df = loader()

def crypto(df):
    if mode == 'download':
        download()
    elif mode == 'loader':
        loader()
    elif mode == 'indicator':
        indicator(df)
    elif mode == 'candle':
        candle(df)
    elif mode == 'signal':
        signal(df)

crypto(df)