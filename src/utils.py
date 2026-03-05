import pandas as pd

def get_anomaly_summary(df):
    anomaly_df = df[df["is_anomaly"] == True]

    final = {
        "total"         : len(anomaly_df),
        "pct"           : ((len(anomaly_df) / len(df)) * 100),
        "high"          : len(df[df["flag_count"] >= 3]),
        "worst_return"  : df["Return"].min(),
        "best_return"   : df["Return"].max()
    }

    return final