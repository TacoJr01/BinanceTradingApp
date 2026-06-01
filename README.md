# Binance Futures Testnet Trading Bot

## Overview

A Python CLI application for placing and managing Binance Futures Testnet (USDT-M) orders.

Features:

* Market Orders
* Limit Orders
* BUY and SELL support
* Account Balance Lookup
* Open Positions Lookup
* Open Orders Lookup
* Input Validation
* Structured Logging
* Error Handling
* Rich CLI Output

---

## Project Structure

```text
trading_bot_assignment/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── trading_bot.log
```

---

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd trading_bot_assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

## Binance Futures Testnet

The application connects to:

```text
https://testnet.binancefuture.com/fapi
```

No real funds are used.

---

## Commands

### Check Balance

```bash
python cli.py balance
```

Example Output:

```text
Asset   Balance     Available
USDT    5000.00     4990.00
BTC     0.0100      0.0100
```

---

### View Positions

```bash
python cli.py positions
```

Displays all open futures positions.

---

### View Open Orders

```bash
python cli.py open-orders
```

Displays all currently active orders.

---

### Place Market BUY Order

```bash
python cli.py order \
  --symbol BTCUSDT \
  --side BUY \
  --type MARKET \
  --quantity 0.001
```

---

### Place Market SELL Order

```bash
python cli.py order \
  --symbol BTCUSDT \
  --side SELL \
  --type MARKET \
  --quantity 0.001
```

---

### Place Limit BUY Order

```bash
python cli.py order \
  --symbol BTCUSDT \
  --side BUY \
  --type LIMIT \
  --quantity 0.001 \
  --price 50000
```

---

### Place Limit SELL Order

```bash
python cli.py order \
  --symbol BTCUSDT \
  --side SELL \
  --type LIMIT \
  --quantity 0.001 \
  --price 150000
```

---

## Validation

The application validates:

* Order Side (BUY / SELL)
* Order Type (MARKET / LIMIT)
* Quantity > 0
* LIMIT orders require a price

---

## Logging

All API requests, responses, and errors are logged to:

```text
trading_bot.log
```

Example:

```text
Request: {...}
Response: {...}
```

---

## Assumptions

* Binance Futures Testnet account is active.
* Valid API credentials are configured.
* User has sufficient testnet balance.
* Internet connection is available.

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* Rich
* argparse

---

## Sample Log Files

The repository includes logs generated from:

* One MARKET order
* One LIMIT order

as required by the assignment.
