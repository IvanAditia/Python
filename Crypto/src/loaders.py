import pandas as pd
from src.settings import PATH
from src.cleaners import cleaner

def loader():

    df = pd.read_excel(PATH)

    df = cleaner(df)

    return df
