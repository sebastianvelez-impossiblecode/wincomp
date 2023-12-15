import pandas as pd
import streamlit as st

df = pd.read_csv("fe/full_harvest_data.csv", parse_dates=["siembra"])

st.title("Demand Forecasting")

st.sidebar.header("User input features")

task = st.sidebar.radio(
    "Select a task to perform",
    ["df exploration", "Demand type visualization", "Product df visualization"],
)

if task == "df exploration":
    category = st.sidebar.selectbox(
        "Select a product category", pd.unique(df["variedad"])
    )

    date_range = st.sidebar.select_slider(
        "Select a range of dates",
        pd.unique(df["siembra"]),
        value=(list(df["siembra"])[0], list(df["siembra"])[-1]),
    )

    display_df = df[
        (df["variedad"] == category)
        & (df["siembra"] >= date_range[0])
        & (df["siembra"] <= date_range[1])
    ]

    st.markdown(
        """
        df dataset exploration:
        """
    )
    st.dataframe(display_df, height=600)
