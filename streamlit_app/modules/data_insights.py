import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
from io import StringIO
import folium
from streamlit_folium import folium_static

# Function to fetch data from data.gov.in APIs
def fetch_data_gov_api(api_url):
    """
    Fetches data from data.gov.in APIs
    Returns a pandas DataFrame or None if the request fails
    """
    try:
        # Add API key if not already in the URL
        if "api-key=" not in api_url:
            api_url += "&api-key=YOUR_API_KEY" if "?" in api_url else "?api-key=YOUR_API_KEY"
        
        # Add format parameter if not already in the URL
        if "format=" not in api_url:
            api_url += "&format=json"
        
        # Make the request
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Try to parse response based on content type
            content_type = response.headers.get('content-type', '')
            
            # Process JSON response
            if 'json' in content_type:
                json_data = response.json()
                
                # Check if response contains records
                if 'records' in json_data and isinstance(json_data['records'], list):
                    if len(json_data['records']) > 0:
                        try:
                            # Handle non-uniform records
                            records = json_data['records']
                            
                            # Find all possible keys across all records
                            all_keys = set()
                            for record in records:
                                all_keys.update(record.keys())
                            
                            # Create normalized records with all fields
                            normalized_records = []
                            for record in records:
                                normalized_record = {key: record.get(key, None) for key in all_keys}
                                normalized_records.append(normalized_record)
                            
                            return pd.DataFrame(normalized_records)
                        except Exception as e:
                            st.error(f"Error normalizing API data: {e}")
                            
                            # Last resort: try to load data one record at a time
                            try:
                                df_list = []
                                for record in records:
                                    df_list.append(pd.DataFrame([record]))
                                if df_list:
                                    return pd.concat(df_list, ignore_index=True)
                                return None
                            except:
                                return None
                    else:
                        st.warning(f"API returned zero records: {json_data.get('message', 'No message')}")
                        return None
                # Try direct conversion if no 'records' field
                else:
                    try:
                        # Try different approaches to parse the data
                        if isinstance(json_data, dict):
                            # If it's just a dict, convert to DataFrame directly
                            return pd.DataFrame([json_data])
                        elif isinstance(json_data, list):
                            # If it's a list, convert directly
                            return pd.DataFrame(json_data)
                        else:
                            st.error(f"Unexpected JSON structure: {type(json_data)}")
                            return None
                    except Exception as inner_e:
                        st.error(f"Error converting JSON to DataFrame: {inner_e}")
                        # Print the structure to help debug
                        st.code(f"JSON structure: {str(json_data)[:500]}...")
                        return None
                    
            elif 'csv' in content_type:
                return pd.read_csv(StringIO(response.text))
            else:
                st.error(f"Unsupported content type: {content_type}")
                return None
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching API data: {e}")
        # Print additional debug info
        st.code(f"API URL: {api_url}")
        return None

# Function to load cached data or fallback to mock data
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_api_data(api_url, mock_data_path=None):
    """
    Attempts to load data from the API, falls back to mock data if API fails
    """
    # First try the API
    df = fetch_data_gov_api(api_url)
    
    # # Log what happened
    # if df is not None:
    #     st.success(f"Successfully loaded {len(df)} records from API")
    # else:
    #     st.warning("Could not load data from API, falling back to mock data")
    
    # If API fails and mock data is provided, use mock data
    if df is None and mock_data_path:
        try:
            if mock_data_path.endswith('.csv'):
                df = pd.read_csv(mock_data_path)
            elif mock_data_path.endswith('.json'):
                df = pd.read_json(mock_data_path)
        except Exception as e:
            st.error(f"Error loading mock data: {e}")
            return None
    
    return df

# Heritage Sites Data
def load_heritage_sites_data():
    # API URL for heritage sites
    api_url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001603d17f141f643e07a5be86c67b2f7b6&format=json&limit=1000"
    
    # Mock data path (fallback)
    mock_data_path = "data/mock_heritage_sites.csv"
    
    # Load data
    return load_api_data(api_url, mock_data_path)

