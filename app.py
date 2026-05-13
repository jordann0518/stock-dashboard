import yfinance as yf

def g(t): return f"\033[92m{t}\033[0m"
def r(t): return f"\033[91m{t}\033[0m"
def c(t): return f"\033[96m{t}\033[0m"
def y(t): return f"\033[93m{t}\033[0m"
def b(t): return f"\033[1m{t}\033[0m"

def divider(): print(c("=" * 48))

def fmt_cap(cap):
    if not cap or cap == "N/A":
        return "N/A"
    try:
        cap = int(cap)
        if cap >= 1_000_000_000_000:
            return f"${cap / 1_000_000_000_000:.1f}T"
        elif cap >= 1_000_000_000:
            return f"${cap / 1_000_000_000:.1f}B"
        elif cap >= 1_000_000:
            return f"${cap / 1_000_000:.1f}M"
        else:
            return f"${cap:,}"
    except:
        return "N/A"

def show_stock(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    name = info.get("longName") or info.get("shortName") or ticker
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    prev_close = info.get("previousClose")
    open_price = info.get("open")
    high = info.get("dayHigh")
    low = info.get("dayLow")
    volume = info.get("volume")
    week_high = info.get("fiftyTwoWeekHigh")
    week_low = info.get("fiftyTwoWeekLow")
    cap = info.get("marketCap")
    pe = info.get("trailingPE")
    eps = info.get("trailingEps")
    beta = info.get("beta")
    div_yield = info.get("dividendYield")
    target = info.get("targetMeanPrice")
    sector = info.get("sector")
    industry = info.get("industry")

    if not price:
        print(r(f"  No data found for {ticker}. Check the ticker and try again."))
        return

    change = price - prev_close if price and prev_close else 0
    change_pct = (change / prev_close * 100) if prev_close else 0
    arrow = "▲" if change >= 0 else "▼"
    change_color = g if change >= 0 else r

    divider()
    print(f"  {b(name)} ({ticker.upper()})")
    divider()
    print(f"  {'Price:':<22} {b('$' + f'{price:.2f}')}")
    print(f"  {'Change:':<22} {change_color(arrow + ' ' + f'{change:+.2f}' + ' (' + f'{change_pct:+.2f}%)')}")
    print(f"  {'Open:':<22} ${open_price:.2f}" if open_price else f"  {'Open:':<22} N/A")
    print(f"  {'High:':<22} ${high:.2f}" if high else f"  {'High:':<22} N/A")
    print(f"  {'Low:':<22} ${low:.2f}" if low else f"  {'Low:':<22} N/A")
    print(f"  {'Prev Close:':<22} ${prev_close:.2f}" if prev_close else f"  {'Prev Close:':<22} N/A")
    print(f"  {'Volume:':<22} {volume:,}" if volume else f"  {'Volume:':<22} N/A")
    print(c("-" * 48))
    print(f"  {'Sector:':<22} {sector or 'N/A'}")
    print(f"  {'Industry:':<22} {industry or 'N/A'}")
    print(f"  {'Market Cap:':<22} {fmt_cap(cap)}")
    print(f"  {'P/E Ratio:':<22} {round(pe, 2) if pe else 'N/A'}")
    print(f"  {'EPS:':<22} {round(eps, 2) if eps else 'N/A'}")
    print(f"  {'Dividend Yield:':<22} {str(round(div_yield * 100, 2)) + '%' if div_yield else 'N/A'}")
    print(f"  {'52 Wk High:':<22} ${week_high:.2f}" if week_high else f"  {'52 Wk High:':<22} N/A")
    print(f"  {'52 Wk Low:':<22} ${week_low:.2f}" if week_low else f"  {'52 Wk Low:':<22} N/A")
    print(f"  {'Analyst Target:':<22} ${target:.2f}" if target else f"  {'Analyst Target:':<22} N/A")
    print(f"  {'Beta:':<22} {round(beta, 2) if beta else 'N/A'}")
    divider()
    print()

def show_trend(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")
    if hist.empty:
        print(y("  No trend data available."))
        return
    info = stock.info
    name = info.get("longName") or ticker
    print(f"\n  {b('5-Day Price Trend:')} {name}")
    print(c("-" * 48))
    for date, row in hist.iterrows():
        date_str = date.strftime("%a %b %d")
        close = row["Close"]
        vol = int(row["Volume"])
        print(f"    {date_str}   ${close:.2f}   Vol: {vol:,}")
    print()

def show_crypto(symbol):
    ticker = symbol + "-USD"
    stock = yf.Ticker(ticker)
    info = stock.info
    name = info.get("longName") or info.get("shortName") or symbol
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    prev_close = info.get("previousClose")
    volume = info.get("volume")
    cap = info.get("marketCap")
    week_high = info.get("fiftyTwoWeekHigh")
    week_low = info.get("fiftyTwoWeekLow")

    if not price:
        print(r(f"  No crypto data found for {symbol}."))
        return

    change = price - prev_close if price and prev_close else 0
    change_pct = (change / prev_close * 100) if prev_close else 0
    arrow = "▲" if change >= 0 else "▼"
    change_color = g if change >= 0 else r

    divider()
    print(f"  {b(name)} ({symbol.upper()})")
    divider()
    print(f"  {'Price (USD):':<22} {b('$' + f'{price:,.2f}')}")
    print(f"  {'Change:':<22} {change_color(arrow + ' ' + f'{change:+.2f}' + ' (' + f'{change_pct:+.2f}%)')}")
    print(f"  {'Volume:':<22} {volume:,}" if volume else f"  {'Volume:':<22} N/A")
    print(f"  {'Market Cap:':<22} {fmt_cap(cap)}")
    print(f"  {'52 Wk High:':<22} ${week_high:.2f}" if week_high else f"  {'52 Wk High:':<22} N/A")
    print(f"  {'52 Wk Low:':<22} ${week_low:.2f}" if week_low else f"  {'52 Wk Low:':<22} N/A")
    divider()
    print()

def show_compare(tickers):
    print(f"\n  {b('Stock Comparison:')}")
    print(c("=" * 72))
    print(f"  {'Ticker':<8} {'Price':>10} {'Change':>12} {'Mkt Cap':>12} {'P/E':>8} {'52W High':>10} {'52W Low':>10}")
    print(c("-" * 72))
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("currentPrice") or info.get("regularMarketPrice")
        prev_close = info.get("previousClose")
        cap = info.get("marketCap")
        pe = info.get("trailingPE")
        week_high = info.get("fiftyTwoWeekHigh")
        week_low = info.get("fiftyTwoWeekLow")
        if not price:
            print(r(f"  {ticker:<8} No data found"))
            continue
        change = price - prev_close if prev_close else 0
        change_pct = (change / prev_close * 100) if prev_close else 0
        change_color = g if change >= 0 else r
        change_str = f"{change_pct:+.2f}%"
        print(f"  {ticker:<8} ${price:>9.2f} {change_color(f'{change_str:>11}')} {fmt_cap(cap):>12} {str(round(pe, 1)) + 'x' if pe else 'N/A':>8} ${week_high:>9.2f} ${week_low:>9.2f}")
    print(c("=" * 72))
    print()

def print_help():
    print(f"""
  {b('Commands:')}
    {y('AAPL')}                look up a stock
    {y('AAPL AMZN TSLA')}      compare multiple stocks side by side
    {y('trend AAPL')}          5 day price trend
    {y('crypto BTC')}          crypto price (BTC, ETH, DOGE, etc.)
    {y('help')}                show this menu
    {y('quit')}                exit
""")

def main():
    print(c(b("\n=== Stock & Crypto Tracker ===")))
    print_help()
    while True:
        try:
            user_input = input("  Enter command: ").strip().upper()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        if not user_input:
            continue
        elif user_input == "QUIT":
            print("Goodbye!")
            break
        elif user_input == "HELP":
            print_help()
        elif user_input.startswith("CRYPTO "):
            show_crypto(user_input.split(" ", 1)[1])
        elif user_input.startswith("TREND "):
            show_trend(user_input.split(" ", 1)[1])
        else:
            tickers = user_input.split()
            if len(tickers) > 1:
                show_compare(tickers)
            else:
                show_stock(tickers[0])

if __name__ == "__main__":
    main()