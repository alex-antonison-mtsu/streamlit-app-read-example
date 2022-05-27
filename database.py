from sqlalchemy import create_engine
import streamlit as st


def return_engine():
    # build engine url
    user = st.secrets["username"]
    pwd = st.secrets["password"]
    host = st.secrets["host"]
    engine_url = f"postgresql+psycopg2://{user}:{pwd}@{host}/dear_database"
    # creates the sql alchemy engine to query a database
    return create_engine(engine_url)
