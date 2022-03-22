import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.experimental_singleton
def get_data(url):
  return pd.read_csv(url)

df = get_data("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2015_LoL_esports_match_data_from_OraclesElixir_20220322.csv")

st.title("I'm a test app")

st.header("hear me roar")

st.dataframe(df)

list1 = st.sidebar.multiselect("leagues", df.league.unique())
list2 = st.sidebar.multiselect("positions", df.position.unique())

if list1 == []:
  list1 = df.league.unique()

if list2 == []:
  list2 = df.position.unique()
  
fig, ax = plt.subplots()
ax = sns.violinplot(data=df[(df.league.isin(list1)) & (df.position.isin(list2))], y = "position", x = "kills")
st.pyplot(fig)

with st.expander("player stats"):
  player = st.selectbox("player", df[(df.league.isin(list1)) & (df.position.isin(list2))].playername.unique())
  p_df = df[df.playername == player]
  st.write(f"Most played champion: {p_df.champion.mode()[0]}")
  
