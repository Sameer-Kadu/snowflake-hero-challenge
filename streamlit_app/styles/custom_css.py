import streamlit as st
def apply_custom_css():
    st.markdown("""
    <style>
    
    /* Float the sidebar toggle button to the top-left without taking space */
    [data-testid="stSidebarHeader"] {
        position: absolute;
        left: 17rem;
        position: fixed;
        z-index: 9999;
    }
    
     

        /* Hide Streamlit footer */
        footer[data-testid="stFooter"] {
            display: none;
        }

        /* Optional: Remove blank space from hidden header */
        .block-container {
            padding-top: 1rem;
        }
    
        .block-container {
            padding: 0rem 5rem 0rem 5rem; /* top, right, bottom, left */
        }
        
        /* Main theme colors */
        :root {
            --primary: #FF9E44;
            --secondary: #E25822;
            --accent: #138086;
            --light: #EFFFFA;
            --dark: #1E3D59;
        }
        
        /* Header styling */
        .main-header {
            color: var(--secondary);
            font-family: 'Poppins', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            top-margin: 50px;
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            margin-bottom: 0px;
            margin-bottom: 0px;
            margin-bottom: 0px;
            margin-bottom: 0px;
            margin-bottom: 0px;
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .sub-header {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-top: 0px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 5px solid var(--primary);
        }
        
        .stat-card {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--secondary);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: var(--dark);
            text-transform: uppercase;
        }
        
        /* Section styling */
        .section-title {
            color: var(--dark);
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Sidebar styling */
        .css-1lcbmhc.e1fqkh3o3 {
            background-color: var(--light);
        }
        
        /* Custom metric container */
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 1rem;
        }
        
        /* State info box */
        .state-info {
            background-color: rgba(255, 158, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Cultural site card */
        .site-card {
            background: linear-gradient(135deg, #fff 60%, rgba(255, 158, 68, 0.2) 100%);
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--dark);
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        
        /* Make DataFrames more attractive */
        .dataframe {
            font-family: 'Arial', sans-serif;
        }
        
        /* Adjusting plot background */
        .js-plotly-plot .plotly {
            background-color: transparent !important;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
            background-color: #f0f0f0;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* Custom tooltip */
        [data-testid="stTooltip"] {
            background-color: var(--dark);
            color: white;
            border-radius: 5px;
            padding: 0.5rem;
        }
        
        /* Animate on hover */
        .hover-zoom {
            transition: transform 0.3s ease;
        }
        
        .hover-zoom:hover {
            transform: scale(1.03);
        }
    </style>
    """, unsafe_allow_html=True)