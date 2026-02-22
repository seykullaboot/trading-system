"""
Configuration settings for Trading System
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings"""
    
    # API Configuration
    API_KEY = os.getenv('API_KEY', '')
    API_SECRET = os.getenv('API_SECRET', '')
    API_URL = os.getenv('API_URL', 'https://api.example.com')
    
    # Trading Settings
    SYMBOLS = os.getenv('SYMBOLS', 'BTC/USDT,ETH/USDT').split(',')
    MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', '1.0'))
    STOP_LOSS_PERCENT = float(os.getenv('STOP_LOSS_PERCENT', '5.0'))
    TAKE_PROFIT_PERCENT = float(os.getenv('TAKE_PROFIT_PERCENT', '10.0'))
    
    # Bot Settings
    MONITOR_INTERVAL = int(os.getenv('MONITOR_INTERVAL', '60'))  # seconds
    ANALYZER_PERIOD = int(os.getenv('ANALYZER_PERIOD', '20'))
    EXECUTOR_QUEUE_LIMIT = int(os.getenv('EXECUTOR_QUEUE_LIMIT', '100'))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'trading_system.log')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///trading.db')
    
    # Feature Flags
    ENABLE_LIVE_TRADING = os.getenv('ENABLE_LIVE_TRADING', 'false').lower() == 'true'
    ENABLE_PAPER_TRADING = os.getenv('ENABLE_PAPER_TRADING', 'true').lower() == 'true'
    
    # Risk Management
    MAX_DAILY_LOSS = float(os.getenv('MAX_DAILY_LOSS', '1000.0'))
    MAX_CONCURRENT_TRADES = int(os.getenv('MAX_CONCURRENT_TRADES', '5'))
    
    # Alerts
    ALERT_EMAIL = os.getenv('ALERT_EMAIL', '')
    ENABLE_EMAIL_ALERTS = os.getenv('ENABLE_EMAIL_ALERTS', 'false').lower() == 'true'
    ENABLE_SLACK_ALERTS = os.getenv('ENABLE_SLACK_ALERTS', 'false').lower() == 'true'
    SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK', '')


# Export settings instance
settings = Settings()