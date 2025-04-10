import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configurar página
st.set_page_config(page_title="NEUROGEN-X | Dashboard", layout="wide")

# Título
st.title("🧠 NEUROGEN-X: Nanorobotic Therapy for Creutzfeldt-Jakob Disease")

# Introducción
st.markdown("""
NEUROGEN-X is a revolutionary nanobot therapy using CRISPR-Cas13d to degrade prions and regenerate brain tissue.
This dashboard presents comparative efficacy, core features, and global impact.
""")

# Datos comparativos
df = pd.DataFrame({
    "Therapy": ["Quinacrine", "MIT Nanoparticles", "NIH ASO", "NEUROGEN-X"],
    "Efficacy": [0, 48, 70, 94],
    "Toxicity": ["High", "Moderate", "Low", "None"],
    "Regeneration": ["❌", "❌", "❌", "✅"]
})

# Gráfico
fig = go.Figure(data=[
    go.Bar(name='Efficacy (%)', x=df["Therapy"], y=df["Efficacy"],
           marker_color=['red', 'orange', 'blue', 'green'])
])
fig.update_layout(title="📊 Therapy Efficacy Comparison",
                  yaxis_title="Efficacy (%)",
                  xaxis_title="Therapy",
                  height=500)

st.plotly_chart(fig, use_container_width=True)

# Tabla
st.subheader("📋 Key Comparison Table")
st.dataframe(df, use_container_width=True)

# Componentes del sistema
st.subheader("🔬 NEUROGEN-X Components")
st.markdown("""
- **AI-guided nanobots** with molecular GPS  
- **CRISPR-Cas13d** for prion degradation  
- **BDNF delivery** for neuron regeneration  
- **Smart autodestruction** upon pH change  
- **Projected cost:** ~$8,000 vs. $1.2M for current gene therapies  
""")

# Impacto global
st.subheader("🌍 Global & Ethical Impact")
st.markdown("""
- Targets underserved regions with scalable design  
- Avoids immune overreaction, over-editing or surgery  
- Supports SDG 3 and SDG 10 for health and equity  
""")

# Cierre
st.markdown("---")
st.caption("Created by Sonia Annette Echeverría Vera · Ecuador · 2025")
