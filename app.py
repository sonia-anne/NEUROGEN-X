# app.py – NEUROGEN-X Dashboard in Streamlit

import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide")
st.title("🧠 NEUROGEN-X | Global Neuroregenerative System")

# --- Simulated Data ---
years = [2025, 2026, 2027, 2028, 2029]
traditional_costs = [850000, 870000, 890000, 910000, 930000]
neurogenx_costs = [8000, 7900, 7850, 7800, 7700]
traditional_effectiveness = [0.10, 0.12, 0.13, 0.15, 0.16]
neurogenx_effectiveness = [0.85, 0.89, 0.91, 0.93, 0.94]

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("💸 Comparative Treatment Costs")
    cost_fig = go.Figure()
    cost_fig.add_trace(go.Scatter(x=years, y=traditional_costs, mode='lines+markers', name='Traditional Therapies'))
    cost_fig.add_trace(go.Scatter(x=years, y=neurogenx_costs, mode='lines+markers', name='NEUROGEN-X'))
    cost_fig.update_layout(
        title="Annual Cost per Patient (USD)",
        xaxis_title="Year",
        yaxis_title="Cost (USD)",
        template="plotly_white"
    )
    st.plotly_chart(cost_fig, use_container_width=True)

with col2:
    st.subheader("📈 Clinical Effectiveness Over Time")
    eff_fig = go.Figure()
    eff_fig.add_trace(go.Bar(x=years, y=traditional_effectiveness, name='Traditional'))
    eff_fig.add_trace(go.Bar(x=years, y=neurogenx_effectiveness, name='NEUROGEN-X'))
    eff_fig.update_layout(
        barmode='group',
        title="Prion Degradation Efficiency",
        xaxis_title="Year",
        yaxis_title="Effectiveness",
        template="plotly_white"
    )
    st.plotly_chart(eff_fig, use_container_width=True)

# --- Summary ---
st.markdown("""
---
### 🔬 Project Summary
**NEUROGEN-X** is a revolutionary platform using smart nanorobots with CRISPR-Cas13d to degrade prions and regenerate neurons using nanofibrous scaffolds impregnated with BDNF.

### 📊 Key Stats
- **Degradation Efficiency:** 94% (vs. 48% for gold nanoparticle therapy)
- **Neuronal Regeneration:** +40% synaptic density in 2 weeks (preclinical)
- **Dose Cost:** $8,000 (vs. $850,000+ for traditional gene therapies)
- **Self-destruction:** <72h AI-monitored degradation

### 🌍 Global Impact
- 14,000+ lives saved annually by 2030
- 91% reduction in long-term neurodegenerative care costs
- Fully aligned with SDG 3 and 10 (WHO, 2024)
---
""")
