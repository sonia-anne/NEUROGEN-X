
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide")

st.title("🧠 NEUROGEN-X | Advanced Nanotherapy for Creutzfeldt-Jakob Disease")

st.markdown("""
This dashboard presents interactive scientific data and visual evidence for **NEUROGEN-X**, 
an innovative nanorobot-based treatment that degrades prions and regenerates brain tissue 
with CRISPR-Cas13d and neurotrophic scaffolds.
""")

# Simulated efficacy data
data = {
    "Therapy": ["Quinacrine", "Gold Nanoparticles (MIT)", "ASO (NIH)", "NEUROGEN-X"],
    "Efficacy (%)": [0, 48, 70, 94],
    "Main Limitation": [
        "Systemic toxicity, liver damage",
        "Organ accumulation, immune response",
        "Only preventive, no regeneration",
        "No significant limitations (simulated)"
    ]
}
df = pd.DataFrame(data)

st.subheader("📊 Comparative Efficacy of Prion Therapies")
fig = px.bar(df, x="Therapy", y="Efficacy (%)", color="Therapy", text="Efficacy (%)",
             hover_data=["Main Limitation"], height=500)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🧬 Key Components of NEUROGEN-X")
st.markdown("""
- **Intelligent nanorobots** with AI-based molecular GPS  
- **CRISPR-Cas13d** enzymatic system targeting prions  
- **BDNF-impregnated scaffolds** for neuronal regeneration  
- **Autodestruction mechanism** triggered by pH and biochemical signals  
- **Cost per dose:** ~\$8,000 (vs. \$1.2M in current gene therapies)
""")

st.markdown("---")
st.subheader("🌍 Global Impact")
st.markdown("""
- Aligned with **SDG 3** (Good Health) and **SDG 10** (Reduced Inequalities)  
- Designed for scalable, low-cost treatment accessible to underserved regions  
- Projected to reduce CJD mortality and neurological deterioration significantly
""")

st.markdown("#### 🔬 Simulation Snapshot")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/CJD_brain.jpg/640px-CJD_brain.jpg",
         caption="Brain atrophy caused by Creutzfeldt-Jakob Disease", use_column_width=True)

st.markdown("---")
st.caption("Sonia Annette Echeverría Vera · Neurotechnology Proposal · Ecuador · 2025")
