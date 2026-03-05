import yfinance as yf

def fetch_stock_data(stock, period = "5y"):
        data = yf.download(stock, period = period, auto_adjust = True, progress = False)
        if data.empty:
            return None, "Stock not found"
        else:
            data.columns = data.columns.get_level_values(0)
            data["Return"] = data["Close"].pct_change()
            data = data.dropna()
            return data, None
