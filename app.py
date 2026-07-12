import html
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import tempfile
import uuid
import os
from dotenv import load_dotenv

load_dotenv()
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from database import init_db, save_assessment, get_assessments, init_gamification_db
import gamification as gf
from emissions import calculate_footprint, calculate_eco_score

from recommendations import generate_recommendations
from ocr_utils import extract_text_from_file, parse_energy_consumption

# Added for Route Planning & Offsets
from database import (
    init_marketplace_db, save_journey_profile, get_journey_profiles, delete_journey_profile,
    save_offset_transaction, get_offset_transactions, delete_offset_transaction,
    get_total_offsets, get_total_spend
)
from marketplace import (
    calculate_trip_emissions, calculate_recurring_trip_emissions, compare_transit_modes,
    calculate_offset_cost, validate_offset_transaction, get_offset_projects,
    calculate_net_emissions, calculate_net_zero_progress, get_project_by_id, EMISSION_FACTORS
)



def h(text):
    return html.escape(str(text))


# -------------------------
# INIT
# -------------------------

init_db()
init_gamification_db()
init_marketplace_db()
from database import init_water_db
init_water_db()

if 'extracted_kwh' not in st.session_state:
    st.session_state.extracted_kwh = 200.0


# -------------------------
# DEFAULT FORM VALUES
# -------------------------
DEFAULT_VALUES = {
    "transport": "Car",
    "distance": 10.0,
    "electricity": 200.0,
    "diet": "Vegetarian",
    "flights": 0,
}

for key, value in DEFAULT_VALUES.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.set_page_config(
    page_title="EcoBuddy",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -------------------------
# REFERENCE-INSPIRED ADVANCED STYLING

from styles.theme import apply_theme
apply_theme()

st.markdown("<div class='title'>🌱 EcoBuddy AI+</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your Personal AI-Powered Carbon Footprint Tracker & Eco Assistant</div>", unsafe_allow_html=True)

st.info("👈 Please select a module from the sidebar to get started!")
