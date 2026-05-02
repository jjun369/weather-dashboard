# app.py
import streamlit as st
from api_client import get_coordinates, get_weather
from utils import weather_to_df

st.title("날씨 조회 툴 (REST API + Streamlit)")

city = st.text_input("도시 입력 (예: Seoul, Tokyo, New York)")

if st.button("조회"):

    coords = get_coordinates(city)

    if not coords:
        st.error("도시를 찾을 수 없음")
        st.stop()

    lat, lon = coords

    weather_json = get_weather(lat, lon)
    df = weather_to_df(weather_json)

    st.subheader(f"{city} 시간별 온도")
    st.dataframe(df)

    st.subheader("그래프")
    st.line_chart(df.set_index("time"))

    # 🔍 검색 기능 (핵심)
    keyword = st.text_input("특정 시간 검색 (예: 2025-04-26 12:00)")

    if keyword:
        filtered = df[df["time"].str.contains(keyword)]
        st.write("검색 결과")
        st.dataframe(filtered)