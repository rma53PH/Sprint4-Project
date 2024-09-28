import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df_us_cars = pd.read_csv('vehicles_us.csv')

# Assume the 'model' column has both make and model (e.g., 'Ford F-150')
df_us_cars[['make', 'model']] = df_us_cars['model'].str.split(' ', n=1, expand=True)
df_us_cars[['make', 'model']].head()

# Create checkboxes for selecting vehicle makes
unique_makes = df_us_cars['make'].unique()
selected_makes = st.multiselect('Select Vehicle Makes:', unique_makes)

# Filter the DataFrame based on selected makes
filtered_df = df_us_cars[df_us_cars['make'].isin(selected_makes)]

# Histogram of vehicle types by manufacturer
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x='type', hue='make', order=filtered_df['type'].value_counts().index)
plt.title('Vehicle Types by Manufacturer')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data=filtered_df, x='model_year', hue='condition', multiple='stack', bins=20)
plt.title('Condition vs. Model Year')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered_df, x='make', y='price')
plt.title('Price Distribution Between Manufacturers')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(data=filtered_df, x='model_year', y='price', hue='model', alpha=0.7)
plt.title('Price Distribution by Model Year and Model')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()
