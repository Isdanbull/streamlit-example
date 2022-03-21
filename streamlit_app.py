import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2021_LoL_esports_match_data_from_OraclesElixir_20220321.csv")

st.title("I'm a test app")

st.header("hear me roar")

list1 = st.sidebar.multiselect("leagues", df.league.unique())
list2 = st.sidebar.multiselect("positions", df.position.unique())

slider1 = st.sidebar.slider("rows", min_value=0, max_value=100)

button1 = st.sidebar.button("fire the data cannon")

if button1:
  st.dataframe(df[df.league.isin(list1)].head(slider1))
  
fig, ax = plt.subplots()
ax = sns.violinplot(data=df[(df.league.isin(list1)) & (df.position.isin(list2))], x = "position", y = "kills)
st.pyplot(fig)
