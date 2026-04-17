import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="EcoTrack | GHG Predictor",
    page_icon="🌿",
    layout="centered", # Changed from wide for better focus
    initial_sidebar_state="collapsed",
)

# Custom CSS for a consistent, premium look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: radial-gradient(circle at 10% 20%, #F1F8E8 0%, #FFFFFF 90%);
        font-family: 'Inter', sans-serif;
    }

    /* Target the main container for card-like feel */
    .main .block-container {
        padding-top: 3rem !important;
        max-width: 850px !important;
    }

    /* Header styling */
    .header-tag {
        background: #1A5319;
        color: white;
        padding: 4px 16px;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .hero-title {
        color: #1A5319;
        font-size: 5rem; /* Increased size */
        font-weight: 900;
        line-height: 1.0;
        margin-bottom: 1.5rem;
        letter-spacing: -3px;
    }

    .hero-subtitle {
        color: #4F6F52;
        font-size: 1.25rem;
        margin-bottom: 4rem;
        line-height: 1.6;
        max-width: 650px;
    }

    /* Surgical Fix for Number Input combined border */
    div[data-testid="stNumberInput"] > div:nth-child(2) {
        border: 2px solid #A1C398 !important;
        border-radius: 14px !important;
        background-color: white !important;
        display: flex !important;
        align-items: center !important;
        overflow: hidden !important;
    }

    /* Neutralize all inner elements */
    div[data-testid="stNumberInput"] [data-baseweb="input"],
    div[data-testid="stNumberInput"] [data-baseweb="input"] > div,
    div[data-testid="stNumberInput"] button {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    /* Restore Selectbox styling */
    div[data-testid="stSelectbox"] > div:nth-child(2) {
        border: 2px solid #A1C398 !important;
        border-radius: 14px !important;
        background-color: white !important;
        overflow: hidden !important;
    }
    
    div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
        border: none !important;
    }




    /* Padding for the text inside */
    input {
        padding-top: 10px !important;
        padding-bottom: 10px !important;
    }



    /* Expander / Data Quality Title Styling */
    .stExpander {
        border: none !important;
        background: rgba(255, 255, 255, 0.5) !important;
        border-radius: 16px !important;
        margin-top: 2rem !important;
    }

    .stExpander summary p {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #1A5319 !important;
    }


    /* Form Fields Styling */
    .stSelectbox, .stNumberInput, .stSlider {
        margin-bottom: 1rem;
    }

    label {
        font-weight: 600 !important;
        color: #1A5319 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.5rem !important;
    }

    /* Button Overhaul */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #1A5319 0%, #2ECC71 100%) !important;
        color: white !important;
        padding: 0.8rem 2rem !important;
        border-radius: 14px !important;
        border: none !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        height: auto !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 10px 20px rgba(26, 83, 25, 0.15) !important;
        margin-top: 1rem;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(26, 83, 25, 0.25) !important;
    }

    /* Prediction Result Card - Light Minimalist */
    .prediction-container {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(12px);
        padding: 3rem 2rem;
        border-radius: 28px;
        text-align: center;
        margin-top: 4rem;
        border: 1px solid rgba(26, 83, 25, 0.08); /* Extremely subtle border */
        box-shadow: 0 25px 50px -12px rgba(26, 83, 25, 0.12);
    }

    .prediction-label {
        color: #4F6F52;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 700;
        margin-bottom: 1rem;
    }


    .prediction-value {
        color: #1A5319;
        font-size: 6rem; /* High impact size */
        font-weight: 900;
        margin: 0;
        line-height: 1;
        letter-spacing: -4px;
    }

    .prediction-unit {
        color: #2ECC71;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 0.5rem;
        opacity: 0.8;
    }


    /* Footer */
    .footer {
        text-align: center;
        padding: 4rem 0 2rem;
        color: #80AF81;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# Cache model loading for performance
@st.cache_resource
def load_assets():
    try:
        model = joblib.load('Week2_GHG/models/final_model.pkl')
        encoders = joblib.load('Week2_GHG/models/label_encoders.pkl')
        return model, encoders
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

model, encoders = load_assets()

if model and encoders:
    # Hero Section
    st.markdown('<div class="header-tag">🌿 AI Powered</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Supply Chain<br>GHG Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Optimize your supply chain footprint with enterprise-grade machine learning. Get precise emission factor predictions in seconds.</p>', unsafe_allow_html=True)

    # Main Form
    with st.container():
        st.subheader("📍 Data Input")
        
        # Categorical Inputs Row
        c1, c2 = st.columns(2)
        with c1:
            substance = st.selectbox("Substance Type", encoders['Substance'].classes_)
            source = st.selectbox("Data Source", encoders['Source'].classes_)
        with c2:
            unit = st.selectbox("Measurement Unit", encoders['Unit'].classes_)
            year = st.slider("Assessment Year", 2000, 2100, 2024)

        st.markdown("---")
        
        # Numerical Inputs Row
        st.subheader("📊 Primary Metrics")
        m1, m2 = st.columns(2)
        with m1:
            supply_chain_wo_margin = st.number_input("Base Emission Factor", value=15.70, step=0.01)
        with m2:
            margin = st.number_input("Statistical Margin", value=2.50, step=0.01)

        # Advanced Subsection
        with st.expander("🛠️ Data Quality Details (Advanced)", expanded=False):
            st.write("Refine your prediction by providing quality scores (0-10)")
            dq_c1, dq_c2 = st.columns(2)
            with dq_c1:
                dq_reliability = st.select_slider("Reliability", options=list(range(11)), value=5)
                dq_temporal = st.select_slider("Temporal Correlation", options=list(range(11)), value=4)
                dq_geo = st.select_slider("Geographical Correlation", options=list(range(11)), value=3)
            with dq_c2:
                dq_tech = st.select_slider("Technological Correlation", options=list(range(11)), value=4)
                dq_data = st.select_slider("Data Collection Coverage", options=list(range(11)), value=3)

        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        if st.button("Generate Emission Analysis"):
            # Data Preparation
            input_data = pd.DataFrame([{
                'Substance': encoders['Substance'].transform([substance])[0],
                'Unit': encoders['Unit'].transform([unit])[0],
                'Supply Chain Emission Factors without Margins': supply_chain_wo_margin,
                'Margins of Supply Chain Emission Factors': margin,
                'DQ ReliabilityScore of Factors without Margins': dq_reliability,
                'DQ TemporalCorrelation of Factors without Margins': dq_temporal,
                'DQ GeographicalCorrelation of Factors without Margins': dq_geo,
                'DQ TechnologicalCorrelation of Factors without Margins': dq_tech,
                'DQ DataCollection of Factors without Margins': dq_data,
                'Source': encoders['Source'].transform([source])[0],
                'Year': year,
            }])

            # Prediction
            prediction = model.predict(input_data)[0]
            
            # Result Display
            st.markdown(f"""
                <div class="prediction-container">
                    <div class="prediction-label">Estimated Emission Factor</div>
                    <h2 class="prediction-value">{prediction:.2f}</h2>
                    <div class="prediction-unit">kg CO2e per unit • Predicted by EcoTrack AI</div>
                </div>
            """, unsafe_allow_html=True)
            st.toast('Analysis successfully generated!', icon='🌿')


    st.markdown('<div class="footer">Developed for AICTE Edunet Green-Skill Internship • 2024</div>', unsafe_allow_html=True)
else:
    st.error("Model assets not found. Please verify the 'Week2_GHG/models' directory.")

