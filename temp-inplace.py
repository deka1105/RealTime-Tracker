# # import streamlit as st
# # import plotly.graph_objects as go

# # # Initialize the data for the initial traces
# # x1 = [1, 2, 3]
# # y1 = [4, 5, 6]
# # x2 = [1, 2, 3]
# # y2 = [6, 5, 4]

# # # Create initial traces
# # trace1 = go.Scatter(x=x1, y=y1, mode='markers', name='Trace 1')
# # trace2 = go.Scatter(x=x2, y=y2, mode='lines', name='Trace 2')

# # # Create the figure
# # fig = go.Figure()
# # fig.add_trace(trace1)
# # fig.add_trace(trace2)

# # # Display the initial figure using Streamlit
# # st.plotly_chart(fig, use_container_width=True)

# # # User interaction to update the trace
# # new_x1 = st.text_input("Enter new x values for Trace 1 (comma-separated):")
# # new_y1 = st.text_input("Enter new y values for Trace 1 (comma-separated):")

# # # Convert input strings to lists of floats
# # new_x1 = list(map(float, new_x1.split(',')))
# # new_y1 = list(map(float, new_y1.split(',')))

# # # Update trace 1 with new data
# # fig.update_traces(selector=dict(name='Trace 1'), x=new_x1, y=new_y1)

# # # Display the updated figure
# # st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import plotly.graph_objects as go

# # Initialize the data for the initial traces
# x1 = [1, 2, 3]
# y1 = [4, 5, 6]
# x2 = [1, 2, 3]
# y2 = [6, 5, 4]

# # Create initial traces
# trace1 = go.Scatter(x=x1, y=y1, mode='markers', name='Trace 1')
# trace2 = go.Scatter(x=x2, y=y2, mode='lines', name='Trace 2')

# # Create the figure
# fig = go.Figure()
# fig.add_trace(trace1)
# fig.add_trace(trace2)

# # Display the initial figure using Streamlit
# st.plotly_chart(fig, use_container_width=True)

# # User interaction to update the trace
# new_x1 = st.text_input("Enter new x values for Trace 1 (comma-separated):")
# new_y1 = st.text_input("Enter new y values for Trace 1 (comma-separated):")

# # Convert input strings to lists of floats with error handling
# try:
#     new_x1 = list(map(float, new_x1.split(',')))
#     new_y1 = list(map(float, new_y1.split(',')))
# except ValueError:
#     st.warning("Invalid input. Please enter comma-separated numeric values.")
#     new_x1 = []
#     new_y1 = []

# # Update trace 1 with new data if input is valid
# if new_x1 and new_y1:
#     fig.update_traces(selector=dict(name='Trace 1'), x=new_x1, y=new_y1)

# # Display the updated figure
# st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

st.set_page_config(layout="wide")

# Initialize lists to store predefined ranges, lines, and figures
predefined_rangesList = {}
lineList = {}
figList = {}

# Define ticker symbols
ticker_symbolList = ['AAPL', 'GOOG', 'TSLA', 'NVDA', 'MSFT', 'AMZN']

# Create columns for displaying graphs
col1, col2 = st.columns(2)
columnList = [col1, col2]

# Main loop to fetch data and update graphs
while True:
    for i, ticker_symbol in enumerate(ticker_symbolList):
        try:
            # Fetch stock data
            stock_data = yf.download(ticker_symbol)

            # Define predefined time ranges
            if ticker_symbol not in predefined_rangesList:
                predefined_rangesList[ticker_symbol] = {
                    '1 Month': (datetime.now() - timedelta(days=30), datetime.now()),
                    '3 Months': (datetime.now() - timedelta(days=90), datetime.now()),
                    '6 Months': (datetime.now() - timedelta(days=180), datetime.now()),
                    '1 Year': (datetime.now() - timedelta(days=365), datetime.now()),
                    'MAX': (0, 0)
                }
                figList[ticker_symbol] = go.Figure()
                lineList[ticker_symbol] = columnList[i % 2].selectbox("Choose a column:", list(predefined_rangesList[ticker_symbol]), key = i)

            # Fetch stock data based on selected time range
            start_date, end_date = predefined_rangesList[ticker_symbol].get(lineList[ticker_symbol])
            if lineList[ticker_symbol] == 'MAX':
                stock_data = yf.download(ticker_symbol)
            else:
                stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

            # Update the figure with new data
            fig = figList[ticker_symbol]
            fig.update_traces(go.Candlestick(x=stock_data.index,
                                              open=stock_data['Open'],
                                              high=stock_data['High'],
                                              low=stock_data['Low'],
                                              close=stock_data['Close']))
            fig.update_layout(autosize=True, width=800, height=400)

            # Display the updated figure
            columnList[i % 2].plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Failed to fetch or display data for {ticker_symbol}: {e}")

    # Add a delay to avoid excessive API requests
    time.sleep(40)
