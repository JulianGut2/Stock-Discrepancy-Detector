from src.data_loader import fetch_stock_data
from src.disrepancy_detector import detect_zscore, detect_bollinger, detect_volume_spike, detect_iqr, combine_signals
from src.utils import get_anomaly_summary

df, err = fetch_stock_data("AAPL")
df = detect_zscore(df)
df = detect_bollinger(df)
df = detect_volume_spike(df)
df = detect_iqr(df)
df = combine_signals(df)

print(get_anomaly_summary(df))