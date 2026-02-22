import pandas as pd
import numpy as np

class AnalyzerBot:
    def __init__(self, data):
        self.data = data

    def calculate_sma(self, window):
        return self.data['close'].rolling(window=window).mean()

    def calculate_rsi(self, window):
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def generate_signals(self):
        self.data['sma'] = self.calculate_sma(14)
        self.data['rsi'] = self.calculate_rsi(14)
        conditions = [
            (self.data['rsi'] < 30),
            (self.data['rsi'] > 70)
        ]
        choices = ['buy', 'sell']
        self.data['signal'] = np.select(conditions, choices, default='hold')
        return self.data[['close', 'sma', 'rsi', 'signal']]

# Example usage:
# df = pd.DataFrame({'close': [insert_close_price_data_here]})
# bot = AnalyzerBot(df)
# trading_signals = bot.generate_signals()