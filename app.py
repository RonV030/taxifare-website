import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date_time = st.text_input('date and time')
print(date_time)
pickup_lon = st.text_input('pickup longitude')
print(pickup_lon)
pickup_lat = st.text_input('pickup latitude')
print(pickup_lat)
dropoff_lon = st.text_input('dropoff longitude')
print(dropoff_lon)
dropoff_lat = st.text_input('dropoff latitude')
print(dropoff_lat)
passenger_count = st.text_input('passenger count')
print(passenger_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...
params = {
    'key': ['key'],
    'pickup_datetime': [datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')],
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
}
# 3. Let's call our API using the `requests` package...
response = requests.get(url, params=params)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
prediction = response.json()
## Finally, we can display the prediction to the user
prediction
