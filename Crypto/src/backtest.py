from src.risk import trade_param
import pandas as pd




def backtest(df):

    # State

    position = None
    initial_balance = trade_param['balance']
    balance = initial_balance
    equity_curve = []
    trades = []
    risk = balance * trade_param['risk_per_trade']
    
    
    for i in range(14, len(df)):

        data = df.iloc[i]
        equity_curve.append(balance)

        # Entry

        if position is None:
            
            # LONG

            if data['buy_signal']:
                entry = data['close']
                
                if pd.isna(data['sd']):
                    continue

                sl = entry - data['sd']

                tp = entry + (2 * data['sd'])

                stop_distance = entry - sl

                qty = risk / stop_distance

                notional = qty * entry

                margin = notional / trade_param['leverage']

                if margin > balance :
                    continue

                fee = notional * trade_param['taker_fee']

                balance -= fee

                position = {
                    'side' : 'LONG',
                    'entry' : entry,
                    'sl' : sl,
                    'tp' : tp,
                    'qty' : qty,
                    'margin' : margin,
                    'entry_index' : i
                }
            elif data['sell_signal']:
                entry = data['close']

                if pd.isna(data['sd']):
                    continue

                sl = entry + data['sd']
                
                tp = entry -  (2 * data['sd'])

                stop_distance = sl - entry

                qty = risk / stop_distance

                notional = qty * entry

                margin = notional / trade_param['leverage']

                if margin > balance :
                    continue

                fee = notional * trade_param['taker_fee']

                balance -= fee

                position = {
                    
                    'side' : 'SHORT',
                    'entry' : entry,
                    'sl' : sl,
                    'tp' : tp,
                    'qty' : qty,
                    'margin' : margin,
                    'entry_index' : i
                }

        # MANAGE POSITION

        else:
            
            high = data['high']
            low = data['low']
            exit_price = None
            reason = None

            # LONG

            if position['side'] == 'LONG':
                if low <= position['sl']:
                    exit_price = position['sl']
                    reason = 'SL'

                elif high >= position['tp']:
                    exit_price = position['tp']
                    reason = 'TP'

                if exit_price:
                    pnl =(
                        exit_price - position['entry']
                    ) * position['qty']

                    fee = (
                        exit_price * position['qty']
                    ) * trade_param['taker_fee']

                    pnl -= fee

                    balance += pnl

                    trades.append({
                        'side': 'LONG',
                        'entry': position['entry'],
                        'exit' : exit_price,
                        'qty' : position['qty'],
                        'pnl' : pnl,
                        'reason' : reason
                    })

                    position = None
            
            # SHORT

            if position['side'] == 'SHORT':
                if high >= position['sl']:
                    exit_price = position['sl']
                    reason = 'SL'

                elif low <= position['tp']:
                    exit_price = position['tp']
                    reason = 'TP'

                if exit_price:
                    pnl =(
                        exit_price - position['entry']
                    ) * position['qty']

                    fee = (
                        exit_price * position['qty']
                    ) * trade_param['taker_fee']

                    pnl -= fee

                    balance += pnl

                    trades.append({
                        'side' : 'SHORT',
                        'entry' : position['entry'],
                        'exit' : exit_price,
                        'qty' : position['qty'],
                        'pnl' : pnl,
                        'reason' : reason
                    })

                    position = None

    # Result

    trade = pd.DataFrame(trades)

    print(trade.tail())

    return df