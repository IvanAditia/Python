from src.download import download
import sys

mode = sys.argv[1]

def crypto():
    if mode == 'download':
        download()

crypto()