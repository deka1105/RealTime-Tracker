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

# ticker_symbol1 = 'AAPL'
# ticker_symbol2 = 'GOOG'
# # Get the data of the stock
# apple_stock = yf.Ticker(ticker_symbol1)
# st.write(apple_stock.history())
# google_stock = yf.Ticker(ticker_symbol2)
# # Create a matplotlib figure
# fig, ax = plt.subplots()
# fig2, ax2 = plt.subplots()

# # Use st.pyplot to display the plot
# plot = st.pyplot(fig)
# plot2 = st.pyplot(fig2)
# # Loop to fetch and update stock values
# while True:
#     # Get the historical prices for Apple stock
#     # st.write(type(apple_stock))
#     historical_prices = apple_stock.history(period='1d', interval='1m')
#     historical_prices2 = google_stock.history(period='1d', interval='1m')
#     # st.write(historical_prices)
#     # Get the latest price and time
#     latest_price = historical_prices['Close'].iloc[-1]
#     latest_time = historical_prices.index[-1].strftime('%H:%M:%S')

#     # Clear the plot and plot the new data
#     ax.clear()
#     ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
#     ax.set_xlabel('Time')
#     ax.set_ylabel('Stock Value')
#     ax.set_title('Apple Stock Value')
#     ax.legend(loc='upper left')
#     ax.tick_params(axis='x', rotation=45)

#     latest_price2 = historical_prices2['Close'].iloc[-1]
#     latest_time2 = historical_prices2.index[-1].strftime('%H:%M:%S')

#     # Clear the plot and plot the new data
#     ax2.clear()
#     ax2.plot(historical_prices2.index, historical_prices2['Close'], label='Stock Value')
#     ax2.set_xlabel('Time')
#     ax2.set_ylabel('Stock Value')
#     ax2.set_title('Google Stock Value')
#     ax2.legend(loc='upper left')
#     ax2.tick_params(axis='x', rotation=45)

#     # Update the plot in the Streamlit app
#     plot.pyplot(fig)
#     plot2.pyplot(fig2)

#     # Show the latest stock value in the app
#     st.write(f"Latest Price ({latest_time}): {latest_price}")

#     # Sleep for 1 minute before fetching new data
#     time.sleep(10)

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import numpy as np

# st.title("Plotly Graphs with containers")

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

# plot_spot = st.empty()  # holding the spot for the graph

# # make the widgets that will change the graph
# line = st.selectbox("Choose a column:", chart_data.columns)

# title = st.radio("Decide to include a title:", ["Yes", "No"])

# # Dropdown for selecting number of rows
# num_rows = st.selectbox("Select number of rows:", ["First 5", "First 10", "All"])

# # Filter data based on the selected number of rows
# if num_rows == "First 5":
#     filtered_data = chart_data.head(5)
# elif num_rows == "First 10":
#     filtered_data = chart_data.head(10)
# else:
#     filtered_data = chart_data

# # now code the plotly chart based on the widget selection
# fig = px.line(filtered_data, x=filtered_data.index, y=line)

# if title == "Yes":
#     fig.update_layout(title="My graph title")

# # send the plotly chart to its spot "in the line"
# with plot_spot:
#     st.plotly_chart(fig)



# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
# ----------------------------------------------------------------------------BOF
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
#----------- Pilot 3 BOCode
    # chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    # plot_spot = st.empty() 
    # line = (st.selectbox("Choose a column:", chart_data.columns))
    # fig = px.line(chart_data, x=chart_data.index, y=line)
    # with plot_spot:
    #     st.plotly_chart(fig)
