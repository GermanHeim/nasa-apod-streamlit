# Importing libraries
import streamlit as st
import requests
from datetime import date
import urllib
from datetime import datetime

# Setting up Streamlit
st.set_page_config(layout="centered", page_icon="☄", page_title="NASA APOD")
st.title("🪐 NASA APOD")
st.write("This app shows you the Astronomy Picture of the Day (APOD) from NASA.")

# Getting data from the NASA API
api_key = st.secrets["api_key"]
date = st.date_input('Select the day of the image')
api_url = "https://api.nasa.gov/planetary/apod?date={}&api_key={}".format(date, api_key)
response = requests.get(api_url)

# Get json info from the api_url
json_data = response.json()

# Storing hdurl and title in variables from json_data
today = date.today()
first_apod_str = "16 June, 1995"
first_apod_date = datetime.date(datetime.strptime(first_apod_str, "%d %B, %Y"))

# Setting if statement to check if the date is valid and the status code is 200
if response.status_code == 200:
   if date > today:
      st.error("You can't select a future date")
   elif date < first_apod_date:
      st.error("The first APOD was released in 1995-06-16, please select a date after that one.")
   else:
      media_type = json_data["media_type"]
      if media_type == "image":
         hdurl = json_data["hdurl"]
         title = json_data["title"]
         explanation = json_data["explanation"]
         
         # Showing the information
         st.image(hdurl)
         st.header(title + " - " + str(date))
         st.write(explanation)
         st.write("Image by NASA https://www.nasa.gov/ © 2022 All rights reserved")
         
         # Creating an image to download
         req = urllib.request.build_opener()
         req.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)')]
         file_name = "APOD.jpg"
         urllib.request.install_opener(req)
         urllib.request.urlretrieve(hdurl, file_name)
         
         # Adding a download button
         with open("APOD.jpg", "rb") as file:
            btn = st.download_button(
               label="Download image",
               data=file,
               file_name="APOD.jpg",
               mime="image/jpg"
               )
            if btn:
               st.success("Image downloaded")
            else:
               st.error("There isn't an available picture for that date, please select another date.")
else:
   st.error("There was an error, please try using another date.")