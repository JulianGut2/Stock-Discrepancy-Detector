import streamlit as st
import yfinance as yf
from src.data_loader import fetch_stock_data
from src.disrepancy_detector import detect_zscore, detect_bollinger, detect_volume_spike, detect_iqr, combine_signals
from src.utils import get_anomaly_summary
import plotly.graph_objects as go 

st.set_page_config(page_title = "Stock Discrepancy Detector", layout = "wide")

with st.sidebar:
    ticker = st.text_input("Stock Value", value = "AAPL")
    period = st.selectbox(label = "Period", options = ["1y", "2y", "5y"])
    run = st.button(label = "Run")

if run:
    df, err = fetch_stock_data(ticker, period)

    if err is not None:
        st.error(err)
        st.stop()

    df = detect_zscore(df)
    df = detect_bollinger(df)
    df = detect_volume_spike(df)
    df = detect_iqr(df)
    df = combine_signals(df)
    st.write(get_anomaly_summary(df))

    fig = go.Figure()
    anom_df = df[df["is_anomaly"] == True]

    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close Price"))

    fig.add_trace(go.Scatter(x=anom_df.index, y=anom_df["Close"], mode="markers"))

    st.plotly_chart(fig, use_container_width = True)