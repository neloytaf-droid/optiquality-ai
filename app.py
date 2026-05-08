import streamlit as st
import pandas as pd
import numpy as np

# Title and App Interface
st.title("🛡️ OptiQuality AI: Strategic Decision Support")
st.markdown("### Level 7 OQM Assessment Prototype")

# Sidebar for controls
st.sidebar.header("Operations Settings")
threshold = st.sidebar.slider("Material Moisture Threshold (%)", 0.0, 5.0, 2.0)

# 1. Data Upload
uploaded_file = st.file_uploader("Upload Production Log (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Production Data", df)

    # 2. Quality Estimation Logic (LO2)
    st.divider()
    st.write("### 🧠 AI Quality Estimation")
    
    # Simple logic to simulate AI analysis
    risky_batches = df[df['Material_Moisture_%'] > threshold]
    
    if not risky_batches.empty:
        st.error(f"⚠️ Alert: {len(risky_batches)} batches exceed quality threshold!")
        st.write(risky_batches)
        
        # Simulated GenAI Strategic Insight
        st.info(f"**Strategic Insight:** Based on current moisture levels ({risky_batches['Material_Moisture_%'].max()}%), "
                "there is a 15% projected increase in micro-fracture defects. "
                "Recommendation: Trigger immediate dehumidification in Zone B.")
    else:
        st.success("✅ All batches within quality specification limits.")

    # 3. Visualization
    st.line_chart(df.set_index('Batch_ID')[['Temp_C', 'Quality_Score']])
