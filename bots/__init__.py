"""Bots package - Trading System Bot Modules"""
from .trader_bot import TraderBot
from .monitor_bot import MonitorBot
from .analyzer_bot import AnalyzerBot
from .executor_bot import ExecutorBot
__all__ = ['TraderBot', 'MonitorBot', 'AnalyzerBot', 'ExecutorBot']
__version__ = '1.0.0'