# import streamlit as st
# import yfinance as yf
# import matplotlib.pyplot as plt
# import time
# import matplotlib.pyplot as plt 
# from mpl_finance import candlestick_ohlc 
# import pandas as pd 
# import matplotlib.dates as mpl_dates 
# import numpy as np 
# import datetime 
# import yfinance as yf

# st.title("Real-time Stock Prices")
# # Define the ticker symbol for Apple
# tickerList = ['AAPL']#, 'GOOG']#, 'TSLA', 'AMZN', 'NVDA', 'MSFT']
# rowCount = len(tickerList)/2
# if len(tickerList)%2 != 0:
#     rowCount += 1
# colCount = 2

# figList = []
# axList = []
# plotList = []
# stockDataList = []

# for i in range (0,len(tickerList)):
#     tic = tickerList[i]
#     ticker_symbol = tic
#     st.write(tic)
#     stockData = yf.Ticker(ticker_symbol)
#     # st.write(stockData)
#     # st.write(stockData.history(period='1d', interval='1m'))
#     stockDataList.append(stockData)
#     # st.write(stockData.history())
#     # st.write(int(rowCount), colCount, i+1)
#     fig, ax = plt.subplots()#int(rowCount), colCount, i+1)
#     figList.append(fig)
#     axList.append(ax)
#     plotList.append(st.pyplot(fig))
# # st.write(type(stockDataList[i]))
# historical_pricesList = []
# latest_timeList = []
# latest_price = []
# while True:
#     for i in range (0,len(tickerList)):
#         # st.write(i)
#         # st.write(tickerList[i])
#         # Get the historical prices for Apple stock
#         historical_prices = (yf.Ticker(tickerList[i])).history(period='1d', interval='1m')
#         # st.write(stockDataList[i].history(period='1d', interval='1m'))
        
#         latest_price = historical_prices['Close'].iloc[-1]
#         latest_time = historical_prices.index[-1].strftime('%H:%M:%S')


#         historical_prices.reset_index(inplace=True)
#         historical_prices['Date'] = historical_prices['Datetime']
#         ohlc = historical_prices.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']] 
#         ohlc['Date'] = pd.to_datetime(ohlc['Date']) 
#         ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num) 
#         ohlc = ohlc.astype(float) 

#         candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8) 
        
#         historical_pricesList.append(historical_prices) #2 = google_stock.history(period='1d', interval='1m')
#         # print(historical_prices)
#         # Get the latest price and time
#         # print(historical_prices.head(10))
        
#         ax = axList[i]
#         # Clear the plot and plot the new data
#         ax.clear()

#         ax.set_xlabel('Date') 
#         ax.set_ylabel('Price') 
#         # figList[i].suptitle('Daily Candlestick Chart of NIFTY50') 

#         # Formatting Date 
#         date_format = mpl_dates.DateFormatter('%D-%m-%Y') 
#         ax.xaxis.set_major_formatter(date_format) 
#         figList[i].autofmt_xdate() 

#         # figList[i].tight_layout()

#         # ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
#         # ax.set_xlabel('Time')
#         # ax.set_ylabel('Stock Value')
#         # ax.set_title(tickerList[i] + ' Stock Value')
#         # ax.legend(loc='upper left')
#         # ax.tick_params(axis='x', rotation=45)

#            # Update the plot in the Streamlit app
#         plotList[i].pyplot(figList[i])
#         # plot2.pyplot(fig2)

#         # Show the latest stock value in the app
#         st.write(f"({tickerList[i]})Latest Price ({latest_time}): {latest_price}")

# #         # Sleep for 1 minute before fetching new data
#         time.sleep(10)



###############Interactive Line plot#################

# import streamlit as st
# import yfinance as yf
# import plotly.graph_objs as go
# import time

# st.title("Real-time Stock Prices")

# # Define the ticker symbol for Apple
# tickerList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']

# figList = []
# plotList = []
# stockDataList = []

# for ticker_symbol in tickerList:
#     st.write(ticker_symbol)
#     stockData = yf.Ticker(ticker_symbol)
#     stockDataList.append(stockData)
#     historical_prices = stockData.history(period='1d', interval='1m')

#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=historical_prices.index, y=historical_prices['Close'], mode='lines', name='Stock Value'))
#     fig.update_layout(title=f'{ticker_symbol} Stock Value', xaxis_title='Time', yaxis_title='Stock Value')
#     figList.append(fig)
#     plotList.append(st.plotly_chart(fig))

