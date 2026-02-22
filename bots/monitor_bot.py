"""
Monitor Bot - Real-time market monitoring and alerts
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class MonitorBot:
    """
    Monitors market data and generates alerts
    """
    
    def __init__(self, config: Dict):
        """Initialize Monitor Bot"""
        self.config = config
        self.price_data = {}
        self.alerts = []
        self.watched_symbols = set()
        logger.info("Monitor Bot initialized")
    
    def add_watch(self, symbol: str, alert_price: Optional[float] = None) -> bool:
        """
        Add symbol to watch list
        
        Args:
            symbol: Trading symbol
            alert_price: Price threshold for alerts
            
        Returns:
            Success status
        """
        try:
            self.watched_symbols.add(symbol)
            if symbol not in self.price_data:
                self.price_data[symbol] = {
                    'current': 0,
                    'high': 0,
                    'low': float('inf'),
                    'alert_price': alert_price
                }
            logger.info(f"Now watching {symbol}")
            return True
        except Exception as e:
            logger.error(f"Failed to watch {symbol}: {str(e)}")
            return False
    
    def update_price(self, symbol: str, price: float) -> None:
        """
        Update price for a symbol
        
        Args:
            symbol: Trading symbol
            price: Current price
        """
        if symbol not in self.price_data:
            self.price_data[symbol] = {'current': price, 'high': price, 'low': price}
        else:
            self.price_data[symbol]['current'] = price
            self.price_data[symbol]['high'] = max(
                self.price_data[symbol]['high'], price
            )
            self.price_data[symbol]['low'] = min(
                self.price_data[symbol]['low'], price
            )
        
        # Check for alerts
        self._check_alerts(symbol, price)
    
    def _check_alerts(self, symbol: str, price: float) -> None:
        """Check if alert conditions are met"""
        data = self.price_data.get(symbol, {})
        alert_price = data.get('alert_price')
        
        if alert_price and price >= alert_price:
            alert = {
                'symbol': symbol,
                'price': price,
                'alert_price': alert_price,
                'timestamp': datetime.now().isoformat(),
                'type': 'PRICE_ALERT'
            }
            self.alerts.append(alert)
            logger.warning(f"Alert: {symbol} reached {price}")
    
    def get_price(self, symbol: str) -> Optional[float]:
        """Get current price for symbol"""
        return self.price_data.get(symbol, {}).get('current')
    
    def get_market_data(self, symbol: str) -> Optional[Dict]:
        """Get full market data for symbol"""
        return self.price_data.get(symbol)
    
    def get_alerts(self, limit: int = 10) -> List[Dict]:
        """Get recent alerts"""
        return self.alerts[-limit:]
    
    def get_watched_symbols(self) -> List[str]:
        """Get all watched symbols"""
        return list(self.watched_symbols)
    
    def get_volatility(self, symbol: str) -> Optional[float]:
        """Calculate volatility (high - low)"""
        data = self.price_data.get(symbol)
        if data:
            return data['high'] - data['low']
        return None


def main():
    """Main function for testing"""
    config = {'api_key': 'test_key'}
    
    monitor = MonitorBot(config)
    
    # Add symbols to watch
    monitor.add_watch('BTC/USDT', alert_price=45000)
    monitor.add_watch('ETH/USDT', alert_price=3000)
    
    # Update prices
    monitor.update_price('BTC/USDT', 45100)
    monitor.update_price('ETH/USDT', 2950)
    
    # Get data
    print(f"BTC Price: {monitor.get_price('BTC/USDT')}")
    print(f"Alerts: {monitor.get_alerts()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()