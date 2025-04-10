
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page settings
st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide")

# Title
st.title("🧠 NEUROGEN-X | Nanorobotic Cure for Creutzfeldt-Jakob Disease")

# Description
st.markdown("""
NEUROGEN-X is a nanotechnology-based therapy that targets and degrades prions using intelligent nanorobots
equipped with CRISPR-Cas13d and promotes brain regeneration through BDNF-impregnated scaffolds.
This dashboard showcases simulated comparative efficacy and core features.
""")

# Comparative efficacy data
therapies = ["Quinacrine", "Gold Nanoparticles (MIT)", "ASO (NIH)", "NEUROGEN-X"]
efficacy = [0, 48, 70, 94]
limitations = [
    "Systemic toxicity, liver damage",
    "Organ accumulation, immune response",
    "Only preventive, no regeneration",
    "No major limitations (simulated)"
]

# Create bar chart
fig = go.Figure(data=[go.Bar(
    x=therapies,
    y=efficacy,
    text=efficacy,
    textposition='auto',
    marker_color=['#FF6666', '#FFCC66', '#66CCFF', '#66FF66'],
    hovertext=limitations,
    hoverinfo="text+y"
)])
fig.update_layout(
    title="Simulated Efficacy of Prion Therapies",
    xaxis_title="Therapy",
    yaxis_title="Efficacy (%)",
    height=500
)

# Show chart
st.plotly_chart(fig, use_container_width=True)

# Key Features
st.markdown("### 🧬 Key Features of NEUROGEN-X")
st.markdown("""
- Nanorobots with molecular GPS guided by AI.
- CRISPR-Cas13d targeting prions with 94% degradation rate.
- Neural regeneration via nanoscaffolds and BDNF.
- Smart auto-destruction to prevent accumulation.
- Estimated cost: $8,000 per dose (vs $1.2M gene therapies).
""")

# Impact Summary
st.markdown("### 🌍 Global Impact and Accessibility")
st.markdown("""
- Aligned with **SDG 3** (Health) and **SDG 10** (Inequality).
- Designed for global implementation, including low-resource settings.
- Integrates neuroscience, bioengineering, and AI.
""")

# Footer
st.markdown("---")
st.caption("Developed by Sonia Annette Echeverría Vera · Ecuador · 2025")
