"""
Trader Bot - Executes buy/sell orders and manages portfolio
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class TraderBot:
    """
    Handles order execution and portfolio management
    """
    
    def __init__(self, config: Dict):
        """Initialize Trader Bot"""
        self.config = config
        self.portfolio = {}
        self.orders = []
        self.positions = {}
        logger.info("Trader Bot initialized")
    
    def execute_buy_order(self, symbol: str, quantity: float, price: float) -> Dict:
        """
        Execute a buy order
        
        Args:
            symbol: Trading symbol (e.g., 'BTC/USDT')
            quantity: Number of units to buy
            price: Price per unit
            
        Returns:
            Order confirmation dict
        """
        try:
            order = {
                'id': len(self.orders) + 1,
                'type': 'BUY',
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
                'timestamp': datetime.now().isoformat(),
                'status': 'EXECUTED'
            }
            
            # Update portfolio
            cost = quantity * price
            if symbol not in self.positions:
                self.positions[symbol] = 0
            self.positions[symbol] += quantity
            
            self.orders.append(order)
            logger.info(f"Buy order executed: {symbol} x {quantity} @ {price}")
            
            return order
        except Exception as e:
            logger.error(f"Buy order failed: {str(e)}")
            return {'status': 'FAILED', 'error': str(e)}
    
    def execute_sell_order(self, symbol: str, quantity: float, price: float) -> Dict:
        """
        Execute a sell order
        
        Args:
            symbol: Trading symbol
            quantity: Number of units to sell
            price: Price per unit
            
        Returns:
            Order confirmation dict
        """
        try:
            if symbol not in self.positions or self.positions[symbol] < quantity:
                raise ValueError(f"Insufficient position for {symbol}")
            
            order = {
                'id': len(self.orders) + 1,
                'type': 'SELL',
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
                'timestamp': datetime.now().isoformat(),
                'status': 'EXECUTED'
            }
            
            # Update portfolio
            self.positions[symbol] -= quantity
            self.orders.append(order)
            logger.info(f"Sell order executed: {symbol} x {quantity} @ {price}")
            
            return order
        except Exception as e:
            logger.error(f"Sell order failed: {str(e)}")
            return {'status': 'FAILED', 'error': str(e)}
    
    def get_portfolio(self) -> Dict:
        """Get current portfolio positions"""
        return self.positions.copy()
    
    def get_orders(self, limit: int = 10) -> List[Dict]:
        """Get recent orders"""
        return self.orders[-limit:]
    
    def cancel_order(self, order_id: int) -> bool:
        """Cancel a pending order"""
        for order in self.orders:
            if order['id'] == order_id and order['status'] == 'PENDING':
                order['status'] = 'CANCELLED'
                logger.info(f"Order {order_id} cancelled")
                return True
        return False


def main():
    """Main function for testing"""
    config = {
        'api_key': 'test_key',
        'api_secret': 'test_secret'
    }
    
    trader = TraderBot(config)
    
    # Test buy order
    buy_order = trader.execute_buy_order('BTC/USDT', 0.5, 45000)
    print(f"Buy Order: {buy_order}")
    
    # Test sell order
    sell_order = trader.execute_sell_order('BTC/USDT', 0.2, 46000)
    print(f"Sell Order: {sell_order}")
    
    # Get portfolio
    portfolio = trader.get_portfolio()
    print(f"Portfolio: {portfolio}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()