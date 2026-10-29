import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization

st.title("Best selling video game dashboard")
st.header("CIS 3590 - Internship-Ready Software Development")
st.subheader("Ethan Rodriguez")

st.divider()

df = pd.read_csv("videogamesales.csv")
top_n = st.slider("Number of publishers to show", 3, 20, 10)
filtered = df.copy()
tables, plots= st.tabs(["Data","Charts"])

sales = (filtered.groupby(["Publisher", "Developer"])["Sales_Millions"].sum()
         .reset_index())
top_pubs = (sales.groupby("Publisher")["Sales_Millions"].sum()
            .nlargest(top_n).index)
sales = sales[sales["Publisher"].isin(top_pubs)]

fig = px.bar(
    sales,
    x="Publisher",
    y="Sales_Millions",
    color="Developer",                      # this creates the legend
    title=f"Top {top_n} Publishers by Total Sales",
    labels={"Publisher": "Publisher",
            "Sales_Millions": "Total Sales (Millions of Units)",
            "Developer": "Game Developer"},     # axis and legend labels
)
fig.update_layout(xaxis={"categoryorder": "total descending"})
with plots:
    st.plotly_chart(fig, use_container_width=True)
with tables:
    st.caption("Raw Data")
    st.dataframe(filtered)
    st.caption("Descriptive Statistics")
    st.dataframe(filtered.describe())