# Tourist Visits Data
def load_tourist_visits_data():
    """
    Fetches and transforms tourist visits data from data.gov.in API
    """
    api_url = "https://api.data.gov.in/resource/1d118b7d-e870-4666-b77b-9ff823382494?api-key=579b464db66ec23bdd000001603d17f141f643e07a5be86c67b2f7b6&format=json&limit=100000"
    
    df = fetch_data_gov_api(api_url)
    
    if df is not None and not df.empty:
        # Transform the data from wide to long format
        transformed_data = []
        
        for _, row in df.iterrows():
            # 2016 data
            transformed_data.append({
                'state': row['states'],
                'year': 2016,
                'domestic_tourists': row['_2016___dtv'],
                'foreign_tourists': row['_2016___ftv']
            })
            
            # 2017 data
            transformed_data.append({
                'state': row['states'],
                'year': 2017,
                'domestic_tourists': row['_2017___dtv'],
                'foreign_tourists': row['_2017___ftv']
            })
            
            # 2018 data
            transformed_data.append({
                'state': row['states'],
                'year': 2018,
                'domestic_tourists': row['_2018__revised____dtv'],
                'foreign_tourists': row['_2018__revised____ftv']
            })
        
        return pd.DataFrame(transformed_data)
    
    # If API fails, use mock data
    mock_data_path = "data/mock_tourist_visits.csv"
    try:
        return pd.read_csv(mock_data_path)
    except Exception as e:
        st.error(f"Error loading mock data: {e}")
        return None

# Performing Arts Data
def load_performing_arts_data():
    # API URL for performing arts
    api_url = "https://api.data.gov.in/resrce/1d118b7d-e870-4666-b77b-9ff823382494?api-key=579b464db66ec23bdd000001603d17f141f643e07a5be86c67b2f7b6&format=json&limit=100"
    
    # Mock data path (fallback)
    mock_data_path = "data/mock_performing_arts.csv"
    
    # Load data
    return load_api_data(api_url, mock_data_path)

