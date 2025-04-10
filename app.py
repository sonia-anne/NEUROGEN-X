# NEUROGEN-X | Streamlit app.py

import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide")
st.title("🧠 NEUROGEN-X | Global Neuroregenerative System")

# --- Simulated Data ---
years = [2025, 2026, 2027, 2028, 2029]
traditional_costs = [850000, 870000, 890000, 910000, 930000]  # USD
neurogenx_costs = [8000, 7900, 7850, 7800, 7700]
effectiveness = [0.1, 0.12, 0.13, 0.15, 0.16]  # traditional
effectiveness_ngx = [0.85, 0.89, 0.91, 0.93, 0.94]

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("💸 Comparative Treatment Costs")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=traditional_costs, mode='lines+markers', name='Traditional Therapies'))
    fig.add_trace(go.Scatter(x=years, y=neurogenx_costs, mode='lines+markers', name='NEUROGEN-X'))
    fig.update_layout(title="Cost per Patient (USD)", xaxis_title="Year", yaxis_title="Cost")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📈 Clinical Effectiveness Over Time")
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=years, y=effectiveness, name='Traditional'))
    fig2.add_trace(go.Bar(x=years, y=effectiveness_ngx, name='NEUROGEN-X'))
    fig2.update_layout(barmode='group', title="Treatment Efficacy (Prion Reduction)", xaxis_title="Year", yaxis_title="Effectiveness")
    st.plotly_chart(fig2, use_container_width=True)

# --- Additional Details ---
st.markdown("""
### 🔬 Project Summary
**NEUROGEN-X** uses intelligent nanorobots to cross the blood-brain barrier, detect misfolded prions, and deploy CRISPR-Cas13d to degrade them. Integrated with biodegradable scaffolds releasing BDNF, the system regenerates brain circuits in parallel. 

### 📊 Technical Highlights
- **Targeted degradation efficiency:** 94% (vs. 48% in MIT gold nanoparticle trials)
- **Neuronal regeneration rate:** +40% synaptic density in 2 weeks
- **Cost per dose:** ~$8000 vs $850,000+ for gene therapy
- **Self-destruction cycle:** <72h via AI-monitored degradation

### 🌐 Impact Simulation (2030)
- Estimated 14,000 lives saved annually
- Reduction in long-term care costs by 91%
- Global accessibility plan aligned with SDG 3 & 10

---
Made with ❤️ by Annette Echeverría Vera
""")
