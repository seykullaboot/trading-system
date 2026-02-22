"""
Executor Bot - Command execution and strategy processing
"""

import logging
from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class CommandType(Enum):
    """Command types"""
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    CANCEL = "CANCEL"
    STOP_LOSS = "STOP_LOSS"
    TAKE_PROFIT = "TAKE_PROFIT"


dataclass
class Command:
    """Command data class"""
    type: CommandType
    symbol: str
    quantity: float
    price: float
    timestamp: str
    priority: int = 0


class ExecutorBot:
    """
    Executes commands and manages strategy execution
    """
    
    def __init__(self, config: Dict):
        """Initialize Executor Bot"""
        self.config = config
        self.command_queue = []
        self.executed_commands = []
        self.active_strategies = {}
        logger.info("Executor Bot initialized")
    
    def queue_command(self, command: Command) -> bool:
        """
        Queue a command for execution
        
        Args:
            command: Command object
            
        Returns:
            Success status
        """
        try:
            self.command_queue.append(command)
            self.command_queue.sort(key=lambda x: x.priority, reverse=True)
            logger.info(f"Command queued: {command.type.value} {command.symbol}")
            return True
        except Exception as e:
            logger.error(f"Failed to queue command: {str(e)}")
            return False
    
    def execute_command(self, command: Command) -> Dict:
        """
        Execute a single command
        
        Args:
            command: Command object
            
        Returns:
            Execution result
        """
        try:
            result = {
                'command_type': command.type.value,
                'symbol': command.symbol,
                'quantity': command.quantity,
                'price': command.price,
                'status': 'EXECUTED',
                'timestamp': command.timestamp
            }
            
            self.executed_commands.append(result)
            logger.info(f"Command executed: {command.type.value}")
            
            return result
        except Exception as e:
            logger.error(f"Command execution failed: {str(e)}")
            return {'status': 'FAILED', 'error': str(e)}
    
    def process_queue(self) -> List[Dict]:
        """
        Process command queue
        
        Returns:
            List of execution results
        """
        results = []
        while self.command_queue:
            command = self.command_queue.pop(0)
            result = self.execute_command(command)
            results.append(result)
        
        logger.info(f"Processed {len(results)} commands")
        return results
    
    def start_strategy(self, strategy_name: str, config: Dict) -> bool:
        """
        Start a trading strategy
        
        Args:
            strategy_name: Strategy identifier
            config: Strategy configuration
            
        Returns:
            Success status
        """
        try:
            self.active_strategies[strategy_name] = {
                'name': strategy_name,
                'config': config,
                'status': 'ACTIVE',
                'commands_executed': 0
            }
            logger.info(f"Strategy started: {strategy_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to start strategy: {str(e)}")
            return False
    
    def stop_strategy(self, strategy_name: str) -> bool:
        """
        Stop a trading strategy
        
        Args:
            strategy_name: Strategy identifier
            
        Returns:
            Success status
        """
        if strategy_name in self.active_strategies:
            self.active_strategies[strategy_name]['status'] = 'STOPPED'
            logger.info(f"Strategy stopped: {strategy_name}")
            return True
        return False
    
    def get_strategy_status(self, strategy_name: str) -> Optional[Dict]:
        """Get strategy status"""
        return self.active_strategies.get(strategy_name)
    
    def get_active_strategies(self) -> List[Dict]:
        """Get all active strategies"""
        return [s for s in self.active_strategies.values() if s['status'] == 'ACTIVE']
    
    def get_executed_commands(self, limit: int = 10) -> List[Dict]:
        """Get recent executed commands"""
        return self.executed_commands[-limit:]


def main():
    """Main function for testing"""
    from datetime import datetime
    
    config = {'max_queue': 100}
    executor = ExecutorBot(config)
    
    # Create and queue commands
    cmd1 = Command(
        type=CommandType.BUY,
        symbol='BTC/USDT',
        quantity=0.5,
        price=45000,
        timestamp=datetime.now().isoformat(),
        priority=1
    )
    
    cmd2 = Command(
        type=CommandType.SELL,
        symbol='ETH/USDT',
        quantity=1.0,
        price=3000,
        timestamp=datetime.now().isoformat(),
        priority=2
    )
    
    executor.queue_command(cmd1)
    executor.queue_command(cmd2)
    
    # Process queue
    results = executor.process_queue()
    print(f"Results: {results}")
    
    # Start strategy
    executor.start_strategy('ma-crossover', {'period': 20})
    print(f"Active strategies: {executor.get_active_strategies()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()