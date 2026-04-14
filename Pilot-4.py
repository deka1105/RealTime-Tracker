import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import time
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
from datetime import datetime, timedelta
import plotly.figure_factory as ff
# st.write('#')
st.set_page_config(layout="wide",)
predefined_rangesList = []
lineList = []
figList = []

# st.write(len(figList))
# st.title("Plotly Graphs with containers")
col1, col2 = st.columns([0.5, 0.5])
columnList = [col1, col2]
# myExpander = st.expander()

ticker_symbolList = ['AAPL', 'GOOG']#, 'TSLA', 'NVDA', 'MSFT', 'AMZN']
while True:
    stop = 0
    # def rerun():
    for i in range (0, len(ticker_symbolList)):

                ticker_symbol = ticker_symbolList[i]
                print(ticker_symbol)
                # Fetch the date of the stock's initial public offering (IPO)
                stock_info = yf.Ticker(ticker_symbol)

                # Define predefined time ranges
                if len(predefined_rangesList) != len(ticker_symbolList):
                    predefined_rangesList.append({
                        ticker_symbol+' 1 Month': (datetime.now() - timedelta(days=30), datetime.now()),
                        ticker_symbol+' 3 Months': (datetime.now() - timedelta(days=90), datetime.now()),
                        ticker_symbol+' 6 Months': (datetime.now() - timedelta(days=180), datetime.now()),
                        ticker_symbol+' 1 Year': (datetime.now() - timedelta(days=365), datetime.now())
                        ,ticker_symbol+' MAX': (0, 0)
                    })    
                    figList.append(go.Figure())
                    lineList.append(columnList[i%2].selectbox("Choose a column:", list(predefined_rangesList[i].keys())))
                    # print(len(figList))

                if lineList[i] == ticker_symbol+' MAX':
                    stock_data = yf.download(ticker_symbol)
                else:
                    start_date, end_date = predefined_rangesList[i].get(lineList[i])
                    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
                if stop == 0:
                    figList[i].add_trace(go.Candlestick(x=stock_data.index,
                                        open=stock_data['Open'],
                                        high=stock_data['High'],
                                        low=stock_data['Low'],
                                        close=stock_data['Close']))
                    figList[i].update_layout(autosize=True,width=800,height=400)
                    # st.write(type(figList[i]) 
                    # st.plotly_chart(figList[i], use_container_width=True)
                    figList[i].update_layout(autosize=True)
                    columnList[i%2].plotly_chart(figList[i], use_container_width=True)
                else:
                    figList[i].update_traces(go.Candlestick(x=stock_data.index,
                                        open=stock_data['Open'],
                                        high=stock_data['High'],
                                        low=stock_data['Low'],
                                        close=stock_data['Close']))
                    figList[i].update_layout(autosize=True,width=800,height=400)
                    # st.write(type(figList[i]) 
                    # st.plotly_chart(figList[i], use_container_width=True)
                    figList[i].update_layout(autosize=True)
                    columnList[i%2].plotly_chart(figList[i], use_container_width=True)
                if len(figList) == len(ticker_symbolList):
                     stop = 1
                time.sleep(20)
        # rerun()

