import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df_us_cars = pd.read_csv('vehicles_us.csv')

# Assume the 'model' column has both make and model (e.g., 'Ford F-150')
df_us_cars[['make', 'model']] = df_us_cars['model'].str.split(' ', n=1, expand=True)
df_us_cars[['make', 'model']].head()

# Clean column names
df_us_cars.columns = df_us_cars.columns.str.strip().str.lower()

# Header
st.header("US Vehicles Data Analysis")

# Checkbox to filter data based on 'is_4wd' column
show_4wd = st.checkbox('Show only 4WD vehicles')

# Filter data based on checkbox
if show_4wd:
    filtered_df = df_us_cars[df_us_cars['is_4wd'] == 1]
else:
    filtered_df = df_us_cars

# Plotly Express Histogram of Vehicle Prices
st.subheader("Vehicle Price Distribution")
fig_hist = px.histogram(filtered_df, x='price', nbins=30, title='Price Distribution of Vehicles')
st.plotly_chart(fig_hist)

# Plotly Express Scatter Plot of Price vs Model Year
st.subheader("Price vs. Model Year Scatter Plot")
fig_scatter = px.scatter(filtered_df, x='model_year', y='price', color='condition',
                         title='Price vs. Model Year by Condition')
st.plotly_chart(fig_scatter)

