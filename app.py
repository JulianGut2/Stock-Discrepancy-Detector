import streamlit as st
import yfinance as yf
from src.data_loader import fetch_stock_data
from src.disrepancy_detector import detect_zscore, detect_bollinger, detect_volume_spike, detect_iqr, combine_signals
from src.utils import get_anomaly_summary

st.set_page_config(page_title = "Stock Discrepancy Detector", layout = "wide")

