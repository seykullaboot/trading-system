# Trading System - Phase 1

## Overview
Multi-bot trading system with 4 base bots working together.

## Phase 1: 4 Base Bots

### 1. Trader Bot 🤖
- Executes buy/sell orders
- Manages portfolio
- Tracks positions

### 2. Monitor Bot 👁️
- Real-time market monitoring
- Price tracking
- Alert system

### 3. Analyzer Bot 🧠
- Technical analysis
- Pattern recognition
- Signal generation

### 4. Executor Bot ⚙️
- Process commands
- Execute strategies
- Risk management

## Project Structure
```
trading-system/
├── bots/
│   ├── trader_bot.py
│   ├── monitor_bot.py
│   ├── analyzer_bot.py
│   └── executor_bot.py
├── config/
│   └── settings.py
├── tests/
│   └── test_bots.py
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## Installation

### Requirements
- Python 3.8+
- Docker & Docker Compose
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/seykullaboot/trading-system.git
cd trading-system

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run with Docker
docker-compose up -d
```

## Configuration
See `.env.example` for all available settings.

## Running the Bots

### Individual Bot
```bash
python -m bots.trader_bot
```

### All Bots (Docker)
```bash
docker-compose up
```

## Testing
```bash
pytest tests/
```

## Phase 1 Features
- ✅ Basic bot architecture
- ✅ Event-driven system
- ✅ Real-time data processing
- ✅ Order execution
- ✅ Portfolio tracking

## Next Phases
- Phase 2: Advanced strategies
- Phase 3: Machine learning
- Phase 4: Production deployment

## License
MIT

## Author
@seykullaboot