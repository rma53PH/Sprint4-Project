# Sprint4-Project
Triple Ten Sprint 4 Project Software Development Tools
The goal of this project is to develop a web app using different software developmenet tools from a local terminal. GitHub, Render, VS Code

Creat a FiftHub Account, a Render Account and VS Code. 

Download the vehicles_us.csv file and create a Data Frame. Save this file to your root directory/Repository for this project. 
Explore the df information in order to create a data set to use in your web app. 

Create an EDA.ipynb Jupyter notebook in VS Code.
Save the notebook in the notebooks directory of your project.
Perform some basic exploratory analysis of the dataset in the notebook.
Create a couple of histograms and scatterplots using plotly-express library.

Develop the web application dashboard
Note that this is not the same development flow that we used in the lesson on rendering.

Create an app.py file in the root of the project’s directory. The following steps (2-4) will require you to write code into this app.py file.
In the app.py file, import streamlit, pandas, and plotly.express.
Read the dataset’s CSV file into a Pandas DataFrame.
From the Jupyter notebook, create and/or copy:
at least one st.header with text
at least one Plotly Express histogram using st.write or st.plotly_chart
at least one Plotly Express scatter plot using st.write or st.plotly_chart
at least one checkbox using st.checkbox that changes the behavior of any of the above components
Deploy the application using Render and verify your app is functional using the URL created. 