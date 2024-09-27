import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df_us_cars = pd.read_csv('vehicles_us.csv')

# Title for the app
st.title('Vehicle Data Exploration')

# Display the dataframe with a checkbox to toggle visibility
if st.checkbox('Show DataFrame'):
    st.write(df.head())

# Histogram for Condition vs Model Year
st.header('Histogram: Condition vs. Model Year')
fig_hist = px.histogram(df_us_cars, x='model_year', color='condition', 
                        title='Condition Distribution by Model Year', 
                        nbins=20)
st.plotly_chart(fig_hist)

# Vehicle types by manufacturer
st.header('Vehicle Types by Manufacturer')
manufacturer = st.selectbox('Select Manufacturer', df['make'].unique())
filtered_df = df_us_cars[df_us_cars['make'] == manufacturer]
fig_types = px.histogram(filtered_df, x='type', 
                         title=f'Vehicle Types for {manufacturer}')
st.plotly_chart(fig_types)

# Price Distribution by Manufacturer
st.header('Compare Price Distribution Between Manufacturers')
fig_price_manufacturer = px.box(df_us_cars, x='make', y='price', 
                                title='Price Distribution Across Manufacturers', 
                                points='all')
st.plotly_chart(fig_price_manufacturer)

# Scatter plot: Price distribution by model year and model
st.header('Scatter Plot: Price Distribution by Model Year and Model')
model_year_range = st.slider('Select Model Year Range', 
fig_price_manufacturer = px.box(df_us_cars, x='make', y='price', 
                             int(['model_year'].min()), 
fig_price_manufacturer = px.box(df_us_cars, x='make', y='price', 
                             int(['model_year'].max()), 
                             (2000, 2020))

filtered_df_scatter = df_us_cars[(['model_year'] >= model_year_range[0]) & 
                         (df_us_cars['model_year'] <= model_year_range[1])]

fig_scatter = px.scatter(filtered_df_scatter, x='model_year', y='price', 
                         color='model', title='Price vs. Model Year by Model', 
                         hover_data=['manufacturer'])
st.plotly_chart(fig_scatter)

