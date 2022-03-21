import streamlit as st
import pandas as pd

df = pd.read_csv("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2021_LoL_esports_match_data_from_OraclesElixir_20220321.csv")

st.title("I'm a test app")

st.header("hear me roar")

button1 = st.button("fire the data cannon")

slider1 = st.slider("rows", min_value=0, max_value=100)

if button1:
  st.write("2021 data", df.head(slider1))
