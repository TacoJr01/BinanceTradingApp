from binance.client import Client

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)

    def get_order(self, symbol, order_id):
        return self.client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

    def get_balance(self):
        return self.client.futures_account_balance()

    def get_positions(self):
        return self.client.futures_position_information()

    def get_open_orders(self):
        return self.client.futures_get_open_orders()