# while True:
#     for i, ticker_symbol in enumerate(tickerList):
#         historical_prices = stockDataList[i].history(period='1d', interval='1m')

#         latest_price = historical_prices['Close'].iloc[-1]
#         latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

#         fig = figList[i]
#         fig.add_trace(go.Scatter(x=[latest_time], y=[latest_price], mode='markers', name='Latest Price', marker=dict(color='red', size=10)))

#         plotList[i].plotly_chart(fig)

#         st.write(f"({ticker_symbol}) Latest Price ({latest_time}): {latest_price}")

#         time.sleep(10)


###############ORIGINAL#################

# import streamlit as st
# import yfinance as yf
# import matplotlib.pyplot as plt
# import time
# st.title("Real-time Stock Prices")
# # Define the ticker symbol for Apple
# tickerList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
# rowCount = len(tickerList)/2
# if len(tickerList)%2 != 0:
#     rowCount += 1
# colCount = 2

# figList = []
# axList = []
# plotList = []
# stockDataList = []

# for i in range (0,len(tickerList)):
#     tic = tickerList[i]
#     ticker_symbol = tic
#     st.write(tic)
#     stockData = yf.Ticker(ticker_symbol)
#     # st.write(stockData)
#     # st.write(stockData.history(period='1d', interval='1m'))
#     stockDataList.append(stockData)
#     # st.write(stockData.history())
#     # st.write(int(rowCount), colCount, i+1)
#     fig, ax = plt.subplots()#int(rowCount), colCount, i+1)
#     figList.append(fig)
#     axList.append(ax)
#     plotList.append(st.pyplot(fig))
# # st.write(type(stockDataList[i]))
# historical_pricesList = []
# latest_timeList = []
# latest_price = []
# while True:
#     for i in range (0,len(tickerList)):
#         # st.write(i)
#         # st.write(tickerList[i])
#         # Get the historical prices for Apple stock
#         historical_prices = (yf.Ticker(tickerList[i])).history(period='1d', interval='1m')
#         # st.write(stockDataList[i].history(period='1d', interval='1m'))
#         historical_pricesList.append(historical_prices) #2 = google_stock.history(period='1d', interval='1m')
        
#         # Get the latest price and time
#         latest_price = historical_prices['Close'].iloc[-1]
#         latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

        
#         ax = axList[i]
#         # Clear the plot and plot the new data
#         ax.clear()
#         ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
#         ax.set_xlabel('Time')
#         ax.set_ylabel('Stock Value')
#         ax.set_title(tickerList[i] + ' Stock Value')
#         ax.legend(loc='upper left')
#         ax.tick_params(axis='x', rotation=45)

#            # Update the plot in the Streamlit app
#         plotList[i].pyplot(figList[i])
#         # plot2.pyplot(fig2)

#         # Show the latest stock value in the app
#         st.write(f"({tickerList[i]})Latest Price ({latest_time}): {latest_price}")

# #         # Sleep for 1 minute before fetching new data
#         time.sleep(10)


#########Interactive CandleStick##########


# import streamlit as st
# import yfinance as yf
# import plotly.graph_objs as go
# import time

# st.title("Real-time Stock Prices")

# # Define the ticker symbol for Apple
# tickerList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']

# figList = []
# plotList = []
# stockDataList = []

# for ticker_symbol in tickerList:
#     st.write(ticker_symbol)
#     stockData = yf.Ticker(ticker_symbol)
#     stockDataList.append(stockData)
#     historical_prices = stockData.history(period='1d', interval='1m')

#     fig = go.Figure(data=[go.Candlestick(x=historical_prices.index,
#                                           open=historical_prices['Open'],
#                                           high=historical_prices['High'],
#                                           low=historical_prices['Low'],
#                                           close=historical_prices['Close'])])
#     fig.update_layout(title=f'{ticker_symbol} Candlestick Chart', xaxis_title='Time', yaxis_title='Stock Price')
#     figList.append(fig)
#     plotList.append(st.plotly_chart(fig))

# while True:
#     for i, ticker_symbol in enumerate(tickerList):
#         historical_prices = stockDataList[i].history(period='1d', interval='1m')

#         latest_price = historical_prices['Close'].iloc[-1]
#         latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

#         fig = figList[i]
#         fig.add_trace(go.Scatter(x=[latest_time], y=[latest_price], mode='markers', name='Latest Price', marker=dict(color='red', size=10)))

#         plotList[i].plotly_chart(fig)

#         st.write(f"({ticker_symbol}) Latest Price ({latest_time}): {latest_price}")

