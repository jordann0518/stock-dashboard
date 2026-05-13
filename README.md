# Stock & Crypto Tracker

A command-line stock and crypto dashboard built with Python. Look up real-time stock data, compare multiple tickers side by side, track 5-day price trends, and check live crypto prices — all from your terminal.

## Features

- Real-time stock price, change, volume, and market data
- Company overview including sector, P/E ratio, EPS, beta, and analyst target
- Side-by-side comparison of multiple stocks
- 5-day price trend with daily close and volume
- Live crypto prices with 52-week range and market cap
- Color-coded output — green for gains, red for losses

## Built With

- Python 3
- yfinance — real-time market data
- No API key required

## Usage

Run the app:

```bash
python app.py
```

Commands:

| Command | Description |
|---|---|
| `AAPL` | Look up a single stock |
| `AAPL AMZN TSLA` | Compare multiple stocks |
| `trend AAPL` | 5-day price trend |
| `crypto BTC` | Crypto price |
| `help` | Show all commands |
| `quit` | Exit |

## Examples
