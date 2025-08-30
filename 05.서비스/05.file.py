import streamlit as st
import pandas as pd
import time 

#파일 업로드 버튼 (업로드 기능)
file = st.file_uploader("파일 선택(csv or excel)", type = ['csv', 'xls','xlsx'])
time.sleep(3)

if file is not None :
    ext = file.name.split('.')[-1]
    if ext == 'csv' : 
        #파일 읽기 
        df = pd.read_csv(file)
        st.dataframe(df)
    elif 'xis' in ext:
        df = pd.read_excel(file, engine='openpyxl')
        st.dataframe(df)
    else: 
        st.write("지원하지 않는 파일 형식입니다.")
        