import plotly.express as px
import streamlit as st

from src.analysis.business import business_overview


def payment_analysis_component():

    st.subheader("Payment Insights")

    # Run business analysis ONCE
    business_data = business_overview()

    payment_stats = (
        business_data["payment_type_stats"]
        .to_pandas()
    )

    col1, col2 = st.columns([1.2, 1])

    # -----------------------------------------
    # Payment Distribution
    # -----------------------------------------

    with col1:

        st.write("How are customers paying for their trips?")
        st.markdown("#### Trip Distribution")

        fig = px.pie(
            payment_stats,
            names="payment_method",
            values="total_trips",
            hole=0.55,
            title="Trip Distribution by Payment Method",
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )

        fig.update_layout(
            showlegend=True,
            margin=dict(
                t=60,
                b=20,
                l=20,
                r=20
            )
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

    # -----------------------------------------
    # Payment Summary
    # -----------------------------------------

    with col2:

        st.markdown("#### Payment Summary")

        top_payment = payment_stats.iloc[0]

        total_trips = payment_stats["total_trips"].sum()

        percentage = (
            top_payment["total_trips"] / total_trips
        ) * 100

        st.metric(
            "Most Common Payment Method",
            top_payment["payment_method"]
        )

        st.metric(
            "Share of Trips",
            f"{percentage:.1f}%"
        )

        st.info(
            f"💡 {top_payment['payment_method']} "
            f"is the most common payment method, "
            f"accounting for {percentage:.1f}% of trips."
        )