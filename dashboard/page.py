import streamlit as st

from src.analysis.overview import dataset_overview
from src.analysis.business import business_overview
from src.analysis.fare import fare_analysis

from components.demandAnalysis import demand_analysis_component
from components.vendorAnalysis import vendor_analysis_component

def dashboard_page():

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

    st.set_page_config(
    page_title="NYC Taxi Analytics",
    page_icon="🚖",
    layout="wide",
    initial_sidebar_state="expanded",
    )
    st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------
# Title
# ----------------------------------------------------

    st.title("🚖 NYC Taxi Analytics Dashboard")
    st.caption("January 2025 Yellow Taxi Dataset")
    
    st.divider()

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

    overview = dataset_overview()
    fare = fare_analysis()
    business = business_overview()

# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Trips",
            f"{overview['total_rows']:,}"
        )

    with col2:
        st.metric(
            "Total Revenue",
            f"${business['total_revenue']:,.2f}"
        )

    with col3:
        st.metric(
            "Average Fare",
            f"${fare['average_fare']:.2f}"
        )

    with col4:
        st.metric(
            "Average Distance",
            f"{business['avg_distance']:.2f} km"
        )

    ## demand analysis

    demand_analysis_component()  


    ## vendor analysis

    vendor_analysis_component()  