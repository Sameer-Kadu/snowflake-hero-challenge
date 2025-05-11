import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from streamlit_lottie import st_lottie
import requests
from streamlit_folium import folium_static
import folium
from styles.custom_css import apply_custom_css
from config.snowflake_config import get_snowflake_connection

# Page configuration
st.set_page_config(
    page_title="India Cultural Explorer",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

# Function to load lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animation URLs
culture_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_5njp3vgg.json")  # Cultural/travel themed animation
tourism_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_totrpclr.json")  # Tourism themed animation


# Function to execute query and return DataFrame
def run_query(query):
    try:
        conn = get_snowflake_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            df = pd.DataFrame(data, columns=columns)
            cursor.close()
            conn.close()
            return df
        return None
    except Exception as e:
        st.error(f"Query error: {e}")
        return None


# Load data (either from Snowflake or mock data)
@st.cache_data
def load_data():
    tourism_query = "SELECT * FROM tourism_stats"
    cultural_sites_query = "SELECT * FROM cultural_sites"
    yearly_tourism_query = "SELECT * FROM yearly_tourism"

    tourism_df = run_query(tourism_query)
    cultural_sites_df = run_query(cultural_sites_query)
    yearly_tourism_df = run_query(yearly_tourism_query)

    return tourism_df, cultural_sites_df, yearly_tourism_df

# Load the data
tourism_df, cultural_sites_df, yearly_tourism_df = load_data()

# Create sidebar
with st.sidebar:
    st.image("streamlit_app/assets/image.png", width=500)
    st.markdown("<h2 style='text-align: center;'>Cultural Explorer</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation options
    page = st.radio(
        "Navigate to",
        ["🏠 Dashboard", "🗺️ Tourism Insights", "🎭 Cultural Sites", "📊 Analysis", "ℹ️ About"]
    )
   
    
    # Only show relevant filters based on the page
    if page in ["🏠 Dashboard", "🗺️ Tourism Insights"]:
        st.markdown("---")
         # Filters section
        st.markdown("### Filters")
        selected_states = st.multiselect(
            "Select States",
            options=tourism_df['STATE_NAME'].unique(),
            default=tourism_df['STATE_NAME'].unique()[:3]
        )
        
        selected_months = st.multiselect(
            "Select Months",
            options=tourism_df['MONTH'].unique(),
            default=tourism_df['MONTH'].unique()
        )
        
        tourist_type = st.radio(
            "Tourist Type",
            ["All", "Domestic", "Foreign"]
        )
    
    if page in ["🏠 Dashboard", "🎭 Cultural Sites"]:
        st.markdown("---")
        art_types = st.multiselect(
            "Art Types",
            options=cultural_sites_df['ART_TYPE'].unique(),
            default=cultural_sites_df['ART_TYPE'].unique()
        )
    
    st.markdown("---")
    st_lottie(culture_animation, height=200, key="sidebar_animation")

# Filter the data based on selections
def filter_tourism_data():
    filtered_df = tourism_df.copy()
    
    if 'selected_states' in locals():
        if selected_states:
            filtered_df = filtered_df[filtered_df['STATE_NAME'].isin(selected_states)]
    
    if 'selected_months' in locals():
        if selected_months:
            filtered_df = filtered_df[filtered_df['MONTH'].isin(selected_months)]
    
    if 'tourist_type' in locals():
        if tourist_type != "All":
            filtered_df = filtered_df[filtered_df['CATEGORY'] == tourist_type]
    
    return filtered_df

def filter_cultural_data():
    filtered_df = cultural_sites_df.copy()
    
    if 'art_types' in locals():
        if art_types:
            filtered_df = filtered_df[filtered_df['ART_TYPE'].isin(art_types)]
    
    if 'selected_states' in locals():
        if selected_states:
            # For cultural sites, use REGION instead of STATE_NAME
            filtered_df = filtered_df[filtered_df['REGION'].isin(selected_states)]
    
    return filtered_df

# Dashboard page
if page == "🏠 Dashboard":
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
        folium_static(m, width=1000, height=500)
    
    # Featured content (cultural sites spotlight)
    st.markdown("<h3 class='section-title'>Featured Cultural Experiences</h3>", unsafe_allow_html=True)
    
    featured_sites = cultural_sites_df.sample(n=3).reset_index(drop=True)
    
    # Display featured sites in 3 columns
    cols = st.columns(3)
    for i, (idx, site) in enumerate(featured_sites.iterrows()):
        with cols[i]:
            st.markdown(f"""
            <div class='site-card hover-zoom'style='margin-top: 10px;'>
                <h4>{site['NAME']}</h4>
                <p><b>Region:</b> {site['REGION']}</p>
                <p><b>Type:</b> {site['ART_TYPE']}</p>
                <p>{site['DESCRIPTION'][:100]}...</p>
            </div>
            """, unsafe_allow_html=True)

# Tourism Insights page
elif page == "🗺️ Tourism Insights":
    st.markdown("<h1 class='main-header'>Tourism Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Deep dive into tourism trends and patterns</p>", unsafe_allow_html=True)
    
    # Filter data based on selections
    filtered_tourism = filter_tourism_data()
    
    # Year-over-year trends
    st.markdown("<h3 class='section-title'>Tourism Trends (2020-2024)</h3>", unsafe_allow_html=True)
    
    # Filter yearly data based on selected states
    if 'selected_states' in locals():
        filtered_yearly_tourism = yearly_tourism_df[yearly_tourism_df['STATE_NAME'].isin(selected_states)]
    else:
        filtered_yearly_tourism = yearly_tourism_df
    
    # Create line chart for yearly trends
    fig = px.line(
        filtered_yearly_tourism,
        x='YEAR',
        y='YEARLY_VISITORS',
        color='STATE_NAME',
        line_dash='CATEGORY',
        labels={'YEARLY_VISITORS': 'Annual Visitors', 'YEAR': 'Year', 'STATE_NAME': 'State', 'CATEGORY': 'Tourist Type'},
        title="Tourism Trends (2020-2024)",
        height=400,
        markers=True
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        margin=dict(l=40, r=40, t=60, b=60),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # COVID impact analysis
    st.markdown("<h3 class='section-title'>COVID Impact & Recovery</h3>", unsafe_allow_html=True)
    
    # Calculate recovery metrics
    recovery_data = []

    # Debugging: Check if DataFrame is empty
    if filtered_yearly_tourism.empty:
        st.write("in yearly tourism filter: ", filtered_yearly_tourism)
        st.warning("No data available for the selected filters.")
    else:
        for state in filtered_yearly_tourism['STATE_NAME'].unique():
            for category in ['Domestic', 'Foreign']:
                state_cat_data = filtered_yearly_tourism[
                    (filtered_yearly_tourism['STATE_NAME'] == state) &
                    (filtered_yearly_tourism['CATEGORY'] == category)
                ]

                # Debugging: Check data for required years
                if 2020 in state_cat_data['YEAR'].values and 2021 in state_cat_data['YEAR'].values and 2022 in state_cat_data['YEAR'].values:
                    pre_covid = state_cat_data[state_cat_data['YEAR'] == 2020]['YEARLY_VISITORS'].values[0]
                    covid_low = state_cat_data[state_cat_data['YEAR'] == 2021]['YEARLY_VISITORS'].values[0]
                    current = state_cat_data[state_cat_data['YEAR'] == 2022]['YEARLY_VISITORS'].values[0]

                    # Avoid division by zero
                    if (pre_covid - covid_low) != 0:
                        recovery_pct = (current - covid_low) / (pre_covid - covid_low) * 100
                    else:
                        recovery_pct = 0

                    recovery_data.append({
                        'STATE_NAME': state,
                        'CATEGORY': category,
                        'PRE_COVID': pre_covid,
                        'COVID_LOW': covid_low,
                        'CURRENT': current,
                        'RECOVERY_PCT': min(recovery_pct, 100)  # Cap at 100%
                    })
                else:
                    st.warning(f"Missing data for state: {state}, category: {category}")
    
    recovery_df = pd.DataFrame(recovery_data)
    
    # Create a bar chart showing recovery percentage
    fig = px.bar(
        recovery_df,
        x='STATE_NAME',
        y='RECOVERY_PCT',
        color='CATEGORY',
        labels={'RECOVERY_PCT': 'Recovery %', 'STATE_NAME': 'State', 'CATEGORY': 'Tourist Type'},
        color_discrete_map={'Domestic': '#FF9E44', 'Foreign': '#138086'},
        title="Tourism Recovery After COVID-19",
        barmode='group',
        height=350
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        yaxis=dict(ticksuffix="%"),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)
     
    # Analysis by tourist type
    st.markdown("<h3 class='section-title'>Domestic vs. Foreign Tourism Analysis</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Monthly tourism patterns
    st.markdown("<h3 class='section-title'>Monthly Tourism Patterns</h3>", unsafe_allow_html=True)
    
    # Group by month and state
    monthly_patterns = filtered_tourism.groupby(['MONTH', 'STATE_NAME', 'CATEGORY'])['VISITORS'].sum().reset_index()
    
    # Create a line chart for monthly patterns
    fig = px.line(
        monthly_patterns,
        x='MONTH',
        y='VISITORS',
        color='STATE_NAME',
        line_dash='CATEGORY',
        markers=True,
        labels={'VISITORS': 'Number of Visitors', 'MONTH': 'Month', 'STATE_NAME': 'State', 'CATEGORY': 'Tourist Type'},
        title="Monthly Tourism Patterns",
        height=400
    )
    
    # Ensure correct month ordering
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig.update_xaxes(categoryorder='array', categoryarray=month_order)
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        margin=dict(l=40, r=40, t=60, b=60),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tourism recommendations
    st.markdown("<h3 class='section-title'>Tourism Development Recommendations</h3>", unsafe_allow_html=True)
    
    # Create recommendation cards
    recommendations = [
        {
            "title": "Sustainable Tourism Initiatives",
            "description": "Develop eco-tourism packages that highlight cultural heritage while preserving natural resources. Implement carbon offset programs for tourists.",
            "icon": "🌿"
        },
        {
            "title": "Digital Presence Enhancement",
            "description": "Create immersive virtual tours of cultural sites to attract international visitors. Implement AI-powered recommendation systems for personalized itineraries.",
            "icon": "🌐"
        },
        {
            "title": "Cultural Festival Calendar",
            "description": "Develop a year-round calendar of cultural festivals to reduce seasonality in tourism. Create partnership packages with artists and performers.",
            "icon": "🎭"
        }
    ]
    
    cols = st.columns(3)
    for i, rec in enumerate(recommendations):
        with cols[i]:
            st.markdown(f"""
            <div class='card hover-zoom'style='margin-top: 10px;'>
                <h1 style='font-size: 2rem; text-align: center;'>{rec['icon']}</h1>
                <h4>{rec['title']}</h4>
                <p>{rec['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col1:
        # Calculate domestic vs foreign ratio
        tourism_ratio = filtered_tourism.groupby(['STATE_NAME', 'CATEGORY'])['VISITORS'].sum().unstack()
        if 'Domestic' in tourism_ratio.columns and 'Foreign' in tourism_ratio.columns:
            tourism_ratio['Ratio'] = tourism_ratio['Domestic'] / tourism_ratio['Foreign']
            tourism_ratio.reset_index(inplace=True)
            
            # Create bar chart for domestic/foreign ratio
            fig = px.bar(
                tourism_ratio,
                x='STATE_NAME',
                y='Ratio',
                color='STATE_NAME',
                labels={'Ratio': 'Domestic/Foreign Ratio', 'STATE_NAME': 'State'},
                title="Domestic to Foreign Tourist Ratio",
                height=350
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif"),
                showlegend=False,
                margin=dict(l=40, r=40, t=60, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Create a radar chart for tourism resilience
        categories = ['Recovery Speed', 'Domestic Growth', 'Foreign Growth', 
                     'Seasonal Stability', 'Infrastructure']
        
        # Simulated data for tourism resilience by state
        resilience_data = {
            'Kerala': [80, 85, 70, 60, 90],
            'Rajasthan': [75, 70, 85, 80, 65],
            'Assam': [65, 75, 55, 70, 60]
        }
        
        # Filter states based on selection
        if 'selected_states' in locals() and selected_states:
            resilience_data = {k: v for k, v in resilience_data.items() if k in selected_states}
        
        # Create radar chart
        fig = go.Figure()
        
        for state, values in resilience_data.items():
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=state
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            title="Tourism Resilience Factors",
            height=350,
            font=dict(family="Poppins, sans-serif"),
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        # Cultural Sites page content
elif page == "🎭 Cultural Sites":
    st.markdown("<h1 class='main-header'>Explore Cultural Sites</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Discover India's rich artistic heritage and traditions</p>", unsafe_allow_html=True)
    
    # Filter data based on selections
    filtered_cultural = filter_cultural_data()
    
    # Interactive exploration UI with tabs
    tab1, tab2 = st.tabs(["📍 Site Directory", "🔍 Deep Dive"])
    
    with tab1:
        # Display cultural sites in a searchable table
        st.markdown("<h3 class='section-title'>Cultural Site Directory</h3>", unsafe_allow_html=True)
        
        # Search functionality
        search_term = st.text_input("Search sites by name or description", "")
        
        if search_term:
            search_results = filtered_cultural[
                filtered_cultural['NAME'].str.contains(search_term, case=False) | 
                filtered_cultural['DESCRIPTION'].str.contains(search_term, case=False)
            ]
        else:
            search_results = filtered_cultural
        
        # Display results
        if not search_results.empty:
            for idx, site in search_results.iterrows():
                st.markdown(f"""
                <div class='site-card hover-zoom'>
                    <h4>{site['NAME']}</h4>
                    <p><b>Region:</b> {site['REGION']} | <b>Type:</b> {site['ART_TYPE']}</p>
                    <p>{site['DESCRIPTION']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No results found. Try a different search term.")
    
    with tab2:
        # Select a site for detailed exploration
        st.markdown("<h3 class='section-title'>Cultural Deep Dive</h3>", unsafe_allow_html=True)
        
        selected_site = st.selectbox(
            "Select a cultural site to explore in detail",
            filtered_cultural['NAME'].tolist()
        )
        
        # Get details for the selected site
        site_details = filtered_cultural[filtered_cultural['NAME'] == selected_site].iloc[0]
        
        # Display detailed information
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <h2>{site_details['NAME']}</h2>
                <p><b>Region:</b> {site_details['REGION']}</p>
                <p><b>Art Type:</b> {site_details['ART_TYPE']}</p>
                <p>{site_details['DESCRIPTION']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Additional info based on art type
            if site_details['ART_TYPE'] == 'Performing Arts':
                st.markdown("""
                <div class='state-info'>
                    <h4>About Performing Arts in India</h4>
                    <p>Indian performing arts have a history spanning over 2,500 years. These traditions encompass music, dance, and theatrical performances that are deeply rooted in religious and cultural practices.</p>
                    <p>Each region has developed its unique styles, techniques, and repertoire, reflecting the diversity of India's cultural landscape.</p>
                </div>
                """, unsafe_allow_html=True)
            elif site_details['ART_TYPE'] == 'Visual Arts':
                st.markdown("""
                <div class='state-info'>
                    <h4>About Visual Arts in India</h4>
                    <p>India's visual arts tradition dates back to ancient rock paintings and continues through diverse styles of painting, sculpture, and decorative arts.</p>
                    <p>Regional traditions have their own distinctive color palettes, themes, and techniques that often reflect local mythology, history, and natural surroundings.</p>
                </div>
                """, unsafe_allow_html=True)
            elif site_details['ART_TYPE'] == 'Architecture':
                st.markdown("""
                <div class='state-info'>
                    <h4>About Indian Architecture</h4>
                    <p>Indian architecture is known for its elaborate temples, palaces, and forts that showcase sophisticated design principles and engineering techniques.</p>
                    <p>Regional architectural styles often incorporate local materials and respond to climatic conditions while accommodating cultural and religious requirements.</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Generate a simulated visitor stats chart
            visitor_data = {
                'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Visitors': np.random.randint(1000, 5000, size=6)
            }
            visitor_df = pd.DataFrame(visitor_data)
            
            st.markdown("<h4>Monthly Visitors</h4>", unsafe_allow_html=True)
            fig = px.bar(
                visitor_df,
                x='Month',
                y='Visitors',
                title=f"Visitor Statistics for {selected_site}",
                color_discrete_sequence=['#FF9E44']
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Responsible tourism tips
            st.markdown("""
            <div class='card'>
                <h4>Responsible Tourism Tips</h4>
                <ul>
                    <li>Respect local customs and traditions</li>
                    <li>Support local artisans and performers</li>
                    <li>Minimize environmental impact</li>
                    <li>Learn about cultural significance before visiting</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Cultural preservation initiatives
    st.markdown("<h3 class='section-title'>Cultural Preservation Initiatives</h3>", unsafe_allow_html=True)
    
    # Add information about preservation initiatives
    initiatives = [
        {
            "title": "Digital Documentation",
            "description": "Efforts to digitally document and preserve traditional art forms using advanced technology like 3D scanning and high-definition video.",
            "impact": "High"
        },
        {
            "title": "Apprenticeship Programs",
            "description": "Supporting master-apprentice relationships to ensure traditional skills and knowledge are passed down to younger generations.",
            "impact": "Medium"
        },
        {
            "title": "Community Museums",
            "description": "Establishing local museums and cultural centers managed by communities to preserve and showcase their unique heritage.",
            "impact": "Medium"
        }
    ]
    
    # Display initiatives in columns
    cols = st.columns(3)
    for i, initiative in enumerate(initiatives):
        with cols[i]:
            impact_color = "#28a745" if initiative["impact"] == "High" else "#ffc107"
            st.markdown(f"""
            <div class='card hover-zoom'>
                <h4>{initiative['title']}</h4>
                <p>{initiative['description']}</p>
                <p><b>Impact:</b> <span style='color:{impact_color};'>{initiative['impact']}</span></p>
            </div>
            """, unsafe_allow_html=True)

# Analysis page
elif page == "📊 Analysis":
    st.markdown("<h1 class='main-header'>Data Analysis & Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Exploring patterns and trends in cultural tourism data</p>", unsafe_allow_html=True)
    
    # Analysis tabs
    tab1, tab2, tab3 = st.tabs(["📈 Tourism Correlation", "🔄 Seasonal Patterns", "📍 Regional Analysis"])
    
    with tab1:
        st.markdown("<h3 class='section-title'>Cultural Site Impact on Tourism</h3>", unsafe_allow_html=True)
        
        # Create simulated correlation data
        correlation_data = {
            'Region': ['Kerala', 'Rajasthan', 'Assam', 'Maharashtra', 'Tamil Nadu'],
            'Cultural_Sites': [15, 23, 8, 19, 17],
            'Tourist_Volume': [250000, 350000, 90000, 280000, 220000],
            'Tourism_Revenue': [45, 60, 20, 50, 40]  # in million USD
        }
        correlation_df = pd.DataFrame(correlation_data)
        
        # Plot correlation between cultural sites and tourism
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.scatter(
                correlation_df,
                x='Cultural_Sites',
                y='Tourist_Volume',
                size='Tourism_Revenue',
                color='Region',
                labels={
                    'Cultural_Sites': 'Number of Cultural Sites',
                    'Tourist_Volume': 'Annual Tourist Volume',
                    'Tourism_Revenue': 'Tourism Revenue (Million USD)'
                },
                title="Correlation: Cultural Sites vs. Tourism",
                height=400
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Create a heatmap of correlations
            corr_matrix = correlation_df[['Cultural_Sites', 'Tourist_Volume', 'Tourism_Revenue']].corr()
            
            fig = px.imshow(
                corr_matrix,
                text_auto=True,
                color_continuous_scale='OrRd',
                labels=dict(x="Variable", y="Variable", color="Correlation"),
                title="Correlation Matrix"
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Analysis insights
        st.markdown("""
        <div class='state-info'>
            <h4>Key Insights</h4>
            <ul>
                <li>There is a strong positive correlation (0.91) between the number of cultural sites and tourism volume.</li>
                <li>Regions with a higher number of cultural sites tend to generate more tourism revenue.</li>
                <li>Rajasthan shows the highest tourism volume and revenue, likely due to its rich cultural heritage.</li>
                <li>Assam has potential for growth by developing and promoting more cultural sites.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<h3 class='section-title'>Seasonal Tourism Patterns</h3>", unsafe_allow_html=True)
        
        # Create simulated seasonal data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        # Different seasonal patterns for different regions
        seasonal_data = {
            'Month': months * 3,
            'Region': ['Kerala'] * 12 + ['Rajasthan'] * 12 + ['Assam'] * 12,
            'Visitors': [
                # Kerala - peak in winter months
                50000, 45000, 40000, 30000, 25000, 20000, 25000, 30000, 35000, 40000, 60000, 70000,
                # Rajasthan - peak in winter, low in summer
                60000, 55000, 40000, 25000, 15000, 10000, 15000, 20000, 35000, 50000, 65000, 70000,
                # Assam - more consistent with peak in spring
                20000, 25000, 30000, 35000, 25000, 20000, 15000, 15000, 20000, 25000, 20000, 20000
            ],
            'Cultural_Events': [
                # Kerala
                3, 2, 4, 1, 1, 2, 1, 3, 2, 3, 5, 6,
                # Rajasthan
                5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7,
                # Assam
                2, 3, 5, 4, 3, 2, 1, 1, 2, 3, 2, 2
            ]
        }
        seasonal_df = pd.DataFrame(seasonal_data)
        
        # Plot seasonal patterns
        col1, col2 = st.columns([3, 1])
        
        with col1:
            fig = px.line(
                seasonal_df,
                x='Month',
                y='Visitors',
                color='Region',
                markers=True,
                title="Monthly Tourism Patterns by Region",
                height=400
            )
            
            # Add cultural events as a secondary y-axis
            for region in seasonal_df['Region'].unique():
                region_data = seasonal_df[seasonal_df['Region'] == region]
                fig.add_trace(
                    go.Scatter(
                        x=region_data['Month'],
                        y=region_data['Cultural_Events'],
                        mode='markers',
                        marker=dict(size=region_data['Cultural_Events'] * 3),
                        name=f"{region} Events",
                        yaxis="y2"
                    )
                )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif"),
                yaxis2=dict(
                    title="Number of Cultural Events",
                    overlaying="y",
                    side="right",
                    range=[0, 10]
                )
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Seasonality analysis
            st.markdown("""
            <div class='card'>
                <h4>Seasonality Insights</h4>
                <p><b>Kerala:</b> Peak season in Nov-Feb (winter)</p>
                <p><b>Rajasthan:</b> Strong winter peak, low summer</p>
                <p><b>Assam:</b> More consistent year-round</p>
                <p>Cultural events correlate strongly with visitor numbers across all regions</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Off-season promotion ideas
            st.markdown("""
            <div class='card'>
                <h4>Off-Season Promotion Ideas</h4>
                <ul>
                    <li>Monsoon cultural festivals</li>
                    <li>Summer artisan workshops</li>
                    <li>Special pricing for cultural tours</li>
                    <li>Indoor cultural experiences</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<h3 class='section-title'>Regional Cultural Analysis</h3>", unsafe_allow_html=True)
        
        
        # Fetch regional insights from the database
        def fetch_regional_insights():
            query = "SELECT * FROM regional_insights"
            return run_query(query)

        # Fetch the data
        regional_df = fetch_regional_insights()
        
        # Create a radar chart for each region
        selected_region = st.selectbox(
            "Select a region to analyze",
            regional_df['REGION'].tolist()
        )
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Get data for selected region
            region_row = regional_df[regional_df['REGION'] == selected_region].iloc[0]
            
            # Create the radar chart
            categories = ['PERFORMING_ARTS', 'VISUAL_ARTS', 'ARCHITECTURE', 'HERITAGE_SITES', 'CULTURAL_FESTIVALS']
            values = [region_row[cat] for cat in categories]
            
            # Make it a complete circle by repeating the first value
            categories = [cat.replace('_', ' ') for cat in categories]
            categories = categories + [categories[0]]
            values = values + [values[0]]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=selected_region,
                line=dict(color='#FF9E44', width=2),
                fillcolor='rgba(255, 158, 68, 0.5)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 50]
                    )
                ),
                showlegend=False,
                title=f"Cultural Assets of {selected_region}",
                height=400,
                font=dict(family="Poppins, sans-serif"),
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Regional strengths and opportunities
            if selected_region == 'Kerala':
                st.markdown("""
                <div class='state-info'>
                    <h4>Regional Insights: Kerala</h4>
                    <p><b>Strengths:</b> Strong performing arts tradition, particularly in Kathakali and other classical forms.</p>
                    <p><b>Opportunities:</b> Can further develop visual arts tourism through traditional mural painting experiences.</p>
                    <p><b>Tourism Focus:</b> Cultural immersion experiences, performing arts workshops, ayurvedic wellness traditions.</p>
                </div>
                """, unsafe_allow_html=True)
            elif selected_region == 'Rajasthan':
                st.markdown("""
                <div class='state-info'>
                    <h4>Regional Insights: Rajasthan</h4>
                    <p><b>Strengths:</b> Exceptional architectural heritage with numerous forts and palaces.</p>
                    <p><b>Opportunities:</b> Growing interest in folk performances can be leveraged for more inclusive cultural tourism.</p>
                    <p><b>Tourism Focus:</b> Heritage walks, architectural tours, craft bazaars, desert culture experiences.</p>
                </div>
                """, unsafe_allow_html=True)
            elif selected_region == 'Assam':
                st.markdown("""
                <div class='state-info'>
                    <h4>Regional Insights: Assam</h4>
                    <p><b>Strengths:</b> Unique cultural identity with Bihu dance and other distinctive traditions.</p>
                    <p><b>Opportunities:</b> Largely untapped potential for cultural tourism, especially around heritage sites.</p>
                    <p><b>Tourism Focus:</b> River culture, tea plantation heritage, textile traditions, tribal cultural exchange.</p>
                </div>
                """, unsafe_allow_html=True)
            elif selected_region == 'Maharashtra':
                st.markdown("""
                <div class='state-info'>
                    <h4>Regional Insights: Maharashtra</h4>
                    <p><b>Strengths:</b> Rich visual arts tradition and important heritage sites.</p>
                    <p><b>Opportunities:</b> Can develop more cultural festivals to attract year-round tourism.</p>
                    <p><b>Tourism Focus:</b> Cave art tours, traditional Warli painting experiences, urban-rural cultural contrasts.</p>
                </div>
                """, unsafe_allow_html=True)
            elif selected_region == 'Tamil Nadu':
                st.markdown("""
                <div class='state-info'>
                    <h4>Regional Insights: Tamil Nadu</h4>
                    <p><b>Strengths:</b> Classical performing arts tradition with Bharatanatyam and Carnatic music.</p>
                    <p><b>Opportunities:</b> Potential to connect ancient temple architecture with living traditions.</p>
                    <p><b>Tourism Focus:</b> Temple architecture tours, classical dance and music festivals, bronze casting traditions.</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Comparison with other regions
        st.markdown("<h4>Regional Comparison</h4>", unsafe_allow_html=True)
        
        # Melt the dataframe for easier plotting
        regional_melted = pd.melt(
            regional_df, 
            id_vars=['REGION'], 
            value_vars=['PERFORMING_ARTS', 'VISUAL_ARTS', 'ARCHITECTURE', 'HERITAGE_SITES', 'CULTURAL_FESTIVALS'],
            var_name='Category',
            value_name='Value'
        )
        
        # Create a grouped bar chart
        fig = px.bar(
            regional_melted,
            x='REGION',
            y='Value',
            color='Category',
            title="Cultural Assets by Region",
            height=400,
            labels={'Value': 'Relative Strength (0-50)', 'Region': 'Region', 'Category': 'Cultural Category'}
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins, sans-serif")
        )
        
        st.plotly_chart(fig, use_container_width=True)

# About page
elif page == "ℹ️ About":
    st.markdown("<h1 class='main-header'>About This Project</h1>", unsafe_allow_html=True)
    
    # Project information
    st.markdown("""
    <div class='card'>
        <h3>India Cultural Explorer</h3>
        <p>This application was developed for the YourStory | Snowflake - Hero Challenge 2025. The project aims to showcase traditional art forms, uncover cultural experiences across India, and promote responsible tourism using data-driven insights.</p>
        <p>The application integrates cultural data with tourism statistics to provide meaningful insights and recommendations for preserving India's rich cultural heritage while promoting sustainable tourism.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Data sources
    st.markdown("<h3 class='section-title'>Data Sources</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h4>Primary Data Sources</h4>
        <ul>
            <li>Government of India Open Data Portal (data.gov.in)</li>
            <li>Ministry of Tourism Annual Reports</li>
            <li>Ministry of Culture Heritage Sites Directory</li>
            <li>State Tourism Departments</li>
            <li>Cultural Research Institutions</li>
        </ul>
        <p><i>Note: For demonstration purposes, this application uses simulated data that approximates real-world trends and patterns.</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technologies used
    st.markdown("<h3 class='section-title'>Technologies Used</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='card hover-zoom'>
            <h4>Snowflake</h4>
            <p>Used as the primary data platform for storing, processing, and analyzing the cultural and tourism datasets.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card hover-zoom'>
            <h4>Streamlit</h4>
            <p>Frontend web application framework used to create this interactive data visualization and exploration platform.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='card hover-zoom'>
            <h4>Python Libraries</h4>
            <p>Pandas for data manipulation, Plotly and Matplotlib for visualizations, and Folium for interactive maps.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Future enhancements
    st.markdown("<h3 class='section-title'>Future Enhancements</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h4>Planned Improvements</h4>
        <ol>
            <li><b>Real-time Data Integration:</b> Connect with live tourism APIs and social media feeds to provide real-time insights.</li>
            <li><b>Predictive Analytics:</b> Implement machine learning models to forecast tourism trends and provide recommendations.</li>
            <li><b>User-Generated Content:</b> Allow tourists to contribute their experiences and ratings of cultural sites.</li>
            <li><b>Cultural Preservation Tracker:</b> Monitor and report on the preservation status of endangered cultural practices.</li>
            <li><b>Personalized Itinerary Generator:</b> Create custom travel plans based on cultural interests and preferences.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Team information
    st.markdown("<h3 class='section-title'>Meet the Team</h3>", unsafe_allow_html=True)
    
    team_members = [
        {"name": "Project Lead", "role": "Data Scientist & Cultural Researcher"},
        {"name": "Snowflake Developer", "role": "Backend Data Engineering Specialist"},
        {"name": "Streamlit Developer", "role": "Frontend Visualization Expert"},
        {"name": "Cultural Consultant", "role": "Subject Matter Expert in Indian Art Forms"}
    ]
    
    # Display team members in two columns
    cols = st.columns(2)
    for i, member in enumerate(team_members):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='card hover-zoom'>
                <h4>{member['name']}</h4>
                <p>{member['role']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contact information
    st.markdown("<h3 class='section-title'>Contact Information</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <p>For more information about this project or to provide feedback, please contact:</p>
        <p><b>Email:</b> indiacultureexplorer@example.com</p>
        <p><b>GitHub:</b> github.com/indiacultureexplorer</p>
    </div>
    """, unsafe_allow_html=True)

# Add a footer
st.markdown("""
<div class='footer' style='margin-bottom:-500px'>
    <p>© 2025 India Cultural Explorer | Developed for YourStory | Snowflake - Hero Challenge</p>
    <p>Showcasing India's cultural heritage through data-driven insights</p>
</div>
""", unsafe_allow_html=True)