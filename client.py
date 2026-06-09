import os
import time
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceClient:

    def __init__(self):

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

        # Debug prints
        print("API Key loaded:", bool(self.api_key))
        print("Secret loaded:", bool(self.secret_key))

        # Connect using Binance Testnet
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.secret_key,
            testnet=True
        )

        # Sync local time with Binance server time
        server_time = self.client.get_server_time()
        self.client.timestamp_offset = (
            server_time["serverTime"] - int(time.time() * 1000)
        )

    def create_order(self, order_data):

        symbol = order_data["symbol"]
        side = order_data["side"]
        order_type = order_data["type"]
        quantity = order_data["quantity"]
        price = order_data.get("price")

        try:

            if order_type == "MARKET":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity,
                    recvWindow=10000
                )

            elif order_type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=str(price),
                    recvWindow=10000
                )

        except Exception as e:
            return {"error": str(e)}