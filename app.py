import streamlit as st
import requests

st.set_page_config(page_title="Weather Dashboard")

st.title("날씨 조회 앱")

API_KEY = st.secrets["OPENWEATHER_KEY"]

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }

    res = requests.get(url, params=params)
    return res

city = st.text_input("도시 입력", value="Seoul")

if st.button("조회"):
    res = get_weather(city)

    if res.status_code != 200:
        st.error("API 호출 실패")
        st.write(res.text)
    else:
        data = res.json()

        st.success(f"{city} 날씨 조회 성공")

        st.metric("온도", f"{data['main']['temp']} °C")
        st.metric("습도", f"{data['main']['humidity']} %")
        st.write("상태:", data["weather"][0]["description"])
