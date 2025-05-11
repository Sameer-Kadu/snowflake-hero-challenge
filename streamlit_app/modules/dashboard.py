import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import snowflake.connector
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import json
import requests
from streamlit_folium import folium_static
import folium
from styles.custom_css import apply_custom_css

# Load data (either from Snowflake or mock data)
@st.cache_data
def load_data():
    # Uncomment to use actual Snowflake connection
    # tourism_df = run_query("SELECT * FROM tourism_stats")
    # cultural_sites_df = run_query("SELECT * FROM cultural_sites")
    
    # Using mock data for demo
    tourism_df = get_mock_data("tourism_stats")
    cultural_sites_df = get_mock_data("cultural_sites")
    
    return tourism_df, cultural_sites_df

# Load the data
tourism_df, cultural_sites_df = load_data()

def dashboard():
    # Header
    st.markdown("<h1 class='main-header'>India's Cultural Treasure Map</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Explore India's rich artistic heritage and tourism landscape</p>", unsafe_allow_html=True)
        
    # Overview stats in a 3-column layout
    col1, col2, col3 = st.columns(3)

    # Calculate overall stats
    total_domestic = tourism_df[tourism_df['CATEGORY'] == 'Domestic']['VISITORS'].sum()
    total_foreign = tourism_df[tourism_df['CATEGORY'] == 'Foreign']['VISITORS'].sum()
    total_cultural_sites = len(cultural_sites_df)

    with col1:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-value'>{:,}</div>
            <div class='stat-label'>Domestic Tourists</div>
        </div>
        """.format(total_domestic), unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-value'>{:,}</div>
            <div class='stat-label'>Foreign Tourists</div>
        </div>
        """.format(total_foreign), unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='stat-card'>
            <div class='stat-value'>{}</div>
            <div class='stat-label'>Cultural Sites</div>
        </div>
        """.format(total_cultural_sites), unsafe_allow_html=True)

    st.markdown("---")

    # Interactive map and summary tabs
    tab1, tab2 = st.tabs(["📊 Tourism Overview", "🗺️ Cultural Map"])

    with tab1:
        # Tourism summary and visualizations
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("<h3 class='section-title'>Tourism Statistics by State</h3>", unsafe_allow_html=True)

            # Group data by state and category
            tourism_by_state = tourism_df.groupby(['STATE_NAME', 'CATEGORY'])['VISITORS'].sum().reset_index()

            # Create a grouped bar chart
            fig = px.bar(
                tourism_by_state,
                x='STATE_NAME',
                y='VISITORS',
                color='CATEGORY',
                title="Tourist Visitors by State and Type",
                labels={'VISITORS': 'Number of Visitors', 'STATE_NAME': 'State', 'CATEGORY': 'Tourist Type'},
                color_discrete_map={'Domestic': '#FF9E44', 'Foreign': '#138086'},
                barmode='group',
                height=400
            )

            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif"),
                margin=dict(l=40, r=40, t=60, b=60),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("<h3 class='section-title'>Monthly Distribution</h3>", unsafe_allow_html=True)

            # Group data by month
            tourism_by_month = tourism_df.groupby('MONTH')['VISITORS'].sum().reset_index()

            # Ensure correct month ordering
            month_order = ['January', 'February', 'March']
            tourism_by_month['MONTH'] = pd.Categorical(tourism_by_month['MONTH'], categories=month_order, ordered=True)
            tourism_by_month = tourism_by_month.sort_values('MONTH')

            # Create a line chart
            fig = px.line(
                tourism_by_month,
                x='MONTH',
                y='VISITORS',
                markers=True,
                line_shape='spline',
                labels={'VISITORS': 'Total Visitors', 'MONTH': 'Month'},
                height=350
            )

            fig.update_traces(line=dict(color='#E25822', width=3))

            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif"),
                margin=dict(l=20, r=20, t=20, b=20)
            )

            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("<h3 class='section-title'>Cultural Sites Across India</h3>", unsafe_allow_html=True)

        # Create a folium map
        m = folium.Map(location=[23.0, 80.0], zoom_start=5, tiles='CartoDB positron')

        # Add markers for each cultural site
        for idx, row in cultural_sites_df.iterrows():
            # Create popup content
            popup_content = f"""
            <div style='width: 200px;'>
                <h4>{row['NAME']}</h4>
                <p><b>Region:</b> {row['REGION']}</p>
                <p><b>Type:</b> {row['ART_TYPE']}</p>
                <p>{row['DESCRIPTION'][:100]}...</p>
            </div>
            """

            # Add marker with popup
            folium.Marker(
                location=[row['LATITUDE'], row['LONGITUDE']],
                popup=folium.Popup(popup_content, max_width=300),
                tooltip=row['NAME'],
                icon=folium.Icon(icon='info-sign', prefix='fa', color='orange')
            ).add_to(m)

        # Display the map
        folium_static(m, width=800, height=500)

    # Featured content (cultural sites spotlight)
    st.markdown("<h3 class='section-title'>Featured Cultural Experiences</h3>", unsafe_allow_html=True)

    featured_sites = cultural_sites_df.sample(n=3).reset_index(drop=True)

    # Display featured sites in 3 columns
    cols = st.columns(3)
    for i, (idx, site) in enumerate(featured_sites.iterrows()):
        with cols[i]:
            st.markdown(f"""
            <div class='site-card hover-zoom'>
                <h4>{site['NAME']}</h4>
                <p><b>Region:</b> {site['REGION']}</p>
                <p><b>Type:</b> {site['ART_TYPE']}</p>
                <p>{site['DESCRIPTION'][:100]}...</p>
            </div>
            """, unsafe_allow_html=True)

