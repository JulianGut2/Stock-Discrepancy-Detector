import yfinance as yf

data = yf.download("AAPL", period = "5y", auto_adjust = True, progress = False)

print(f"{data.columns} \n\n {data.shape}")