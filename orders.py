from bot.client import BinanceClient
from bot.logging_config import logger

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price
    }

    logger.info(f"ORDER REQUEST: {order_data}")

    response = client.create_order(order_data)

    # 🔥 PRINT RAW RESPONSE (IMPORTANT)
    print("\nRAW BINANCE RESPONSE:")
    print(response)

    logger.info(f"ORDER RESPONSE: {response}")

    return response