import plotly.express as px
import streamlit as st

from src.analysis.business import business_overview


def location_analysis_component():

    st.subheader("Location Insights")

    business_data = business_overview()

    pickup_df = (
        business_data["most_common_pu_location"]
        .to_pandas()
    )

    pickup_df["PULocationID"] = (
        pickup_df["PULocationID"]
        .astype(str)
    )

    fig = px.treemap(
        pickup_df,
        path=["PULocationID", "total_trips"],
        values="total_trips",
        title="Top Pickup Locations"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )