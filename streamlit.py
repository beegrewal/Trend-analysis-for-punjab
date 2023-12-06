import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# important Liabraries


# start plot view for india in main section
st.header("Trend Analysis for Rainfall In India")
st.subheader("2000-2015")

df = pd.read_csv('rainfall in india 2000-2015.csv')
st.dataframe(df)
# end plot view for india in main section


#plot section for main
st.subheader("Plot View")
df2=df[['SUBDIVISION','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].groupby("SUBDIVISION").sum().reset_index().copy()

plt.figure(figsize=(20,5))
sns.barplot(df2,x='SUBDIVISION',y='JAN')
plt.xticks(rotation=90)
st.pyplot(plt)
# end plot section for main


st.subheader("Coolab report link") 
st.markdown("[Google Coolab Report](https://colab.research.google.com/drive/1q_5lc1YlyCP6vCyQNQpVInlwvygxOHRJ?usp=sharing)")



# sidebar section
st.sidebar.title("Trend Analysis for Punjab Rainfall")
st.sidebar.subheader("2000-2015")

st.sidebar.header("Select Country")
st.sidebar.selectbox("", ["India"])
st.sidebar.subheader("Select State")
st.sidebar.selectbox("", ["Punjab"])
st.sidebar.subheader("Select Month")
st.sidebar.selectbox("", ["ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])


# end sidebar section

# Functions for sidebar

