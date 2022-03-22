import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt



def score_f(row):
    if row.position == 'team':
        if (row.result == 1) and (row.gamelength < 1800):
            return row.towers + 1.5*row.elementaldrakes + 2*row.elders + 2*row.barons + 2*row.firsttower +3 #fast win bonus 
        else:
            return row.towers + 1.5*row.elementaldrakes + 2*row.elders + 2*row.barons + 2*row.firsttower
    else:    #scores for players
        return (3*row.kills) + (2*row.assists) + (0.02*row['total cs']) + (2*row.firstbloodkill) + (2*(row.triplekills-row.quadrakills)) + (4*(row.quadrakills-row.pentakills)) + (7*row.pentakills) - row.deaths

@st.experimental_memo
def get_data(url):
  df = pd.read_csv(url)
  df['score'] = df.apply(lambda row: score_f(row), axis=1)
  df['date'] = pd.to_datetime(df.date).dt.date
  return df


df = get_data("https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/2015_LoL_esports_match_data_from_OraclesElixir_20220322.csv")


st.title("I'm a test app")

st.header("hear me roar")

year = st.selectbox("year", ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
today = dt.date.today()
today = today.strftime('%Y%m%d')
url = f'https://oracleselixir-downloadable-match-data.s3-us-west-2.amazonaws.com/{year}_LoL_esports_match_data_from_OraclesElixir_{today}.csv'

df = get_data(url)

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
    p = df[(df.league.isin(list1)) & (df.position.isin(list2))].playername.unique()
    q = sorted(p)
    player = st.selectbox("player", q)
    p_df = df[df.playername == player]
    st.write(f"Most played champion: {p_df.champion.mode()[0]}")
    fig, axs = plt.subplots()
    ax = sns.countplot(data=p_df, x='champion')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax = sns.lineplot(data=p_df, x='date', y='score')
    st.pyplot(fig)
