import plotly.express as px
import streamlit as st
from src.analysis.vendor import vendor_analysis

def vendor_analysis_component():

    st.divider()

    st.subheader("Vendor Performance")

    vendor_data = vendor_analysis()
    vendor_df = vendor_data.to_pandas()

    col1, col2 = st.columns(2)

    with col1:

        st.write("Which vendor generates the most revenue?")

        fig = px.pie(
            vendor_df,
            names="VendorID",
            values="total_revenue",
            title="Revenue by Vendor",
            
        )

        fig.update_layout(
            xaxis_title="Vendor",
            yaxis_title="Revenue ($)",
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

    with col2:

        st.write("Is the vendor with the highest revenue also handling the most trips?")

        fig = px.pie(
            vendor_df,
            names="VendorID",
            values="total_trips",
            title="Trips by Vendor",
           hole=0.55,
        )

        fig.update_layout(
            xaxis_title="Vendor",
            yaxis_title="Trips",
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

    top_vendor = vendor_df.loc[
    vendor_df["total_revenue"].idxmax()
]

    st.info(
        f"💡 Vendor {int(top_vendor['VendorID'])} "
        f"generated the highest revenue with "
        f"${top_vendor['total_revenue']:,.2f}."
    )