#----------- Pilot 3 EOCode


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
    # Create dropdown widget for selecting predefined time ranges
    # range_dropdown = widgets.Dropdown(
    #     options=list(predefined_rangesList[i].keys()),
    #     description='Select Range:',
    #     disabled=False
    # )

    if lineList[i] == ticker_symbol+' MAX':
        stock_data = yf.download(ticker_symbol)
    else:
        start_date, end_date = predefined_rangesList[i].get(lineList[i])
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # if lineList[i] == ticker_symbol+' 1 Month':
    #     start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 1 Month')
    #     stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    # elif lineList[i] == ticker_symbol+' 3 Month':
    #     start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 3 Month')
    #     stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    # elif lineList[i] == ticker_symbol+' 6 Month':
    #     start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 6 Month')
    #     stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    # elif lineList[i] == ticker_symbol+' 1 Year':
    #     start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' 1 Year')
    #     stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    # elif lineList[i] == ticker_symbol+' MAX':
    #     start_date, end_date = predefined_rangesList[i].get(ticker_symbol+' MAX')
    #     stock_data = yf.download(ticker_symbol)#, start=start_date, end=end_date)

    figList.append(go.Figure(data=[go.Candlestick(x=stock_data.index,
                        open=stock_data['Open'],
                        high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'])]))

    # fig.update_layout(
    #     title='Interactive Candlestick Chart for {}'.format(ticker_symbol),
    #     xaxis_title='Date',
    #     yaxis_title='Price',
    #     xaxis_rangeslider_visible=False
    # )
    # with plot_spot:
    st.plotly_chart(figList[i], use_container_width=True)

    # # ---Temp Comment till EOL

    # # Define update function
    # def update_chart(change):
    #     selected_range = range_dropdown.value
    #     start_date, end_date = predefined_rangesList[i][selected_range]

    #     # Fetch historical data
    #     if(start_date == 0)&(end_date == 0):
    #         stock_data = yf.download(ticker_symbol)
    #     else:
    #         stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    #     # Create Candlestick chart
    #     fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
    #                     open=stock_data['Open'],
    #                     high=stock_data['High'],
    #                     low=stock_data['Low'],
    #                     close=stock_data['Close'])])

    #     fig.update_layout(
    #         title='Interactive Candlestick Chart for {}'.format(ticker_symbol),
    #         xaxis_title='Date',
    #         yaxis_title='Price',
    #         xaxis_rangeslider_visible=False
    #     )

    #     # fig.show()
    #     st.plotly_chart(fig, use_container_width=True)

    # # Register the update function to be called when dropdown values change
    # range_dropdown.observe(update_chart, names='value')

    # # Display dropdown menu
    # display(range_dropdown)

    # # Initialize the chart with default range (1 Month)
    # update_chart(None)
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF
# ----------------------------------------------------------------------------EOF

# import yfinance as yf
# import plotly.graph_objs as go
# import ipywidgets as widgets
# from IPython.display import display
# from datetime import datetime, timedelta
# import plotly.figure_factory as ff

# # Define the ticker symbol
# ticker_symbol = 'AAPL'
# ticker_symbolList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
# for i in range(0, len(ticker_symbolList)):
#     ticker_symbol = ticker_symbolList[i]

#     # Fetch the date of the stock's initial public offering (IPO)
#     stock_info = yf.Ticker(ticker_symbol)


#     # Define predefined time ranges
#     predefined_ranges = {
#         '1 Month': (datetime.now() - timedelta(days=30), datetime.now()),
#         '3 Months': (datetime.now() - timedelta(days=90), datetime.now()),
#         '6 Months': (datetime.now() - timedelta(days=180), datetime.now()),
#         '1 Year': (datetime.now() - timedelta(days=365), datetime.now()),
#         'MAX': (0, 0)
#     }

#     # Create dropdown widget for selecting predefined time ranges
#     range_dropdown = widgets.Dropdown(
#         options=list(predefined_ranges.keys()),
#         description='Select Range:',
#         disabled=False
#     )

#     # Define update function
#     def update_chart(change):
#         selected_range = range_dropdown.value
#         start_date, end_date = predefined_ranges[selected_range]

#         # Fetch historical data
#         if(start_date == 0)&(end_date == 0):
#             stock_data = yf.download(ticker_symbol)
#         else:
#             stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

#         # Create Candlestick chart
#         fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
#                         open=stock_data['Open'],
#                         high=stock_data['High'],
#                         low=stock_data['Low'],
#                         close=stock_data['Close'])])

#         fig.update_layout(
#             title='Interactive Candlestick Chart for {}'.format(ticker_symbol),
#             xaxis_title='Date',
#             yaxis_title='Price',
#             xaxis_rangeslider_visible=False
#         )

#         # fig.show()
#         st.plotly_chart(fig, use_container_width=True)

#     # Register the update function to be called when dropdown values change
#     range_dropdown.observe(update_chart, names='value')

#     # Display dropdown menu
#     display(range_dropdown)

#     # Initialize the chart with default range (1 Month)
#     update_chart(None)
