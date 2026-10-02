# dashboard.py - Streamlit
import streamlit as st
import pandas as pd
import sqlalchemy

st.title("Network & Infrastructure Observability")

# Conexão com banco de dados
engine = sqlalchemy.create_engine("postgresql://user:pass@localhost:5432/telemetry_db")

df = pd.read_sql("SELECT time, cpu_percent FROM device_metrics ORDER BY time DESC LIMIT 100", engine)
st.line_chart(df.set_index("time"))