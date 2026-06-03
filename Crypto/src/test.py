import pandas as pd
from binance.client import Client
from settings import API_KEY
from settings import SECRET_KEY
from tabulate import tabulate
import json

client = Client(API_KEY, SECRET_KEY)

account = client.get_account()

print(json.dumps(account['canTrade'], indent=2))