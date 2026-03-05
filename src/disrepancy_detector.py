import pandas as pd
from scipy import stats


def detect_zscore(df, threshold = 2.5):

    df["z_score"] = stats.zscore(df["Return"])
    df["zscore_anomaly"] = abs(df["z_score"]) > threshold
    return df


def detect_bollinger(df, window = 20, n_std = 2.0):

    rolling_std = df["Close"].rolling(window).std()
    rolling_mean = df["Close"].rolling(window).mean()

    df["BB_upper"] = rolling_mean + (rolling_std * n_std)
    df["BB_lower"] = rolling_mean - (rolling_std * n_std)
    df["bb_anomaly"] = (df["Close"] > df["BB_upper"]) | (df["Close"] < df["BB_lower"])
    return df


def detect_volume_spike(df, threshold = 2.5):
    average_vol = df["Volume"].rolling(20).mean()
    df["volume_anomaly"] = df["Volume"] > (threshold * average_vol)
    return df


def detect_iqr(df):
    q1 = df["Return"].quantile(0.25)
    q3 = df["Return"].quantile(0.75)
    iqr = q3-q1

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    df["iqr_anomaly"] = (df["Return"] > upper_fence) | (df["Return"] < lower_fence)
    return df


def combine_signals(df):
    df["flag_count"] = df[["zscore_anomaly", "bb_anomaly", "volume_anomaly", "iqr_anomaly"]].sum(axis = 1)
    df["is_anomaly"] = df["flag_count"] >= 1
    return df