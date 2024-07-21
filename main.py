import streamlit as st


# First Page setup
def page_overview():
    st.subheader("Global Asylum Decisions by Year Range (Choose Range)")
    # data viz code below


# Second Page setup - country specific with barchart
def page_country_analysis():
    st.subheader("Country Analysis")
    # data viz code below

# Third Page setup - choropleth map
def page_choropleth():
    st.subheader("Global Distribution of asylum decisions")
    # data viz code below


# Main app with navigation
def main():
    st.set_page_config(page_title="Asylum Decisions Dashboard", layout="wide", initial_sidebar_state="expanded", page_icon="🌍")
    
    st.sidebar.title("Navigation")
    menu_options = ["Global Asylum Decisions", "Country Analysis", "Global Mapping"]
    menu_choice = st.sidebar.selectbox("Go To", menu_options)
    
    if menu_choice == "Global Asylum Decisions":
        page_overview() 
    elif menu_choice == "Country Analysis":
        page_country_analysis()
    elif menu_choice == "Global Mapping":
        page_choropleth()


if __name__ == "__main__":
    main()
