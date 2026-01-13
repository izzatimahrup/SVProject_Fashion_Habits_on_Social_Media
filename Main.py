import streamlit as st

st.set_page_config(
    page_title="Fashion Shopping Behaviour Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------------
# Define Pages
# ---------------------------------------------------------

HomePage = st.Page(
    "HomePage.py",
    title="Home",
    icon="🏠",
    default=True
)

Izzati = st.Page(
    "Izzati.py",
    title="Demographic Information",
    icon="👥"
)

Hanis = st.Page(
    "Hanis.py",
    title="Consumer Behaviour on Social Media",
    icon="📱"
)

Syadira = st.Page(
    "Syadira.py",
    title="Consumer Interest in Fashion",
    icon="👗"
)

Aina = st.Page(
    "Aina.py",
    title="Motivation to Follow Fashion Brand",
    icon="🎯"
)

# ---------------------------------------------------------
# Navigation Menu
# ---------------------------------------------------------

pg = st.navigation(
    {
        "Main Menu": [
            HomePage,
            Izzati,
            Hanis,
            Syadira,
            Aina
        ]
    }
)

pg.run()
