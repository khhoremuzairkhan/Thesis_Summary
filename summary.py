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
tab1, tab2, tab3, tab4 = st.tabs([
    "IEEE 14 Bus Overview",
    "Research Overview",
    "Trained Model Performance",
    "Workflow"
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

        # Split into ML and DL DataFrames
        ML_df = df[df["Model_Type"] == "ML_Algorithm"].copy()
        DL_df = df[df["Model_Type"] == "Neural_Network"].copy()

        # Drop irrelevant columns
        if not ML_df.empty:
            ML_df = ML_df.drop(columns=["Architecture", "Activation", "Dropout"], errors="ignore")
        if not DL_df.empty:
            DL_df = DL_df.drop(columns=["Model_Name"], errors="ignore")

        # Selection radio button
        option = st.radio("Select Model Type to View:", ["ML Algorithms", "Neural Networks"])

        if option == "ML Algorithms":
            selected_df = ML_df
            st.subheader("Machine Learning Models")
            st.dataframe(selected_df, use_container_width=True)
        else:
            selected_df = DL_df
            st.subheader("Deep Learning Models")
            st.dataframe(selected_df, use_container_width=True)

        # Selection of target and metric
        target_option = st.radio("Select the intended target:", ["Active Loss", "Reactive Loss"])
        metric_option = st.radio("Select the important metric:", ["MSE", "MAE", "R2"])

        # Filter based on target
        filtered_df = selected_df[selected_df["Target"] == target_option].copy()

        if not filtered_df.empty and metric_option in filtered_df.columns:
            # Sorting condition
            ascending = False if metric_option == "R2" else True
            sorted_df = filtered_df.sort_values(by=metric_option, ascending=ascending)

            # Dynamic heading
            st.subheader(f"Lowest {metric_option} for predicting {target_option} using {option}")

            # Show top 5
            st.dataframe(sorted_df.head(5), use_container_width=True)
        else:
            st.warning(f"No data available for {option} with target '{target_option}' and metric '{metric_option}'.")

    except FileNotFoundError:
        st.error("❌ File 'Merged_All_ML_and_DL_Results.xlsx' not found in the current directory.")


# -------------------------------
# TAB 4: Workflow
# -------------------------------
with tab4:
    st.header("Workflow for the Project")

    st.write(
        "Took real world load profile from 2020 to 2024 from "
        "[CAISO Demand Trend](https://www.caiso.com/TodaysOutlook/Pages/Demand.aspx)"
    )

    # Centered and responsive arrow (10% of screen width)
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
            <img src="app/static/arrow.png" style="width:10%; min-width:50px; max-width:120px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Normalized the load profile as per respective standard loads of the IEEE 14 bus system"
    )
