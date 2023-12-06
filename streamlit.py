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
df2=df[['SUBDIVISION','ANNUAL','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].groupby("SUBDIVISION").sum().reset_index().copy()

plt.figure(figsize=(20,5))
sns.barplot(df2,x='SUBDIVISION',y='ANNUAL')
plt.xticks(rotation=90)
st.pyplot(plt)
# end plot section for main




# sidebar section
st.sidebar.title("Trend Analysis for Rainfall")
st.sidebar.subheader("2000-2015")
st.sidebar.selectbox("Select Country :", ["India"])



# end sidebar section

# Functions for sidebar

st.header("Trend Analysis for Rainfall In Selected State")
st.subheader("2000-2015")

df2 = pd.read_csv('district wise rainfall normal.csv')

# Create sidebar selectors for country and year selection
selected_country = st.sidebar.selectbox(
    "Select State:",
    options=df2["STATE_UT_NAME"].unique()
)



# Filter the data based on the selected country and year
if selected_country != "All":
    filtered_df = df2[(df2["STATE_UT_NAME"] == selected_country)]

else:
    filtered_df = df2



# Display the filtered DataFrame
st.dataframe(filtered_df)

st.subheader("Plot View (District)")
# Display a bar chart of rainfall for the selected country and year
sns.barplot(x="DISTRICT", y="ANNUAL", data=filtered_df)
plt.xticks(rotation=90)
st.pyplot(plt)


[For More Google Coolab]()

