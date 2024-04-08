
import yfinance as yf
import plotly.graph_objs as go
import ipywidgets as widgets
from IPython.display import display
from datetime import datetime, timedelta
import plotly.figure_factory as ff

# Define the ticker symbol
ticker_symbol = 'AAPL'
ticker_symbolList = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'NVDA', 'MSFT']
for i in range(0, len(ticker_symbolList)):
    ticker_symbol = ticker_symbolList[i]

    # Fetch the date of the stock's initial public offering (IPO)
    stock_info = yf.Ticker(ticker_symbol)


    # Define predefined time ranges
    predefined_ranges = {
        '1 Month': (datetime.now() - timedelta(days=30), datetime.now()),
        '3 Months': (datetime.now() - timedelta(days=90), datetime.now()),
        '6 Months': (datetime.now() - timedelta(days=180), datetime.now()),
        '1 Year': (datetime.now() - timedelta(days=365), datetime.now()),
        'MAX': (0, 0)
    }

    # Create dropdown widget for selecting predefined time ranges
    range_dropdown = widgets.Dropdown(
        options=list(predefined_ranges.keys()),
        description='Select Range:',
        disabled=False
    )

    # Define update function
    def update_chart(change):
        selected_range = range_dropdown.value
        start_date, end_date = predefined_ranges[selected_range]

        # Fetch historical data
        if(start_date == 0)&(end_date == 0):
            stock_data = yf.download(ticker_symbol)
        else:
            stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

        # Create Candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                        open=stock_data['Open'],
                        high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'])])

        fig.update_layout(
            title='Interactive Candlestick Chart for {}'.format(ticker_symbol),
            xaxis_title='Date',
            yaxis_title='Price',
            xaxis_rangeslider_visible=False
        )

        # fig.show()
        st.plotly_chart(fig, use_container_width=True)

    # Register the update function to be called when dropdown values change
    range_dropdown.observe(update_chart, names='value')

    # Display dropdown menu
    display(range_dropdown)

    # Initialize the chart with default range (1 Month)
    update_chart(None)