#         time.sleep(10)




import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import time


# class UniqueNumberGenerator:
#     def __init__(self):
#         self.used_numbers = set()
#         self.generated_numbers = []

#     def get_unique_number(self):
#         for num in range(1001):
#             if num not in self.used_numbers:
#                 self.used_numbers.add(num)
#                 self.generated_numbers.append(num)
#                 return num
#         raise ValueError("No more unique numbers available.")

#     def get_generated_numbers(self):
#         return self.generated_numbers
# gen = UniqueNumberGenerator
                        # import streamlit as st
                        # import yfinance as yf
                        # import plotly.graph_objs as go
                        # import time

                        # def update_chart(selected_time, i):
                        #     if selected_time == '3mo':
                        #         historical_prices = stockDataList[i].history(period='3mo', interval='1d')
                        #     elif selected_time == '6mo':
                        #         historical_prices = stockDataList[i].history(period='6mo', interval='1d')
                        #     elif selected_time == '1y':
                        #         historical_prices = stockDataList[i].history(period='1y', interval='1d')
                        #     elif selected_time == 'max':
                        #         historical_prices = stockDataList[i].history(period='max', interval='1d')

                        #     latest_price = historical_prices['Close'].iloc[-1]
                        #     latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

                        #     fig = figList[i]
                        #     fig.data[0].x = historical_prices.index
                        #     fig.data[0].open = historical_prices['Open']
                        #     fig.data[0].high = historical_prices['High']
                        #     fig.data[0].low = historical_prices['Low']
                        #     fig.data[0].close = historical_prices['Close']

                        #     fig.add_trace(go.Scatter(x=[latest_time], y=[latest_price], mode='markers', name='Latest Price', marker=dict(color='red', size=10)))

                        #     plotList[i].plotly_chart(fig)

                        # st.title("Real-time Stock Prices")

                        # # Define the ticker symbols for various stocks
                        # tickerList = ['AAPL', 'GOOG']#, 'TSLA', 'AMZN', 'NVDA', 'MSFT']
                        # time_options = ['3mo', '6mo', '1y', 'max']

                        # figList = []
                        # plotList = []
                        # stockDataList = []

                        # for ticker_symbol in tickerList:
                        #     st.write(ticker_symbol)
                        #     stockData = yf.Ticker(ticker_symbol)
                        #     stockDataList.append(stockData)
                        #     historical_prices = stockData.history(period='max')

                        #     fig = go.Figure(data=[go.Candlestick(x=historical_prices.index,
                        #                                         open=historical_prices['Open'],
                        #                                         high=historical_prices['High'],
                        #                                         low=historical_prices['Low'],
                        #                                         close=historical_prices['Close'])])
                        #     fig.update_layout(title=f'{ticker_symbol} Candlestick Chart', xaxis_title='Time', yaxis_title='Stock Price')
                        #     figList.append(fig)
                        #     plotList.append(st.plotly_chart(fig))

                        # while True:
                        #     for i, ticker_symbol in enumerate(tickerList):
                        #         selected_time = st.selectbox(f"Select time range for {ticker_symbol}", options=time_options, index=3, key = i)
                        #         update_chart(selected_time, i)

                        #         time.sleep(10)


# import streamlit as st
# import yfinance as yf
# import plotly.graph_objs as go
# import time

# def update_chart(selected_time, i):
#     if selected_time == '3mo':
#         historical_prices = stockDataList[i].history(period='3mo', interval='1d')
#     elif selected_time == '6mo':
#         historical_prices = stockDataList[i].history(period='6mo', interval='1d')
#     elif selected_time == '1y':
#         historical_prices = stockDataList[i].history(period='1y', interval='1d')
#     elif selected_time == 'max':
#         historical_prices = stockDataList[i].history(period='max', interval='1d')

#     latest_price = historical_prices['Close'].iloc[-1]
#     latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

#     fig = figList[i]
#     fig.data[0].x = historical_prices.index
#     fig.data[0].open = historical_prices['Open']
#     fig.data[0].high = historical_prices['High']
#     fig.data[0].low = historical_prices['Low']
#     fig.data[0].close = historical_prices['Close']

#     fig.add_trace(go.Scatter(x=[latest_time], y=[latest_price], mode='markers', name='Latest Price', marker=dict(color='red', size=10)))

#     plotList[i].plotly_chart(fig)

# st.title("Real-time Stock Prices")

# # Define the ticker symbols for various stocks
# tickerList = ['AAPL', 'GOOG']#, 'TSLA', 'AMZN', 'NVDA', 'MSFT']
# time_options = ['3mo', '6mo', '1y', 'max']

