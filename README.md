---
title: Stock Discrepancy Detector
emoji: 📈
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Stock Discrepancy Detector

This project serves as a way to explore statistical anomalies within specified stock tickers. 
It utilizes streamlit to deliver brief, but actionable data along with common statistical methods such as 
standard deviations, rolling means, and Z-scores. All data is live and pulled using the yfinance library.

## Detection Methods

### Z-Score
Using Z-Score I was able to detect when a specific number was out of the standard bounds of the data,
marking an anomaly, specifically focusing on the daily return percentage.

### Bollinger Bands
Researching and utilizing Bollinger Bands I was able to measure market volatility and mark an anomaly when
a specific closing amount was out of the standard bounds of the data.

### IQR
Calculating the IQR was essential in creating another anomaly point as I was able to find the central
portion of the dataset which was essential to understanding what was out of the normal bands. Finding Q1/Q3
helped deafen outliers in the dataset.

### Volume Spike
Volume spikes lastly helped me understand when a value was vastly different from its peers which marks
an anomaly in the data, specifically using a 20 day rolling average to compare each days volume.

## How to run

1. Clone the repo
```bash
git clone https://github.com/JulianGut2/Stock-Discrepancy-Detector.git
cd Stock-Discrepancy-Detector
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run .\app.py
```

## Disclaimer:
This project is for educational and portfolio purposes. It is not financial advice and shoud not be used to make investment decisions.