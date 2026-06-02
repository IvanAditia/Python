
def signal(df):
    df['buy_signal'] = [
        (df['close'] > df['mean']) &
        (df['adx'] > 15) &
        (df['long_candle']) &
        (df['bull_1']) &
        (df['bull_2']) 
    ]

    df['sell_signal'] = [
        (df['close'] < df['mean']) &
        (df['adx'] > 15) &
        (df['long_candle']) &
        (df['bear_1']) &
        (df['bear_2']) 
    ]

    df['exit_buy_signal'] = [
        (df['close'] < df['mean'])  &
        (df['adx'] <= 15)
    ]

    df['exit_buy_signal'] = [
        (df['close'] > df['mean'])  &
        (df['adx'] <= 15)
    ]
    return df