# figList = []
# plotList = []
# stockDataList = []

# for ticker_symbol in tickerList:
#     st.write(ticker_symbol)
#     stockData = yf.Ticker(ticker_symbol)
#     stockDataList.append(stockData)
#     historical_prices = stockData.history(period='max')

#     fig = go.Figure(data=[go.Candlestick(x=historical_prices.index,
#                                           open=historical_prices['Open'],
#                                           high=historical_prices['High'],
#                                           low=historical_prices['Low'],
#                                           close=historical_prices['Close'])])
#     fig.update_layout(title=f'{ticker_symbol} Candlestick Chart', xaxis_title='Time', yaxis_title='Stock Price')
#     figList.append(fig)
#     plotList.append(st.plotly_chart(fig))
# class UniqueNumberGenerator:
#     def __init__(self):
#         self.used_numbers = set()
#         self.generated_numbers = []

#     def get_unique_number(self):
#         for num in range(1001):
#             if num not in self.used_numbers:
#                 self.used_numbers.add(num)
#                 self.generated_numbers.append(num)
#                 return num
#         raise ValueError("No more unique numbers available.")

#     def get_generated_numbers(self):
#         return self.generated_numbers
# gen = UniqueNumberGenerator()
# while True:
#     for i, ticker_symbol in enumerate(tickerList):
#         selected_time = st.selectbox(f"Select time range for {ticker_symbol}", options=time_options, index=3, key=gen.get_unique_number())
#         update_chart(selected_time, i)

#         # Show the latest stock price
#         latest_price = stockDataList[i].history(period='1d', interval='1m')['Close'].iloc[-1]
#         latest_time = stockDataList[i].history(period='1d', interval='1m').index[-1].strftime('%H:%M:%S')
#         st.write(f"({ticker_symbol}) Latest Price ({latest_time}): {latest_price}")

#         time.sleep(10)



import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import time

@st.cache
def get_historical_data(ticker_symbol, selected_time):
    stockData = yf.Ticker(ticker_symbol)
    if selected_time == '3mo':
        historical_prices = stockData.history(period='3mo', interval='1d')
    elif selected_time == '6mo':
        historical_prices = stockData.history(period='6mo', interval='1d')
    elif selected_time == '1y':
        historical_prices = stockData.history(period='1y', interval='1d')
    elif selected_time == 'max':
        historical_prices = stockData.history(period='max', interval='1d')
    return historical_prices

def update_chart(selected_time, i):
    historical_prices = get_historical_data(tickerList[i], selected_time)

    latest_price = historical_prices['Close'].iloc[-1]
    latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

    fig = figList[i]
    fig.data[0].x = historical_prices.index
    fig.data[0].open = historical_prices['Open']
    fig.data[0].high = historical_prices['High']
    fig.data[0].low = historical_prices['Low']
    fig.data[0].close = historical_prices['Close']

    fig.add_trace(go.Scatter(x=[latest_time], y=[latest_price], mode='markers', name='Latest Price', marker=dict(color='red', size=10)))

    plotList[i].plotly_chart(fig)

st.title("Real-time Stock Prices")

# Define the ticker symbols for various stocks
tickerList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
time_options = ['3mo', '6mo', '1y', 'max']

figList = []
plotList = []

for ticker_symbol in tickerList:
    st.write(ticker_symbol)
    historical_prices = get_historical_data(ticker_symbol, 'max')

    fig = go.Figure(data=[go.Candlestick(x=historical_prices.index,
                                          open=historical_prices['Open'],
                                          high=historical_prices['High'],
                                          low=historical_prices['Low'],
                                          close=historical_prices['Close'])])
    fig.update_layout(title=f'{ticker_symbol} Candlestick Chart', xaxis_title='Time', yaxis_title='Stock Price')
    figList.append(fig)
    plotList.append(st.plotly_chart(fig))

while True:
    for i, ticker_symbol in enumerate(tickerList):
        selected_time = st.selectbox(f"Select time range for {ticker_symbol}", options=time_options, index=3)
        update_chart(selected_time, i)

        # Show the latest stock price
        latest_price = get_historical_data(ticker_symbol, '1d')['Close'].iloc[-1]
        latest_time = get_historical_data(ticker_symbol, '1d').index[-1].strftime('%H:%M:%S')
        st.write(f"({ticker_symbol}) Latest Price ({latest_time}): {latest_price}")

        time.sleep(10)
