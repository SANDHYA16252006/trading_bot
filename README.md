````md
# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with the Binance Futures Testnet API to place BUY/SELL orders with MARKET and LIMIT types.

---

## 📌 Features

- Place BUY and SELL orders
- MARKET and LIMIT order support
- Input validation (symbol, quantity, price)
- Error handling for API failures
- Logging of all trades and errors
- Simple command-line interface (CLI)

---

## ⚙️ Requirements

- Python 3.8+
- Binance Futures Testnet API Key
- requests / python-binance (if used)

---

## 🚀 How to Run

### Market Buy Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
````

### Market Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 90000
```

### Limit Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```

---

## 🔐 Configuration

Create a `.env` file in your project root:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## 📊 Project Structure

```
trading_bot/
│── bot/
│   ├── client.py
│   ├── cli.py
│   ├── logger.py
│── README.md
```

---

## ⚠️ Notes

* This bot runs on Binance Futures Testnet only
* Real trading is NOT enabled
* Minimum quantity rules apply based on Binance contract specifications

---

## 🧠 Future Improvements

* Add Stop Loss / Take Profit
* Add real-time price tracking
* Add portfolio / position tracking
* Add paper trading mode
* Add Streamlit dashboard UI

---
## 👨‍💻 Author

Sandhya B
Computer Science Engineering Student
GitHub: https://github.com/SANDHYA16252006
LinkedIn: https://www.linkedin.com/in/sandhya-b-998b65294

---



```
