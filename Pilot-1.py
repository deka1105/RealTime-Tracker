import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import time
st.title("Real-time Stock Prices")
# Define the ticker symbol for Apple
tickerList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
rowCount = len(tickerList)/2
if len(tickerList)%2 != 0:
    rowCount += 1
colCount = 2

figList = []
axList = []
plotList = []
stockDataList = []

for i in range (0,len(tickerList)):
    tic = tickerList[i]
    ticker_symbol = tic
    st.write(tic)
    stockData = yf.Ticker(ticker_symbol)
    # st.write(stockData)
    # st.write(stockData.history(period='1d', interval='1m'))
    stockDataList.append(stockData)
    # st.write(stockData.history())
    # st.write(int(rowCount), colCount, i+1)
    fig, ax = plt.subplots()#int(rowCount), colCount, i+1)
    figList.append(fig)
    axList.append(ax)
    plotList.append(st.pyplot(fig))
# st.write(type(stockDataList[i]))
historical_pricesList = []
latest_timeList = []
latest_price = []
while True:
    for i in range (0,len(tickerList)):
        # st.write(i)
        # st.write(tickerList[i])
        # Get the historical prices for Apple stock
        historical_prices = (yf.Ticker(tickerList[i])).history(period='1d', interval='1m')
        # st.write(stockDataList[i].history(period='1d', interval='1m'))
        historical_pricesList.append(historical_prices) #2 = google_stock.history(period='1d', interval='1m')
        
        # Get the latest price and time
        latest_price = historical_prices['Close'].iloc[-1]
        latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

        
        ax = axList[i]
        # Clear the plot and plot the new data
        ax.clear()
        ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
        ax.set_xlabel('Time')
        ax.set_ylabel('Stock Value')
        ax.set_title(tickerList[i] + ' Stock Value')
        ax.legend(loc='upper left')
        ax.tick_params(axis='x', rotation=45)

           # Update the plot in the Streamlit app
        plotList[i].pyplot(figList[i])
        # plot2.pyplot(fig2)

        # Show the latest stock value in the app
        st.write(f"({tickerList[i]})Latest Price ({latest_time}): {latest_price}")

#         # Sleep for 1 minute before fetching new data
        time.sleep(10)
