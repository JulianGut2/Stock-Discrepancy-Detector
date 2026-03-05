import streamlit as st
import yfinance as yf
from src.data_loader import fetch_stock_data
from src.disrepancy_detector import detect_zscore, detect_bollinger, detect_volume_spike, detect_iqr, combine_signals
from src.utils import get_anomaly_summary
import plotly.graph_objects as go 

st.set_page_config(page_title = "Stock Discrepancy Detector", layout = "wide")

st.markdown("# Stock Discrepancy Detector")
st.header("Use Sidebar to Input Stock Ticker, Insights Will Generate Automatically.")

with st.sidebar:
    st.header("Stock Input Center")
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
    fig = go.Figure()
    anom_df = df[df["is_anomaly"] == True]

    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close Price"))

    fig.add_trace(go.Scatter(
        x=anom_df.index,
        y=anom_df["Close"],
        mode="markers",
        name = "Anomaly",
        marker = dict(color = "red", size = 8, symbol = "circle")
        ))

    fig.update_layout(height = 700)

    st.plotly_chart(fig, use_container_width = True)
    
    summary = get_anomaly_summary(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Anomalies", summary["total"])
    col2.metric("% Of Days", round(summary["pct"], 2))
    col3.metric("High Severity", summary["high"])

    st.subheader("Anomaly Days")
    st.dataframe(anom_df[["Close", "Return", "z_score", "flag_count"]], use_container_width = True)

    st.download_button(
        label = "Download Anomalies CSV",
        data = anom_df.to_csv(),
        file_name = "anomalies.csv",
        mime = "text/csv"
    )