import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st


def MACD(df, window_slow, window_fast, window_signal):
    macd = pd.DataFrame()
    macd['ema_slow'] = df['Close'].ewm(span=window_slow).mean()
    macd['ema_fast'] = df['Close'].ewm(span=window_fast).mean()
    macd['macd'] = macd['ema_slow'] - macd['ema_fast']
    macd['signal'] = macd['macd'].ewm(span=window_signal).mean()
    macd['diff'] = macd['macd'] - macd['signal']
    macd['bar_positive'] = macd['diff'].clip(lower=0)
    macd['bar_negative'] = macd['diff'].clip(upper=0)
    return macd

def Stochastic(df, window, smooth_window):
    stochastic = pd.DataFrame()
    stochastic['%K'] = ((df['Close'] - df['Low'].rolling(window).min()) /
                        (df['High'].rolling(window).max() - df['Low'].rolling(window).min())) * 100
    stochastic['%D'] = stochastic['%K'].rolling(smooth_window).mean()
    stochastic['%SD'] = stochastic['%D'].rolling(smooth_window).mean()
    stochastic['UL'] = 80
    stochastic['DL'] = 20
    return stochastic

symbol = 'AAPL'
# df = yf.download(symbol, period='6mo')
df = (yf.Ticker(symbol)).history(period='1mo', interval='1h')
macd = MACD(df, 12, 26, 9)
stochastic = Stochastic(df, 14, 3)

# Candlestick chart
fig_candlestick = go.Figure(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'], name='Candlestick'))

fig_candlestick.update_layout(title='Interactive Candlestick Chart')
fig_candlestick.update_layout(xaxis_rangeslider_visible=False)

# MACD plot
fig_macd = go.Figure()

fig_macd.add_trace(go.Scatter(x=macd.index, y=macd['macd'], mode='lines', name='MACD'))
fig_macd.add_trace(go.Scatter(x=macd.index, y=macd['signal'], mode='lines', name='Signal'))
fig_macd.add_trace(go.Bar(x=macd.index, y=macd['bar_positive'], name='MACD Positive', marker_color='green'))
fig_macd.add_trace(go.Bar(x=macd.index, y=macd['bar_negative'], name='MACD Negative', marker_color='red'))

fig_macd.update_layout(title='MACD Indicators')

# Stochastic plot
fig_stochastic = go.Figure()

fig_stochastic.add_trace(go.Scatter(x=stochastic.index, y=stochastic['%D'], mode='lines', name='%D'))
fig_stochastic.add_trace(go.Scatter(x=stochastic.index, y=stochastic['%SD'], mode='lines', name='%SD'))
fig_stochastic.add_trace(go.Scatter(x=stochastic.index, y=stochastic['UL'], mode='lines', name='Upper Limit', line=dict(color='blue', dash='dash')))
fig_stochastic.add_trace(go.Scatter(x=stochastic.index, y=stochastic['DL'], mode='lines', name='Lower Limit', line=dict(color='orange', dash='dash')))

fig_stochastic.update_layout(title='Stochastic Indicators')

# Checkbox for selecting graphs to display
display_candlestick = st.checkbox("Candlestick Chart", key = 1)
display_macd = st.checkbox("MACD Plot", key = 2)
display_stochastic = st.checkbox("Stochastic Plot", key = 3)

# Show selected plots
if display_candlestick:
    st.plotly_chart(fig_candlestick)

if display_macd:
    st.plotly_chart(fig_macd)

if display_stochastic:
    st.plotly_chart(fig_stochastic)


symbol = 'AMZN'
# df = yf.download(symbol, period='6mo')
df = (yf.Ticker(symbol)).history(period='1mo', interval='1h')
macd = MACD(df, 12, 26, 9)
stochastic = Stochastic(df, 14, 3)

# Candlestick chart
fig_candlestick1 = go.Figure(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'], name='Candlestick'))

fig_candlestick1.update_layout(title='Interactive Candlestick Chart')
fig_candlestick1.update_layout(xaxis_rangeslider_visible=False)

# MACD plot
fig_macd1 = go.Figure()

fig_macd1.add_trace(go.Scatter(x=macd.index, y=macd['macd'], mode='lines', name='MACD'))
fig_macd1.add_trace(go.Scatter(x=macd.index, y=macd['signal'], mode='lines', name='Signal'))
fig_macd1.add_trace(go.Bar(x=macd.index, y=macd['bar_positive'], name='MACD Positive', marker_color='green'))
fig_macd1.add_trace(go.Bar(x=macd.index, y=macd['bar_negative'], name='MACD Negative', marker_color='red'))

fig_macd1.update_layout(title='MACD Indicators')

# Stochastic plot
fig_stochastic1 = go.Figure()

fig_stochastic1.add_trace(go.Scatter(x=stochastic.index, y=stochastic['%D'], mode='lines', name='%D'))
fig_stochastic1.add_trace(go.Scatter(x=stochastic.index, y=stochastic['%SD'], mode='lines', name='%SD'))
fig_stochastic1.add_trace(go.Scatter(x=stochastic.index, y=stochastic['UL'], mode='lines', name='Upper Limit', line=dict(color='blue', dash='dash')))
fig_stochastic1.add_trace(go.Scatter(x=stochastic.index, y=stochastic['DL'], mode='lines', name='Lower Limit', line=dict(color='orange', dash='dash')))

fig_stochastic1.update_layout(title='Stochastic Indicators')

# Checkbox for selecting graphs to display
display_candlestick1 = st.checkbox("Candlestick Chart", key = 4)
display_macd1 = st.checkbox("MACD Plot", key = 5)
display_stochastic1 = st.checkbox("Stochastic Plot", key = 6)

# Show selected plots
if display_candlestick1:
    st.plotly_chart(fig_candlestick1)

if display_macd1:
    st.plotly_chart(fig_macd)

if display_stochastic1:
    st.plotly_chart(fig_stochastic)
