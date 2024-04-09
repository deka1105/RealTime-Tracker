import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import ipywidgets as widgets
from IPython.display import display
from datetime import datetime, timedelta
import plotly.figure_factory as ff

predefined_rangesList = []


st.title("Plotly Graphs with containers")
lineList = []
figList = []
ticker_symbolList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
for i in range (0, len(ticker_symbolList)):

    ticker_symbol = ticker_symbolList[i]

    # Fetch the date of the stock's initial public offering (IPO)
    stock_info = yf.Ticker(ticker_symbol)


    # Define predefined time ranges
    predefined_rangesList.append({
        ticker_symbol+' 1 Month': (datetime.now() - timedelta(days=30), datetime.now()),
        ticker_symbol+' 3 Months': (datetime.now() - timedelta(days=90), datetime.now()),
        ticker_symbol+' 6 Months': (datetime.now() - timedelta(days=180), datetime.now()),
        ticker_symbol+' 1 Year': (datetime.now() - timedelta(days=365), datetime.now())
        ,ticker_symbol+' MAX': (0, 0)
    })
    lineList.append(st.selectbox("Choose a column:", list(predefined_rangesList[i].keys())))


    if lineList[i] == ticker_symbol+' 1 Month':
        start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 1 Month')
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    elif lineList[i] == ticker_symbol+' 3 Month':
        start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 3 Month')
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    elif lineList[i] == ticker_symbol+' 6 Month':
        start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 6 Month')
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    elif lineList[i] == ticker_symbol+' 1 Year':
        start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 1 Year')
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    elif lineList[i] == ticker_symbol+' MAX':
        start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' MAX')
        stock_data = yf.download(ticker_symbol)#, start=start_date, end=end_date)

    figList.append(go.Figure(data=[go.Candlestick(x=stock_data.index,
                        open=stock_data['Open'],
                        high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'])]))

    st.plotly_chart(figList[i], use_container_width=True)