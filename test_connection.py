from binance.um_futures import UMFutures

API_KEY = "jLAdfyzNaF2rWMXFdKPsBnHoTvC7BdNzADOEEE7Q1syGVKqKqXDZCnS3RYCJqTzB"
API_SECRET = "yQwqVDopU8d3UMyOolX8VbvCEV3M8oHB28clnRVgU4tA7KmXYFtboUiKXdBUDmyE"

client = UMFutures(
    key=API_KEY,
    secret=API_SECRET,
    base_url="https://testnet.binancefuture.com"
)

try:
    account = client.account()
    print("✅ Connected Successfully!")
    print(account)
except Exception as e:
    print("❌ Connection Failed:")
    print(e)