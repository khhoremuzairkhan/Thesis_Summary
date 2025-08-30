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
    "Workflow",
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
# TAB 3: Workflow
# -------------------------------
with tab3:
    st.header("Work done is as follows")

    st.markdown("""
    1. Took IEEE 14 bus system information from **PandaPower Library**  
    2. Took real-world load profile from [CAISO Demand Trend](https://www.caiso.com/todays-outlook#section-demand-trend) for the years **2020–2024**  
    3. Normalized the load profile as per standard IEEE 14 bus system
    4. Took solar load profile from [CAISO Renewables Trend](https://www.caiso.com/todays-outlook/supply#section-renewables-trend) for the years **2020–2024**   
    5. As per the paper *"Impact of Increased Penetration of Photovoltaic Generation on Power Systems"* (p.4), assumed **20% of the system power as Solar Capacity**  
    """)
     
    
    # Add clickable link to PDF (opens in new tab)
    with open("Impact of Increased Penetration of Photovoltaic Generation on Power Systems.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 See Paper",
        data=PDFbyte,
        file_name="Impact of Increased Penetration of Photovoltaic Generation on Power Systems.pdf",
        mime="application/pdf"
    )
    
    
    st.markdown(""" 
    6. Normalized the solar generation to maximum of **20% of 259 MW = 51.8 MW**  
    7. Ran simulation for complete load profile of 5 years for active and reactive losses by placing solar on all **non-generator and non-swing buses**  
    """)

    # Show Solar Placement Summary
    try:
        solar_df = pd.read_excel("Solar Placement Summary.xlsx")
        st.subheader("Solar Placement Summary")
        st.dataframe(solar_df, use_container_width=True)
    except FileNotFoundError:
        st.error("⚠️ Solar Placement Summary.xlsx not found in the directory.")
    except Exception as e:
        st.error(f"⚠️ Error loading Solar Placement Summary.xlsx: {e}")

    st.markdown("""
    8. Chose **Bus 3** for solar placement  
    9. Took wind generation profile from [CAISO Renewables Trend](https://www.caiso.com/todays-outlook/supply#section-renewables-trend) for the years **2020–2024**  
    10. Assumed Active Power from wind generation at **Unity Power Factor** (based on *"Short Circuit Current Contribution for Different Wind Turbine Generator Types"*, p.8)  
    """)
    # Add clickable link to PDF (opens in new tab)
    with open("Short Circuit Current Contribtuion for Different Wind Turbine Generator Types.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 See Paper",
        data=PDFbyte,
        file_name="Short Circuit Current Contribtuion for Different Wind Turbine Generator Types.pdf",
        mime="application/pdf"
    )
    st.markdown(""" 
    13. Ran load flow with solar on Bus 3 and wind on all buses except **generator, swing, and solar buses**  
    """)
    
    
    
    
    
    st.markdown("""
    11. Sized Wind Capacity to **40% of system power** (based on *"Research on Optimal Wind Power Penetration Ratio..."*)  
    12. This made the Wind Capacity = **40% of 259 MW = 103.6 MW** """)
    
    # Add clickable link to PDF (opens in new tab)
    with open("Testing of Electrical Energy Meters Subject to Realistic Distorted Voltages and Currents.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 See Paper",
        data=PDFbyte,
        file_name="Testing of Electrical Energy Meters Subject to Realistic Distorted Voltages and Currents.pdf",
        mime="application/pdf"
    )
    st.markdown(""" 
    13. Ran load flow with solar on Bus 3 and wind on all buses except **generator, swing, and solar buses**  
    """)

    # Show Wind Placement Summary
    try:
        wind_df = pd.read_excel("Wind Placement Summary.xlsx")
        st.subheader("Wind Placement Summary")
        st.dataframe(wind_df, use_container_width=True)
    except FileNotFoundError:
        st.error("⚠️ Wind Placement Summary.xlsx not found in the directory.")
    except Exception as e:
        st.error(f"⚠️ Error loading Wind Placement Summary.xlsx: {e}")

    st.markdown("""
    14. Chose **Bus 13** for wind placement due to least reactive losses  
    15. Carried out Load Flow for IEEE 14-bus system with load profile, wind, and solar generation for **5 years**  
    16. Added maximum of **2.5% noise** to energy readings (based on *"Testing of Electrical Energy Meters Subject to Realistic Distorted Voltages and Currents"*,page 3 table 1 and table 2, EN 50470 / IEC 62053-21,-22)  
    """)
    
    # Add clickable link to PDF (opens in new tab)
    with open("Testing of Electrical Energy Meters Subject to Realistic Distorted Voltages and Currents.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 See Paper",
        data=PDFbyte,
        file_name="Testing of Electrical Energy Meters Subject to Realistic Distorted Voltages and Currents.pdf",
        mime="application/pdf"
    )
    
    
    st.markdown("""
    17. Passed energy values through a **Gaussian Noise Model**  
    18. Working on optimized regression solution with **MSE ≈ 1.0233 × 10⁻³** and **R² ≈ 0.99** (based on *"Estimation of Total Real and Reactive Power Losses in Electrical"*)  
    """)
    # Add clickable link to PDF (opens in new tab)
    with open("Estimation of Total Real and Reactive Power Losses in Electrical.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 See Paper",
        data=PDFbyte,
        file_name="Estimation of Total Real and Reactive Power Losses in Electrical.pdf",
        mime="application/pdf"
    )

    st.title("You can check the Trained Model Performance Tab above")
# -------------------------------
# TAB 4: Trained Model Performance
# -------------------------------
with tab4:
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

            st.dataframe(sorted_df.head(5), use_container_width=True)

    except FileNotFoundError:
        st.error("⚠️ The file `Merged_All_ML_and_DL_Results.xlsx` was not found. Please upload it.")
    except Exception as e:
        st.error(f"⚠️ An error occurred while loading the data: {e}")
