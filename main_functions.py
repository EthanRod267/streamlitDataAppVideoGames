import pandas as pd
import streamlit as st

# Functions to load and analyze video game sales data
@st.cache_data
def load_data(path):
    return pd.read_csv(path, encoding="utf-8")

# Functions to calculate top sales by different categories
def sales_by_publisher(df, top_n):
    return (df.groupby("Publisher")["Sales_Millions"].sum()
              .nlargest(top_n).reset_index())
def sales_by_platform(df, top_n):
    return (df.groupby("Platform")["Sales_Millions"].sum()
              .nlargest(top_n).reset_index())
def sales_by_year(df, top_n):
    return (df.groupby("Year")["Sales_Millions"].sum()
              .nlargest(top_n).reset_index())
