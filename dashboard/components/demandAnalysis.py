import plotly.express as px
import streamlit as st
from src.analysis.time import time_analysis

def demand_analysis_component():

    st.subheader("Demand Analysis")

    time_data = time_analysis()

    col1, col2 = st.columns(2)

    with col1:

        st.write("When is demand highest?")

        hourly_data = time_data["trips_by_hour"].to_pandas()

        fig = px.line(
            hourly_data,
            x="pickup_hour",
            y="total_trips",
            markers=True,
            title="Trips by Hour"
        )

        fig.update_layout(
            xaxis_title="Pickup Hour",
            yaxis_title="Trips",
            hovermode="x unified"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )


    with col2:

        st.write("Which days are busiest?")

        weekday_data = time_data["trips_by_weekday"].to_pandas()

        fig = px.bar(
            weekday_data,
            x="weekday",
            y="total_trips",
            title="Trips by Weekday"
        )

        fig.update_layout(
            xaxis_title="Weekday",
            yaxis_title="Trips"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )