import streamlit as st
import datetime
import requests
import pandas as pd
'''
# 🚖 TaxiFareModel 🚖
'''




# 1 date and time

today = datetime.date.today()
heure_actuelle = datetime.time()
date = st.date_input(
    "pick up date & time",
    today)

heure = st.time_input('à quelle heure ? ', datetime.time(11,45))

pickup_time = date.strftime("%Y-%m-%d") + " " + heure.strftime("%H:%M:%S")



col1, col2, col3 = st.columns(3)

with col1:
   st.header("🚀DEPART")
   pickup_longitude = st.number_input(' longitude ',
                            value = -74.00597,
                            placeholder="exemple -74.00596")
   pickup_latitude = st.number_input(' latitude ',
                           value = 40.71427,
                           placeholder="exemple 40.71427")

with col2:
   st.header("DEST  🏝️")
   dropoff_longitude = st.number_input('longitude ',
                            value = -74.00597,
                            placeholder="exemple -74.00596")
   dropoff_latitude = st.number_input('latitude ',
                           value = 40.71427,
                           placeholder="exemple 40.71427")

with col3:
   st.header("PASSAGERS 👯")
   passenger_count = st.number_input("nb passagers", value=1,
                                        min_value = 1,
                                        max_value=10,
                                        step=1,
                                        placeholder="Type a number...")




#reponse = requests.get(url, params=params)
#print(reponse.status_code)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    #click = st.button("Calculer le prix 💸 ", type = "secondary")
    #if click :
    params = {"pickup_datetime": pickup_time,
                "pickup_longitude":pickup_longitude,
                "pickup_latitude":pickup_latitude,
                "dropoff_longitude":dropoff_longitude,
                "dropoff_latitude":dropoff_latitude,
                "passenger_count":passenger_count
                }
    reponse = requests.get(url, params=params)
    fare = reponse.json()["fare"]
    fare = round(fare,2)
    # affichage en colonnes
    col1, col2, col3 = st.columns(3)
    col1.metric("Status code", reponse.status_code, label_visibility="visible")
    col2.metric("PRICE", str(fare) + " $", delta=None, delta_color="normal", help=None, label_visibility="visible")
    col3.markdown("🚖🚖🚖🚖🚖")

    ballon = st.button("ballons ? ", type="secondary")
    if ballon :
        st.balloons()


    #### CARTE
    st.markdown("# MAPS")
    data = [
    {"coord_type": "pickup", "longitude": params["pickup_longitude"], "latitude": params["pickup_latitude"]},
    {"coord_type": "dropoff", "longitude": params["dropoff_longitude"], "latitude": params["dropoff_latitude"]}]


    df = pd.DataFrame(data)
    st.map(df, size=50, color='#0044ff')
