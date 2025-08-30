import FinanceDataReader as fdr 
import streamlit as st
import datetime 

import yfinance as yf
import matplotlib.pyplot as plt

date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.datetime(2025, 8, 27)
)

code = st.text_input(
    '종목코드', 
    value='', 
    placeholder='종목코드를 입력해 주세요'
)

# 날짜 선택시 라인차트가 그려지도록 작성하기. 
# st.line_chart(date)

if code and date : 
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)






