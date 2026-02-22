"""
Analyzer Bot - Technical analysis and signal generation
"""

import logging
from typing import Dict, List, Optional, Tuple
from collections import deque

logger = logging.getLogger(__name__)


class AnalyzerBot:
    """
    Performs technical analysis and generates trading signals
    """
    
    def __init__(self, config: Dict):
        """Initialize Analyzer Bot"""
        self.config = config
        self.price_history = {}
        self.signals = []
        self.max_history = config.get('max_history', 100)
        logger.info("Analyzer Bot initialized")
    
    def add_price(self, symbol: str, price: float) -> None:
        """
        Add price to history
        
        Args:
            symbol: Trading symbol
            price: Price value
        """
        if symbol not in self.price_history:
            self.price_history[symbol] = deque(maxlen=self.max_history)
        
        self.price_history[symbol].append(price)
    
    def calculate_sma(self, symbol: str, period: int = 20) -> Optional[float]:
        """
        Calculate Simple Moving Average
        
        Args:
            symbol: Trading symbol
            period: Period for SMA
            
        Returns:
            SMA value or None
        """
        prices = self.price_history.get(symbol, [])
        if len(prices) < period:
            return None
        
        recent = list(prices)[-period:]
        return sum(recent) / len(recent)
    
    def calculate_rsi(self, symbol: str, period: int = 14) -> Optional[float]:
        """
        Calculate Relative Strength Index
        
        Args:
            symbol: Trading symbol
            period: Period for RSI
            
        Returns:
            RSI value (0-100) or None
        """
        prices = list(self.price_history.get(symbol, []))
        if len(prices) < period + 1:
            return None
        
        recent = prices[-period:]
        gains = sum(max(recent[i] - recent[i-1], 0) for i in range(1, len(recent)))
        losses = sum(max(recent[i-1] - recent[i], 0) for i in range(1, len(recent)))
        
        avg_gain = gains / period
        avg_loss = losses / period
        
        if avg_loss == 0:
            return 100 if avg_gain > 0 else 50
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def generate_signal(self, symbol: str) -> Optional[str]:
        """
        Generate trading signal based on analysis
        
        Args:
            symbol: Trading symbol
            
        Returns:
            Signal: 'BUY', 'SELL', or None
        """
        sma = self.calculate_sma(symbol)
        rsi = self.calculate_rsi(symbol)
        
        if sma is None or rsi is None:
            return None
        
        current_price = list(self.price_history.get(symbol, []))[-1]
        
        # Buy signal: price above SMA and RSI < 30
        if current_price > sma and rsi < 30:
            signal = 'BUY'
        # Sell signal: price below SMA and RSI > 70
        elif current_price < sma and rsi > 70:
            signal = 'SELL'
        else:
            signal = 'HOLD'
        
        # Log signal
        signal_obj = {
            'symbol': symbol,
            'signal': signal,
            'price': current_price,
            'sma': sma,
            'rsi': rsi
        }
        self.signals.append(signal_obj)
        
        logger.info(f"Signal for {symbol}: {signal} (RSI: {rsi:.2f})")
        return signal
    
    def get_signals(self, symbol: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """
        Get recent signals
        
        Args:
            symbol: Filter by symbol (optional)
            limit: Number of signals to return
            
        Returns:
            List of signals
        """
        signals = self.signals
        if symbol:
            signals = [s for s in signals if s['symbol'] == symbol]
        return signals[-limit:]
    
    def analyze(self, symbol: str) -> Dict:
        """
        Perform full analysis
        
        Args:
            symbol: Trading symbol
            
        Returns:
            Analysis results
        """
        sma = self.calculate_sma(symbol)
        rsi = self.calculate_rsi(symbol)
        signal = self.generate_signal(symbol)
        
        current_price = list(self.price_history.get(symbol, []))[-1] \
            if symbol in self.price_history else None
        
        return {
            'symbol': symbol,
            'current_price': current_price,
            'sma': sma,
            'rsi': rsi,
            'signal': signal
        }


def main():
    """Main function for testing"""
    config = {'max_history': 100}
    analyzer = AnalyzerBot(config)
    
    # Simulate price data
    prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 109, 110]
    for price in prices:
        analyzer.add_price('BTC/USDT', price)
    
    # Analyze
    analysis = analyzer.analyze('BTC/USDT')
    print(f"Analysis: {analysis}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()