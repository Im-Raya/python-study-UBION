import FinanceDataReader as fdr 
import streamlit as st
import datetime 

st.title('종목 차트 검색')

with st.sidebar: 
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
    
    tab1, tab2 = st.tabs(['차트', '데아터'])
    
    with tab1:
        st.line_chart(data)
    with tab2:
        st.dataframe(df.sort_index(ascending=False))
    with st.expander('컬럼 설명') : 
        st.markdown('''
                    - OPEN: 시가
                    - High: 고가
                    - Low: 저각
                    - Close: 종가
                    - Adj Close: 수정 종가
                    - Volumn: 거래량 ''' 
                    )


