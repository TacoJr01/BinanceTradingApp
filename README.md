# Binance Futures Testnet Trading Bot

## Setup
1. Create a Binance Futures Testnet account.
2. Copy .env.example to .env and add API keys.
3. Install dependencies:

pip install -r requirements.txt

## Run

Market order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

## Notes
- Uses Binance Futures Testnet.
- Logs requests/responses to trading_bot.log.
- Supports BUY/SELL and MARKET/LIMIT orders.
