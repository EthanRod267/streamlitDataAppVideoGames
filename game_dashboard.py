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
tables, plots, insights = st.tabs(["Data","Charts","Insights"])

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

# keep the 6 biggest platforms and group the rest into "Other" so the pie stays readable
platform_sales = filtered.groupby("Platforms")["Sales_Millions"].sum().sort_values(ascending=False)
pie_data = platform_sales.head(6)
pie_data["Other"] = platform_sales.iloc[6:].sum()
pie_fig = px.pie(
    names=pie_data.index,
    values=pie_data.values,
    title="Share of Total Sales by Platform",
    labels={"names": "Platform", "values": "Sales (Millions of Units)"},
)

with plots:
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(pie_fig, use_container_width=True)
with tables:
    st.caption("Raw Data")
    st.dataframe(filtered)

    # total sales and number of games per company, highest sales first
    def rank_by_sales(column):
        ranked = (filtered.groupby(column)["Sales_Millions"]
                  .agg(Total_Sales_Millions="sum", Games="count")
                  .sort_values("Total_Sales_Millions", ascending=False)
                  .reset_index())
        ranked.index = ranked.index + 1  # start ranks at 1
        ranked.index.name = "Rank"
        return ranked

    pub_col, dev_col = st.columns(2)
    with pub_col:
        st.caption("Publishers Ranked by Sales")
        st.dataframe(rank_by_sales("Publisher"))
    with dev_col:
        st.caption("Developers Ranked by Sales")
        st.dataframe(rank_by_sales("Developer"))
with insights:
    st.subheader("What the data tells us")
    st.markdown("""
1. **Nintendo dominates the list.** Nintendo published 34 of the 100 games (1,015M units).
   Counting the Pokémon games co-published with The Pokémon Company, that rises to
   45 games and about **31% of all sales**.
2. **A few mega-hits account for a big share of sales.** *Tetris* (520M) and *Minecraft* (400M)
   make up **23%** of all sales, and the top 10 games make up **42%**.
   The average game sold 39.5M, but the median is only 25.0M.
3. **Quality beats quantity for some publishers.** Rockstar Games matches Mojang's 400M total
   with just 6 games (about 67M per game vs. Nintendo's ~30M), and Mojang does it with one game.
4. **Franchises drive sales.** All 10 Activision entries are *Call of Duty* games (264M combined),
   and Game Freak developed 12 Pokémon games on the list.
5. **The 2010s were the peak decade.** 47 of the 100 games came out in the 2010s,
   accounting for **51%** of all units sold.
6. **Releasing on many platforms pays off.** Multi-platform games are 49 of the 100 entries
   but **68%** of total sales. The Nintendo Switch is the strongest single platform (17 games).
7. **Small studios can compete.** *Terraria* (70M), *Human: Fall Flat* (55M) and
   *Stardew Valley* (50M) outsold many big-budget releases.
""")
    st.info("**Note:** sales figures are not all measured the same way. Some combine several "
            "versions, others count one platform only, so treat small differences with caution.")
