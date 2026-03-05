import numpy as np
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


def detect_volume_spike(df, threshhold = 2.5):
    average_vol = df["Volume"].rolling(20).mean()
    df["volume_anomaly"] = df["Volume"] > (threshhold * average_vol)
    return df