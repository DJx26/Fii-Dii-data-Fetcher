import streamlit as st
import pandas as pd
from nsepython import nse_fiidii

st.set_page_config(page_title="FII/DII Dashboard", layout="wide")
st.title("📊 FII/DII Tracker - FundPulse India")
# Fetch data
try:
    data = nse_fiidii("pandas")
    st.write(data)  # Debug: Show raw data
except Exception as e:
    st.error(f"Failed to fetch FII/DII data: {e}")
    st.stop()

# Preprocess
data['buyValue'] = pd.to_numeric(data['buyValue'], errors='coerce')
data['sellValue'] = pd.to_numeric(data['sellValue'], errors='coerce')
data['netValue'] = pd.to_numeric(data['netValue'], errors='coerce')

# Summary cards
fii = data[data['category'] == 'FII']
dii = data[data['category'] == 'DII']

col1, col2 = st.columns(2)
col1.metric("🟢 FII Net", f"{fii['netValue'].sum():,.2f} Cr")
col2.metric("🔵 DII Net", f"{dii['netValue'].sum():,.2f} Cr")

# Display data table
st.subheader("📄 Full FII/DII Report")
st.dataframe(data.style.format({
    'buyValue': '{:,.2f}',
    'sellValue': '{:,.2f}',
    'netValue': '{:,.2f}'
}))
# Top 5 by Buy
st.subheader("🏆 Top 5 Stocks by Buy Value")
top_buy = data.sort_values(by='buyValue', ascending=False).head(5)
st.table(top_buy[['date', 'category', 'buyValue', 'sellValue', 'netValue']])

# Top 5 by Sell
st.subheader("📉 Top 5 Stocks by Sell Value")
top_sell = data.sort_values(by='sellValue', ascending=False).head(5)
st.table(top_sell[['date', 'category', 'buyValue', 'sellValue', 'netValue']]) 
