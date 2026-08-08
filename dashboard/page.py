import streamlit as st

from src.analysis.overview import dataset_overview
from src.analysis.business import business_overview
from src.analysis.fare import fare_analysis

from components.demandAnalysis import demand_analysis_component
from components.vendorAnalysis import vendor_analysis_component
from components.paymentAnalysis import payment_analysis_component
from components.kpiCardsAnalysis import kpi_cards_component
from components.locationAnalysis import location_analysis_component

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
    

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

    # KPI Cards 
    st.divider()
    kpi_cards_component()


    # Demand Analysis
    st.divider()
    demand_analysis_component()


    # Vendor Analysis
    st.divider()
    vendor_analysis_component()


    # Payment Analysis
    st.divider()
    payment_analysis_component()


    # Location Analysis
    st.divider()
    location_analysis_component()