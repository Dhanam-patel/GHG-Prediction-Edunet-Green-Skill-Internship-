import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and encoders
model = joblib.load('Week2_GHG/models/final_model.pkl')
encoders = joblib.load('Week2_GHG/models/label_encoders.pkl')

st.title("Supply Chain GHG Emission Predictor")

st.write(
    "Enter the details below to predict the Supply Chain Emission Factors with Margins."
)

# Use dropdowns for categorical fields to avoid unseen label errors
substance = st.selectbox("Substance", encoders['Substance'].classes_)
unit = st.selectbox("Unit", encoders['Unit'].classes_)
source = st.selectbox("Source", encoders['Source'].classes_)
year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)

supply_chain_wo_margin = st.number_input(
    "Supply Chain Emission Factors without Margins", value=15.7
)
margin = st.number_input("Margins of Supply Chain Emission Factors", value=2.5)
dq_reliability = st.number_input(
    "DQ ReliabilityScore of Factors without Margins", min_value=0, max_value=10, value=5
)
dq_temporal = st.number_input(
    "DQ TemporalCorrelation of Factors without Margins", min_value=0, max_value=10, value=4
)
dq_geo = st.number_input(
    "DQ GeographicalCorrelation of Factors without Margins", min_value=0, max_value=10, value=3
)
dq_tech = st.number_input(
    "DQ TechnologicalCorrelation of Factors without Margins", min_value=0, max_value=10, value=4
)
dq_data = st.number_input(
    "DQ DataCollection of Factors without Margins", min_value=0, max_value=10, value=3
)

if st.button("Predict"):
    # Prepare input DataFrame
    input_dict = {
        'Substance': [substance],
        'Unit': [unit],
        'Supply Chain Emission Factors without Margins': [supply_chain_wo_margin],
        'Margins of Supply Chain Emission Factors': [margin],
        'DQ ReliabilityScore of Factors without Margins': [dq_reliability],
        'DQ TemporalCorrelation of Factors without Margins': [dq_temporal],
        'DQ GeographicalCorrelation of Factors without Margins': [dq_geo],
        'DQ TechnologicalCorrelation of Factors without Margins': [dq_tech],
        'DQ DataCollection of Factors without Margins': [dq_data],
        'Source': [source],
        'Year': [year],
    }
    input_df = pd.DataFrame(input_dict)

    # Encode categorical features using saved encoders
    input_df['Substance'] = encoders['Substance'].transform(input_df['Substance'])
    input_df['Unit'] = encoders['Unit'].transform(input_df['Unit'])
    input_df['Source'] = encoders['Source'].transform(input_df['Source'])

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Supply Chain Emission Factor with Margins: {prediction:.2f}")

st.write("Note: Only values present in the training data can be selected for categorical fields.")