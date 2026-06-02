import pandas as pd

def cleaner(df):
    
    df['open_time'] = pd.to_datetime(
        df['open_time'],
        unit='ms'
    )

    df['date'] = df['open_time'].dt.date
    df['time'] = df['open_time'].dt.time

    df = df[
        [
            'date',
            'time',
            'open',
            'high',
            'low',
            'close',
            'volume',
        ]
    ]
    return df