import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

@st.experimental_singleton
def get_data(url):
  return pd.read_csv(url)

@st.experimental_singleton
def score_f(row):
    if row.position == 'team':
        if (row.result == 1) and (row.gamelength < 1800):
            return row.towers + 1.5*row.elementaldrakes + 2*row.elders + 2*row.barons + 2*row.firsttower +3 #fast win bonus 
        else:
            return row.towers + 1.5*row.elementaldrakes + 2*row.elders + 2*row.barons + 2*row.firsttower
    else:    #scores for players
        return (3*row.kills) + (2*row.assists) + (0.02*row['total cs']) + (2*row.firstbloodkill) + (2*(row.triplekills-row.quadrakills)) + (4*(row.quadrakills-row.pentakills)) + (7*row.pentakills) - row.deaths

@st.experimental_singleton
def score_a(df):
  df['score'] = df.apply(lambda row: score_f(row), axis=1)
  return df

@st.experimental_singleton
def date_f(df):
  df['date'] = pd.to_datetime(df.date).dt.date
  return df

df = get_data("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2015_LoL_esports_match_data_from_OraclesElixir_20220322.csv")
df = score_a(df)
df = date_f(df)

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
  fig, ax = plt.subplots()
  ax = sns.lineplot(data=p_df, x='date', y='score')
  st.pyplot(fig)
  
