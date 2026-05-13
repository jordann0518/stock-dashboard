# Stock & Crypto Tracker

To go along with my interests in data, finance, coding, and AI, I built a command-line stock and crypto dashboard in Python. It pulls real-time stock data, compares multiple tickers side by side, tracks 5-day price trends, and displays live crypto prices... All from your terminal, too.
## Features

- Real-time stock price, change, volume, and market data
- Company overview, including sector, P/E ratio, EPS, beta, and analyst target
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
