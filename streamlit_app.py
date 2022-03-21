import streamlit as st
import pandas as pd

df = pd.read_csv("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2021_LoL_esports_match_data_from_OraclesElixir_20220321.csv")

st.title("I'm a test app")

st.header("hear me roar")

list1 = st.multiselect("leagues", df.league.unique())

slider1 = st.slider("rows", min_value=0, max_value=100)

button1 = st.button("fire the data cannon")

if button1:
  st.write("2021 data", df[df.league.isin(list1)].head(slider1))
