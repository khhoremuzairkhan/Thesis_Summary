# summary.py

import numpy as np
import pandas as pd
import pandapower as pp
import pandapower.networks as pn
import pandapower.plotting as plot
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Thesis Information
# -------------------------------
st.set_page_config(page_title="Thesis Summary", layout="wide")

st.title("**Total Loss Estimation in Electrical Grids with Integrated Renewable Generation using AI**")

st.markdown("""
### **Supervisor:** Dr Shariq Mahmood Khan  
### **Co-Supervisor:** Shariq Shaikh  
### **Student:** Khhorem Uzair Khan  
""")

# -------------------------------
# Tabs
# -------------------------------
tab1, tab2, tab3 = st.tabs([
    "IEEE 14 Bus Overview",
    "Research Overview",
    "Trained Model Performance"
])

# -------------------------------
# TAB 1: IEEE 14 Bus Overview
# -------------------------------
with tab1:
    st.header("14 Bus System at a Glance")

    # Load IEEE 14-bus test system
    net = pn.case14()

    # Show basic system info
    st.write("**Network Overview:**")
    st.write(f"- Number of Buses: {len(net.bus)}")
    st.write(f"- Number of Lines: {len(net.line)}")
    st.write(f"- Number of Loads: {len(net.load)}")
    st.write(f"- Number of Generators: {len(net.gen)}")
    st.write(f"- Number of Transformers: {len(net.trafo)}")

    # Plot the full 14-bus system
    fig, ax = plt.subplots(figsize=(8,6))
    plot.simple_plot(net, ax=ax, show_plot=False)
    st.pyplot(fig)

    # Optionally show the bus, line data tables
    with st.expander("Show Bus Data"):
        st.dataframe(net.bus)

    with st.expander("Show Line Data"):
        st.dataframe(net.line)

    with st.expander("Show Load Data"):
        st.dataframe(net.load)

    with st.expander("Show Generator Data"):
        st.dataframe(net.gen)


# -------------------------------
# TAB 2: Research Overview
# -------------------------------
with tab2:
    st.header("Research Overview")
    st.write("Loss Estimation in Power grids is quite challenge for various utility and power management organizations.")


# -------------------------------
# TAB 3: Trained Model Performance
# -------------------------------
with tab3:
    st.header("Trained Model Performance")

    try:
        df = pd.read_excel("Merged_All_ML_and_DL_Results.xlsx")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error("❌ File 'Merged_All_ML_and_DL_Results.xlsx' not found in the current directory.")
