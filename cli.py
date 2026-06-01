import argparse
import os

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.client import BinanceTestnetClient
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging

console = Console()

load_dotenv()
setup_logging()

client = BinanceTestnetClient(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET")
)

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# -------------------------
# ORDER COMMAND
# -------------------------

order_parser = subparsers.add_parser(
    "order",
    help="Place an order"
)

order_parser.add_argument("--symbol", required=True)
order_parser.add_argument("--side", required=True)
order_parser.add_argument("--type", required=True)
order_parser.add_argument("--quantity", type=float, required=True)
order_parser.add_argument("--price", type=float)

# -------------------------
# BALANCE COMMAND
# -------------------------

subparsers.add_parser(
    "balance",
    help="Show account balance"
)

# -------------------------
# POSITIONS COMMAND
# -------------------------

subparsers.add_parser(
    "positions",
    help="Show open positions"
)

# -------------------------
# OPEN ORDERS COMMAND
# -------------------------

subparsers.add_parser(
    "open-orders",
    help="Show open orders"
)

args = parser.parse_args()

try:

    if args.command == "balance":

        balances = client.get_balance()

        table = Table(title="Account Balance")

        table.add_column("Asset")
        table.add_column("Balance")
        table.add_column("Available")

        for b in balances:
            if float(b["balance"]) > 0:
                table.add_row(
                    b["asset"],
                    b["balance"],
                    b["availableBalance"]
                )

        console.print(table)

    elif args.command == "positions":

        positions = client.get_positions()

        table = Table(title="Open Positions")

        table.add_column("Symbol")
        table.add_column("Amount")
        table.add_column("Entry Price")
        table.add_column("PnL")

        for p in positions:
            if float(p["positionAmt"]) != 0:
                table.add_row(
                    p["symbol"],
                    p["positionAmt"],
                    p["entryPrice"],
                    p["unRealizedProfit"]
                )

        console.print(table)

    elif args.command == "open-orders":

        orders = client.get_open_orders()

        table = Table(title="Open Orders")

        table.add_column("Order ID")
        table.add_column("Symbol")
        table.add_column("Side")
        table.add_column("Type")
        table.add_column("Status")

        for o in orders:
            table.add_row(
                str(o["orderId"]),
                o["symbol"],
                o["side"],
                o["type"],
                o["status"]
            )

        console.print(table)

    elif args.command == "order":

        validate_side(args.side)
        validate_order_type(args.type)

        if args.quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        if args.type == "LIMIT" and args.price is None:
            raise ValueError(
                "LIMIT orders require --price"
            )

        console.print(
            Panel.fit(
                f"""
Symbol   : {args.symbol}
Side     : {args.side}
Type     : {args.type}
Quantity : {args.quantity}
Price    : {args.price if args.price else 'Market Price'}
""",
                title="Order Summary"
            )
        )

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        console.print(
            f"[green]✓ Order placed successfully[/green]"
        )

        console.print(response)

except Exception as e:
    console.print(
        f"[red]✗ Error: {e}[/red]"
    )