# Visualization functions
def visualize_heritage_sites(heritage_df):
    """
    Creates visualizations for heritage sites data
    """
    if heritage_df is None or heritage_df.empty:
        st.warning("No heritage sites data available. Using mock data for visualization.")
        # Generate simple mock data for visualization
        heritage_df = pd.DataFrame({
            'site_name': [
                'Taj Mahal', 'Red Fort', 'Qutub Minar', 'Ajanta Caves', 'Ellora Caves',
                'Sun Temple', 'Khajuraho Temples', 'Mahabalipuram', 'Hampi', 'Fatehpur Sikri'
            ],
            'site_type': [
                'Monument', 'Fort', 'Monument', 'Cave', 'Cave',
                'Temple', 'Temple', 'Temple', 'Archaeological Site', 'Historical City'
            ],
            'state': [
                'Uttar Pradesh', 'Delhi', 'Delhi', 'Maharashtra', 'Maharashtra',
                'Odisha', 'Madhya Pradesh', 'Tamil Nadu', 'Karnataka', 'Uttar Pradesh'
            ],
            'latitude': [
                27.1751, 28.6562, 28.5245, 20.5519, 20.0258,
                19.8876, 24.8318, 12.6269, 15.3350, 27.0940
            ],
            'longitude': [
                78.0421, 77.2410, 77.1855, 75.7003, 75.1772,
                85.8513, 79.9199, 80.1928, 76.4600, 77.6710
            ]
        })
    
    st.markdown("<h3 class='section-title'>Heritage Sites Analysis</h3>", unsafe_allow_html=True)
    
    # Map of heritage sites
    st.markdown("<h4>Geographic Distribution of Heritage Sites</h4>", unsafe_allow_html=True)
    
    # Create a Folium map
    m = folium.Map(location=[23.0, 80.0], zoom_start=5, tiles='CartoDB positron')
    
    # Add markers for each heritage site
    for idx, row in heritage_df.iterrows():
        # Check if latitude and longitude columns exist and are valid
        if 'latitude' in heritage_df.columns and 'longitude' in heritage_df.columns:
            lat, lon = row['latitude'], row['longitude']
            if pd.notna(lat) and pd.notna(lon):
                # Create popup content
                site_name = row.get('site_name', 'Unknown Site')
                site_type = row.get('site_type', 'Not specified')
                state = row.get('state', 'Unknown location')
                
                popup_content = f"""
                <div style='width: 200px;'>
                    <h4>{site_name}</h4>
                    <p><b>Type:</b> {site_type}</p>
                    <p><b>State:</b> {state}</p>
                </div>
                """
                
                # Add marker with popup
                folium.Marker(
                    location=[lat, lon],
                    popup=folium.Popup(popup_content, max_width=300),
                    tooltip=site_name,
                    icon=folium.Icon(icon='info-sign', prefix='fa', color='orange')
                ).add_to(m)
    
    # Display the map
    folium_static(m, width=1000, height=500)
    
    # Additional visualizations based on available columns
    if 'state' in heritage_df.columns:
        # Sites by state bar chart
        sites_by_state = heritage_df['state'].value_counts().reset_index()
        sites_by_state.columns = ['State', 'Number of Sites']
        
        fig = px.bar(
            sites_by_state.head(10),
            x='State',
            y='Number of Sites',
            title="Top 10 States by Number of Heritage Sites",
            color='Number of Sites',
            color_continuous_scale='Oranges',
            height=400
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins, sans-serif")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    if 'site_type' in heritage_df.columns:
        # Sites by type pie chart
        sites_by_type = heritage_df['site_type'].value_counts().reset_index()
        sites_by_type.columns = ['Site Type', 'Count']
        
        fig = px.pie(
            sites_by_type,
            values='Count',
            names='Site Type',
            title="Distribution of Heritage Sites by Type",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins, sans-serif")
        )
        
        st.plotly_chart(fig, use_container_width=True)

def visualize_tourist_visits(visits_df):
    """
    Creates visualizations for tourist visits data
    """
    if visits_df is None or visits_df.empty:
        st.warning("No tourist visits data available.")
        return
    
    st.markdown("<h3 class='section-title'>Tourist Visits Analysis</h3>", unsafe_allow_html=True)
    
    # Check for required columns
    required_cols = ['state', 'year', 'domestic_tourists', 'foreign_tourists']
    missing_cols = [col for col in required_cols if col not in visits_df.columns]
    
    if missing_cols:
        st.warning(f"Tourist visits data is missing columns: {', '.join(missing_cols)}")
        # Create visualizations based on available columns
        if 'state' in visits_df.columns:
            # Basic state-wise visualization
            state_data = visits_df.groupby('state').size().reset_index(name='count')
            fig = px.bar(
                state_data,
                x='state',
                y='count',
                title="Tourist Visits by State",
                height=400
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Poppins, sans-serif")
            )
            
            st.plotly_chart(fig, use_container_width=True)
        return
    
    # Year-wise domestic vs foreign tourists
    year_data = visits_df.groupby('year')[['domestic_tourists', 'foreign_tourists']].sum().reset_index()
    
    # Melt the data for easier plotting
    year_data_melted = pd.melt(
        year_data,
        id_vars=['year'],
        value_vars=['domestic_tourists', 'foreign_tourists'],
        var_name='Tourist Type',
        value_name='Number of Tourists'
    )
    
    # Replace column names for better display
    year_data_melted['Tourist Type'] = year_data_melted['Tourist Type'].replace({
        'domestic_tourists': 'Domestic Tourists',
        'foreign_tourists': 'Foreign Tourists'
    })
    
    fig = px.line(
        year_data_melted,
        x='year',
        y='Number of Tourists',
        color='Tourist Type',
        markers=True,
        title="Domestic vs Foreign Tourist Trends",
        height=400,
        line_shape='spline',
        color_discrete_map={
            'Domestic Tourists': '#FF9E44',
            'Foreign Tourists': '#138086'
        }
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        xaxis=dict(tickmode='linear'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # State-wise comparison
    state_data = visits_df.groupby('state')[['domestic_tourists', 'foreign_tourists']].sum().reset_index()
    
    # Calculate total tourists and ratio
    state_data['total_tourists'] = state_data['domestic_tourists'] + state_data['foreign_tourists']
    state_data['dom_for_ratio'] = state_data['domestic_tourists'] / state_data['foreign_tourists'].replace(0, 1)
    
    # Sort by total tourists
    state_data = state_data.sort_values('total_tourists', ascending=False).head(10)
    
    # Create a grouped bar chart
    fig = px.bar(
        state_data,
        x='state',
        y=['domestic_tourists', 'foreign_tourists'],
        labels={
            'state': 'State',
            'value': 'Number of Tourists',
            'variable': 'Tourist Type'
        },
        title="Top 10 States by Tourist Visits",
        height=400,
        barmode='group',
        color_discrete_map={
            'domestic_tourists': '#FF9E44',
            'foreign_tourists': '#138086'
        }
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        legend=dict(
            title="Tourist Type",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Rename legend items
    fig.for_each_trace(lambda t: t.update(
        name=t.name.replace("domestic_tourists", "Domestic Tourists").replace("foreign_tourists", "Foreign Tourists")
    ))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Domestic to foreign tourist ratio
    fig = px.bar(
        state_data,
        x='state',
        y='dom_for_ratio',
        title="Domestic to Foreign Tourist Ratio by State",
        height=350,
        color='dom_for_ratio',
        color_continuous_scale='Oranges'
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif"),
        yaxis=dict(title="Domestic/Foreign Ratio"),
        coloraxis_showscale=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

def visualize_performing_arts(arts_df):
    """
    Creates visualizations for performing arts data
    """
    if arts_df is None or arts_df.empty:
        st.warning("No performing arts data available.")
        return
    
    st.markdown("<h3 class='section-title'>Performing Arts Analysis</h3>", unsafe_allow_html=True)
    
    # Check for required columns
    if 'art_form' in arts_df.columns and 'state' in arts_df.columns:
        # Distribution of art forms
        art_forms = arts_df['art_form'].value_counts().reset_index()
        art_forms.columns = ['Art Form', 'Count']
        
        fig = px.bar(
            art_forms.head(10),
            x='Art Form',
            y='Count',
            title="Top 10 Performing Art Forms",
            height=400,
            color='Count',
            color_continuous_scale='Oranges'
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins, sans-serif"),
            xaxis=dict(tickangle=45)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # State-wise art forms
        state_arts = arts_df.groupby('state')['art_form'].nunique().reset_index()
        state_arts.columns = ['State', 'Number of Art Forms']
        
        fig = px.choropleth_mapbox(
            state_arts,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Number of Art Forms',
            color_continuous_scale='Oranges',
            range_color=(0, state_arts['Number of Art Forms'].max()),
            mapbox_style="carto-positron",
            zoom=3.5,
            center={"lat": 20.5937, "lon": 78.9629},
            opacity=0.7,
            labels={'Number of Art Forms': 'Art Forms'}
        )
        
        fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0},
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Performing arts data doesn't have required columns (art_form, state).")
        
        # Display available columns
        if arts_df is not None:
            st.write("Available columns:", arts_df.columns.tolist())
            
            # Try to create a basic visualization with whatever columns are available
            if len(arts_df.columns) >= 2:
                column1, column2 = arts_df.columns[:2]
                if arts_df[column1].dtype in [object, 'category'] and pd.api.types.is_numeric_dtype(arts_df[column2]):
                    # Simple bar chart with available columns
                    grouped_data = arts_df.groupby(column1)[column2].sum().reset_index()
                    
                    fig = px.bar(
                        grouped_data.head(10),
                        x=column1,
                        y=column2,
                        title=f"{column2} by {column1}",
                        height=400
                    )
                    
                    fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Poppins, sans-serif")
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)

# Main dashboard function
def data_insights_dashboard():
    """
    Main function to display the Data Insights dashboard
    """
    # st.markdown("<h1 class='main-header'>Data Insights Dashboard</h1>", unsafe_allow_html=True)
    # st.markdown("<p class='sub-header'>Exploring real-time data on India's cultural heritage and tourism</p>", unsafe_allow_html=True)
    
    # Add a notice about real-time data
    # st.info("This dashboard connects to data.gov.in APIs to fetch the latest information on heritage sites, tourism statistics, and cultural arts.")
    
    # Tabs for different data categories
    tab1, tab2, tab3 = st.tabs(["🏛️ Heritage Sites", "🧳 Tourist Visits", "🎭 Performing Arts"])
    
    with tab1:
        # Load and visualize heritage sites data
        heritage_df = load_heritage_sites_data()
        visualize_heritage_sites(heritage_df)
    
    with tab2:
        # Load and visualize tourist visits data
        visits_df = load_tourist_visits_data()
        visualize_tourist_visits(visits_df)
    
    with tab3:
        # Load and visualize performing arts data
        arts_df = load_performing_arts_data()
        visualize_performing_arts(arts_df)
    
    # Cultural tourism correlation analysis
    st.markdown("<h3 class='section-title'>Cultural Tourism Correlation Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<p>Analyzing the relationship between cultural heritage sites and tourism patterns</p>", unsafe_allow_html=True)
    
    # Check if we have both heritage sites and tourist visits data
    if (heritage_df is not None and not heritage_df.empty and 
        visits_df is not None and not visits_df.empty and
        'state' in heritage_df.columns and 'state' in visits_df.columns):
        
        # Aggregate data by state
        heritage_by_state = heritage_df.groupby('state').size().reset_index(name='heritage_site_count')
        visits_by_state = visits_df.groupby('state')[['domestic_tourists', 'foreign_tourists']].sum().reset_index()
        
        # Merge the datasets
        merged_data = pd.merge(heritage_by_state, visits_by_state, on='state', how='inner')
        merged_data['total_tourists'] = merged_data['domestic_tourists'] + merged_data['foreign_tourists']
        
        # Create scatter plot
        fig = px.scatter(
            merged_data,
            x='heritage_site_count',
            y='total_tourists',
            size='total_tourists',
            color='state',
            hover_name='state',
            title="Correlation: Heritage Sites vs Tourist Visits by State",
            labels={
                'heritage_site_count': 'Number of Heritage Sites',
                'total_tourists': 'Total Tourist Visits'
            },
            height=500
        )
        
        # Add a trend line
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Poppins, sans-serif")
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Calculate and display correlation coefficient
        correlation = merged_data['heritage_site_count'].corr(merged_data['total_tourists'])
        
        st.markdown(f"""
        <div class='state-info'>
            <h4>Key Insights</h4>
            <p><b>Correlation Coefficient:</b> {correlation:.2f}</p>
            <p>This indicates a {'strong positive' if abs(correlation) > 0.7 else 'moderate positive' if abs(correlation) > 0.4 else 'weak'} correlation between the number of heritage sites and tourist visits.</p>
            <p>States with more heritage sites tend to attract {'more' if correlation > 0 else 'fewer'} tourists, suggesting that cultural heritage is a {'significant' if abs(correlation) > 0.7 else 'modest'} driver of tourism.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Insufficient data to perform correlation analysis between heritage sites and tourism.")
    
    # Recommendations based on insights
    st.markdown("<h3 class='section-title'>Recommendations for Cultural Tourism Development</h3>", unsafe_allow_html=True)
    
    recommendations = [
        {
            "title": "Digital Heritage Experience",
            "description": "Create virtual reality experiences of heritage sites to reach global audiences and preserve digital records of cultural artifacts.",
            "impact": "High",
            "icon": "🔍"
        },
        {
            "title": "Cultural Tourism Corridors",
            "description": "Develop thematic cultural routes connecting multiple heritage sites to encourage longer stays and diverse cultural experiences.",
            "impact": "Medium",
            "icon": "🛣️"
        },
        {
            "title": "Artisan Tourism Hubs",
            "description": "Establish centers where tourists can interact with and learn from traditional artisans, creating immersive cultural experiences.",
            "impact": "High",
            "icon": "🧶"
        }
    ]
    
    # Display recommendations in columns
    cols = st.columns(3)
    for i, rec in enumerate(recommendations):
        with cols[i]:
            impact_color = "#28a745" if rec["impact"] == "High" else "#ffc107"
            st.markdown(f"""
            <div class='card hover-zoom'>
                <h1 style='font-size: 2rem; text-align: center;'>{rec['icon']}</h1>
                <h4>{rec['title']}</h4>
                <p>{rec['description']}</p>
                <p><b>Impact:</b> <span style='color:{impact_color};'>{rec['impact']}</span></p>
            </div>
            """, unsafe_allow_html=True)

# Function to create mock data files if not available
def create_mock_data_files():
    """
    Creates mock data files to use as fallback if API requests fail
    """
    import os
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Create mock heritage sites data
    heritage_sites = pd.DataFrame({
        'site_name': [
            'Taj Mahal', 'Red Fort', 'Qutub Minar', 'Ajanta Caves', 'Ellora Caves',
            'Sun Temple', 'Khajuraho Temples', 'Mahabalipuram', 'Hampi', 'Fatehpur Sikri'
        ],
        'site_type': [
            'Monument', 'Fort', 'Monument', 'Cave', 'Cave',
            'Temple', 'Temple', 'Temple', 'Archaeological Site', 'Historical City'
        ],
        'state': [
            'Uttar Pradesh', 'Delhi', 'Delhi', 'Maharashtra', 'Maharashtra',
            'Odisha', 'Madhya Pradesh', 'Tamil Nadu', 'Karnataka', 'Uttar Pradesh'
        ],
        'latitude': [
            27.1751, 28.6562, 28.5245, 20.5519, 20.0258,
            19.8876, 24.8318, 12.6269, 15.3350, 27.0940
        ],
        'longitude': [
            78.0421, 77.2410, 77.1855, 75.7003, 75.1772,
            85.8513, 79.9199, 80.1928, 76.4600, 77.6710
        ],
        'year_of_inscription': [
            1983, 2007, 1993, 1983, 1983,
            1984, 1986, 1984, 1986, 1986
        ],
        'description': [
            'Iconic white marble mausoleum', 'Historic red sandstone fort complex',
            'Tallest brick minaret in the world', 'Buddhist cave paintings',
            'Rock-cut cave temples', 'Ancient sun temple with intricate carvings',
            'Medieval temples with erotic sculptures', 'Shore Temple complex',
            'Ruins of Vijayanagara Empire', 'Mughal imperial city'
        ]
    })
    
    # Create mock tourist visits data
    states = ['Uttar Pradesh', 'Delhi', 'Maharashtra', 'Madhya Pradesh', 'Tamil Nadu', 'Karnataka', 'Rajasthan', 'Kerala', 'Goa']
    years = list(range(2018, 2024))
    
    tourist_data = []
    
    for state in states:
        for year in years:
            # Generate random but realistic looking data
            domestic = int(1000000 * (1 + (year - 2018) * 0.1) * (0.5 + state.__hash__() % 10 / 10))
            foreign = int(100000 * (1 + (year - 2018) * 0.08) * (0.5 + state.__hash__() % 10 / 10))
            
            # Add COVID-19 impact for 2020-2021
            if year == 2020:
                domestic *= 0.3
                foreign *= 0.1
            elif year == 2021:
                domestic *= 0.5
                foreign *= 0.2
            
            tourist_data.append({
                'state': state,
                'year': year,
                'domestic_tourists': int(domestic),
                'foreign_tourists': int(foreign)
            })
    
    tourist_visits = pd.DataFrame(tourist_data)
    
    # Create mock performing arts data
    art_forms = [
        'Bharatanatyam', 'Kathakali', 'Kathak', 'Odissi', 'Kuchipudi',
        'Manipuri', 'Mohiniyattam', 'Sattriya', 'Garba', 'Bhangra',
        'Chhau', 'Yakshagana', 'Lavani', 'Bihu', 'Ghoomar'
    ]
    
    states_art_map = {
        'Tamil Nadu': ['Bharatanatyam', 'Therukoothu'],
        'Kerala': ['Kathakali', 'Mohiniyattam', 'Koodiyattam'],
        'Uttar Pradesh': ['Kathak', 'Nautanki'],
        'Odisha': ['Odissi', 'Chhau', 'Pala'],
        'Andhra Pradesh': ['Kuchipudi', 'Burrakatha'],
        'Manipur': ['Manipuri', 'Lai Haraoba'],
        'Assam': ['Sattriya', 'Bihu', 'Ankiya Naat'],
        'Gujarat': ['Garba', 'Dandiya Raas'],
        'Punjab': ['Bhangra', 'Giddha'],
        'West Bengal': ['Chhau', 'Baul', 'Jatra'],
        'Karnataka': ['Yakshagana', 'Dollu Kunitha'],
        'Maharashtra': ['Lavani', 'Tamasha'],
        'Rajasthan': ['Ghoomar', 'Kalbelia', 'Teratali']
    }
    
    performing_arts_data = []
    
    for state, art_forms in states_art_map.items():
        for art_form in art_forms:
            practitioners = int(100 + (state + art_form).__hash__() % 900)
            events_per_year = int(5 + (state + art_form).__hash__() % 20)
            
            performing_arts_data.append({
                'state': state,
                'art_form': art_form,
                'practitioners': practitioners,
                'events_per_year': events_per_year,
                'endangered_status': practitioners < 300,
                'government_support': bool((state + art_form).__hash__() % 2)
            })
    
    performing_arts = pd.DataFrame(performing_arts_data)
    
    # Save mock data files
    heritage_sites.to_csv("data/mock_heritage_sites.csv", index=False)
    tourist_visits.to_csv("data/mock_tourist_visits.csv", index=False)
    performing_arts.to_csv("data/mock_performing_arts.csv", index=False)
    
    print("Mock data files created successfully.")

# Call create_mock_data_files at import time to ensure files are available
create_mock_data_files()