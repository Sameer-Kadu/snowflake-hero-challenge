import streamlit as st
import snowflake.connector

# Snowflake connection function
def get_snowflake_connection():
    # In a real application, these would be stored securely and not hardcoded
    try:
        conn = snowflake.connector.connect(
            user='samir12',
            password='SamirSubodh@12',
            account='kjzwhoh-wz60091',
            warehouse='COMPUTE_WH',
            database='HERO_DB',
            schema='PUBLIC'
        )
        return conn
    except Exception as e:
        st.error(f"Connection error: {e}")
        return None