# To turn this app,
# 0. Make a copy (Fork) of this repl with your repl account
# 1. install required packages in Shell:  pip install streamlit yfinance mysql-connector-python plotly
# 2. type  streamlit run streamlit_app.py  within the Shell
# import packages needed
from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

# print title
st.title("CIDM6351 Streamlit Homework 10")
# print plain text
st.write("Taylor Hurt")
st.write("tjhurt1@buffs.wtaum.edu")


# print text in markdown
st.markdown("## **Check Stock Information**")

# a list of stock names
stock_names = ['NVDA', 'AAPL', 'AMZN', 'GOOGL', 'PTON', 'XEL']
# select a stock to check
target_stocks = st.multiselect('Select stocks to check',
                               options=stock_names,
                               default=['XEL', 'PTON', 'NVDA'])

st.markdown("## **Check Stock Price History**")

# start date of the stock infomation, default is the first day of year 2021
start_date = st.date_input('Start Date', datetime(2021, 1, 1))
# end date of the stock infomation, default is date of today
end_date = st.date_input("End Date")

# get today date
today = date.today()
if st.button('Submit'):
  # check valid date
  if start_date > today or end_date > today:
    st.write("## **Please select a valid date period.**")
  else:
    # download the stock data based on stock names, start/end date
    data = pd.DataFrame()
    for stock_name in target_stocks:
      stock_data = yf.download(stock_name, start_date, end_date)
      # only keep the 'High' column
      stock_data = stock_data[['High']]
      stock_data.columns = [stock_name]
      data = pd.concat([data, stock_data], axis=1)

    # show a progress bar
    with st.spinner(text='In progress'):
      fig = px.line(
        data,
        x=data.index,
        y=data.columns,
        title=
        f"High Stock Price: {start_date.strftime('%m/%d/%Y')} to {end_date.strftime('%m/%d/%Y')}",
        labels={
          "value": "Stock Price ($)",
          "variable": "Ticker"
        })
      st.write(fig)
      st.success('Done')
