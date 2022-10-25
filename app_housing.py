import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Violet')
df = pd.read_csv('housing.csv')

# add a slider
housing_value_filter = st.slider('Minimal Midian Housing Value (Millions):', 0.0, 500001.0, 20000.0)
# filter by median_house_value 
df = df[df.median_house_value >= housing_value_filter]

st.subheader('see more filters in the sidebar')

# create a multi select
ocean_proximity_filter = st.sidebar.multiselect(
     'Ocean_proximity Selector',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]

# a radio button widget to filter by income level, Low (≤2.5), Medium (> 2.5 & < 4.5), High (> 4.5)
genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Medium':
    df = df[df.median_income > 2.5]
    df = df[df.median_income < 4.5]
    # the second df is on the base of the first df, thus we could get the part ehich is smaller than 4.5 from the part of (2.5: )
else:
    df = df[df.median_income > 4.5]

st.map(df)


# show the plot
st.subheader('Histogram of the Median Housing Value')
fig, ax = plt.subplots()
df.median_house_value.hist(bins=30)
st.pyplot(fig)