def candle(df):

    # Candle

    df['candle'] = abs(df['close'] - df['open'])

    df['upper_wick'] = df['high'] - df[['open', 'close']].max(axis=1)

    df['lower_wick'] = df[['open', 'close']].min(axis=1) - df['low']

    # Filter Candle

    df['bull_candle'] = df['close'] > df['open']

    df['bear_candle'] = df['close'] < df['open']

    df['bull_1'] = df['close'].shift(-1) > df['close'].shift(-1)

    df['bear_1'] = df['close'].shift(-1) < df['close'].shift(-1)

    df['bull_2'] = df['close'].shift(-2) > df['close'].shift(-2)

    df['bear_2'] = df['close'].shift(-2) < df['close'].shift(-2)

    df['long_candle'] = [
        (df['candle'] <= 0.00150) &
        (df['candle'] >= 0.00140)
    ]
    return df