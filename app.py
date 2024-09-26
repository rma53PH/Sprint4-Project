import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')

# Streamlit header
st.header("Vehicle Data Analysis")

# Checkbox to filter data based on vehicle condition
condition_filter = st.checkbox("Show only 'good' condition vehicles")

if condition_filter:
    filtered_df = df[df['condition'] == 'good']
else:
    filtered_df = df

# Plotly Express histogram of vehicle prices
fig_hist = px.histogram(
    filtered_df,
    x='price',
    title='Histogram of Vehicle Prices',
    nbins=30,
    labels={'price': 'Price (USD)'}
)

# Display the histogram using Streamlit
st.plotly_chart(fig_hist)

# Plotly Express scatter plot of price vs. odometer
fig_scatter = px.scatter(
    filtered_df,
    x='odometer',
    y='price',
    color='condition',
    title='Scatter Plot of Price vs. Odometer',
    labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'}
)

# Display the scatter plot using Streamlit
st.plotly_chart(fig_scatter)
