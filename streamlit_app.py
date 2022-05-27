# Importing libraries
import streamlit as st
import requests
from datetime import date

# Setting up streamlit
st.set_page_config(layout="centered", page_icon="🪐", page_title="NASA APOD")
st.title("🪐 NASA APOD")
st.write("This app shows you the Astronomy Picture of the Day (APOD) from NASA.")

# Getting data from the NASA API
api_key = st.secrets[api_key]
date = st.date_input('Select the day of the image')
api_url = "https://api.nasa.gov/planetary/apod?date={}&api_key={}}".format(date, api_key)
response = requests.get(api_url)

# Get json info from the api_url
json_data = response.json()

# Storing hdurl and title in variables from json_data
today = date.today()
if date > today:
   st.error("You can't select a future date")
else:
   hdurl = json_data["hdurl"]
   title = json_data["title"]
   st.image(hdurl)
   st.write(title + " -" + date)