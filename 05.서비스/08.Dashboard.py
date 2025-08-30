import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
import pandas as pd


import os
import matplotlib.font_manager as fm #폰트 관련 용도 as fm 

# list로 받은 데이터의 중복을 제거
def unique(list):
    x = np.array(list)
    return np.unique(x)
# 현재 폴더 안의 customFonts 폴더에서 폰트 파일을 찾아 matplotlib에 등록을 함
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    # 지정된 경로에 있는 모든 폰트 파일 검색
    font_files = fm.findSystemFonts(fontpaths=font_dirs)  # .ttf, .otf
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    # 폰트 매니저를 새로 로드, 캐시를 사용하지 않고 바로 커스텀 폰트 반영
    fm._load_fontmanager(try_read_cache=False)
fontRegistered()
fontNames = [f.name for f in fm.fontManager.ttflist]
default_font = "Malgun Gothic"
fontname = st.selectbox(
    "폰트 선택",
    unique(fontNames),
    index = unique(fontNames).tolist().index(default_font) if default_font in unique(fontNames) else 0
)
# rc : runtime configuration / 설정값들이 모든 그래프에 적용
plt.rc('font', family=fontname)


st.set_page_config(page_title="💻 데이터 분석 대시보드", layout="wide")

#사이드바 
st.sidebar.title("⚙️설정")
menu = st.sidebar.radio("메뉴 선택", ["홈", "데이터 업로드", "EDA분석", "시각화"])

if menu == "홈":
    st.title(":막대_차트: Streamlit 데이터 분석 대시보드")
    st.markdown("""
    이 앱은 Streamlit을 활용해 만든 미니 분석 도구입니다.
    - CSV 파일 업로드
    - 기초 통계량 확인
    - 시각화 그래프 선택
    """)
elif menu == "데이터 업로드": 
    st.header("📂 CSV 파일 업로드")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])
    
    if uploaded_file is not None: 
        df = pd.read_csv(uploaded_file, encoding='cp949')
        st.success("파일 업로드 성공 ✅")
        st.write("데이터 미리보기")
        st.dataframe(df.head())
        
        #세션에 저장
        st.session_state["df"]=df 
elif menu == "EDA분석":
    st.header("🔍 데이터 EDA")
    
    if "df" not in st.session_state:
        st.warning("먼저 CSV파일을 업로드해주세요.")
    else: 
        df = st.session_state['df']
        
        st.subheader("데이터 기본 정보")
        st.write("행/열 크기:", df.shape)
        st.write("컬럼명:", list(df.columns))
                
        st.subheader("📊기초 통계량")
        st.write(df.describe())
        
        st.subheader("📈 결측치 확인")
        st.bar_chart(df.isnull().sum())
        
elif menu == '시각화': 
    st.header("🎨 데이터 시각화")
    
    if "df" not in st.session_state:
        st.warning("먼저 CSV파일을 업로드해주세요.")
    else: 
        df = st.session_state['df']
        # 수치형 컬럼만 선택
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        if not num_cols:
            st.error("수치형 데이터가 없습니다.")
        else:
            x_col = st.selectbox("X축 선택", num_cols)
            y_col = st.selectbox("Y축 선택", num_cols)
            plot_type = st.radio("그래프 종류 선택", ["산점도", "히스토그램", "박스플롯"])
            fig, ax = plt.subplots(figsize=(8, 5))
            if plot_type == "산점도":
                sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
            elif plot_type == "히스토그램":
                sns.histplot(df[x_col], kde=True, ax=ax)
            elif plot_type == "박스플롯":
                sns.boxplot(x=df[x_col], ax=ax)
            st.pyplot(fig),
            