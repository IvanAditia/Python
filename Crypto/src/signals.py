from src.indicator import indicator

def signal(df):
    df = indicator(df)
    print(df['mean'].tail(1))
    return