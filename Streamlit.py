import streamlit as st
import pickle
import pandas as pd
from PIL import Image

#loading the model 

with open("best_model.pkl","rb") as f:
    model=pickle.load(f)

with open("best_class.pkl", "rb") as f:
    class_model = pickle.load(f)

#geting the list of columns
trained_columns = model.feature_names_in_
trained_class_columns = class_model.feature_names_in_

def homepage():
    st.image("D:/Guvi/Projects/Flight/miscellaneous/3.png", use_container_width=True)

def homepage1():
    st.title("FLIGHT PRICE PREDICTION")
    st.image("D:/Guvi/Projects/Flight/miscellaneous/generated-image.png")

def eda_flight():
    st.title("Exploratory Data Analysis (EDA)")
    st.subheader("Total Stops vs Price")
    image1 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/stop_vs_price.png")
    st.image(image1, use_container_width=True)

    st.subheader("Arline Vs pricing")
    image2 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/arlineprice.png")
    st.image(image2, use_container_width=True)

    st.subheader("Heatmap")
    image3 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/heatmap.png")
    st.image(image3, use_container_width=True)

def homepage2():
    st.title("CUSTOMER SATISFACTION PREDICTION")
    st.image("D:/Guvi/Projects/Flight/miscellaneous/generated-image2.png")

def eda_satisfaction():
    st.title("Exploratory Data Analysis (EDA)")
    st.subheader("Baggage handling Vs satisfactions")
    image1 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/cx sat/bag to sat.png")
    st.image(image1, use_container_width=True)

    st.subheader("Arrival to Departure delay affecting Satisfaction")
    image2 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/cx sat/ari_dep_delay to sat.png")
    st.image(image2, use_container_width=True)

    st.subheader("Travel class impact on stisfaction")
    image3 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/cx sat/traval class to sat.png")
    st.image(image3, use_container_width=True)

    st.subheader("Inflight service Vs Satisfaction")
    image4 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/cx sat/in flishgt ser to sat.png")
    st.image(image4, use_container_width=True)



def price_predict():
    st.title("Flight Price Prediction")
    st.subheader("Choose the choices for Your journey")

    airline = st.selectbox("Airline", ['Jet Airways', 'IndiGo', 'Air India', 'SpiceJet', 'Vistara'])
    Source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
    total_stops = st.selectbox("Total Stops", ['non-stop', '1 stop', '2 stops', '3 stops'])
    journey_day = st.number_input("Journey Day (1-31)", 1, 31, 12, key= "journey_day")
    journey_month = st.number_input("Journey Month (1-12)", 1, 12, 5, key= "journey_month")
    journey_year = st.number_input("Journey Year (2019 - 2020)", 2019, 2020, 2019, key="journey_year")
    dep_hour = st.slider("Departure Hour", 0, 23, 10, key="dep_hour")
    dep_minute = st.slider("Departure Minute", 0, 59, 30,key="dep_minute")
    arrival_day = st.number_input("Arrival Day (1-31)", 1, 31, 1, key="arrival_day")
    arrival_month = st.number_input("Arrival Month (1-12)", 1, 6, 5,key="arrival_month")
    arrival_year = st.number_input("Arrival Year (2019 - 2020)", 2019, 2020, 2019, key="arrival_year")
    arrival_hour = st.slider("Arrival Hour", 0, 23, 14, key="arrival_hour")
    arrival_minute = st.slider("Arrival Minute", 0, 59, 45, key="arrival_minute")
    duration_hours = st.number_input("Duration Hours", 0, 24, 2)


    input_data = {'Airline': airline,
    'Source': Source,
    'Destination': Destination,
    'Total_Stops': total_stops,
    'journey_day': journey_day,
    'journey_month': journey_month,
    'journey_year': journey_year,
    'Dep_hour': dep_hour,
    'Dep_minute': dep_minute,
    'arrival_day': arrival_day,
    'arrival_month': arrival_month,
    'arrival_year': arrival_year,
    'Arrival_hour': arrival_hour,
    'Arrival_minute': arrival_minute,
    'Duration_in_hours': duration_hours}

    #seperating columns 
    categorical_columns = ['Airline', 'Source', 'Destination', 'Total_Stops']
    numerical_columns = ['journey_day', 'journey_month', 'journey_year',
    'Dep_hour', 'Dep_minute',
    'arrival_day', 'arrival_month', 'arrival_year',
    'Arrival_hour', 'Arrival_minute',
    'Duration_in_hours']

    #dataframe
    df_input = pd.DataFrame([input_data])

    #one hot encoding
    df_cat_encoded = pd.get_dummies(df_input[categorical_columns])

    df_final = pd.concat([df_input[numerical_columns], df_cat_encoded], axis=1)

    #to fill any missing columns 
    for col in trained_columns:
        if col not in df_final.columns:
            df_final[col] = 0
    df_final = df_final[trained_columns]


    
    if st.button("Predict"):
        prediction = model.predict(df_final)[0]
        st.success(f"Estimated Flight Price: ₹{prediction:.2f}")
            

def customer_satisfaction():
    st.title("Customer satisfaction Prediction")
    st.subheader("Select your choice among the choices")

    gender = st.selectbox("Gender", ['Male', 'Female'])
    custoner_type = st.selectbox("Custoer Type", ['Loyal Customer', 'disloyal Customer'])
    age = st.number_input("age (1-100)", 1, 100, 24, key= "age")
    travel_type = st.selectbox("Travel type", ['Personal Travel', 'Business travel'])
    class_t = st.selectbox("Class", ['Eco Plus', 'Business', 'Eco'])
    distance = st.slider("Flight Distance", 0, 10000, 500, key="Flight Distance")
    in_service = st.slider("Inflight wifi service", 0, 5, 4, key="Inflight wifi service")
    dept_arrival = st.slider("Departure/Arrival time convenient", 0, 5, 3, key="Departure/Arrival time convenient") 
    online_booking = st.slider("Ease of Online booking", 0, 5, 3, key="Ease of Online booking") 
    gate_loaction = st.slider("Gate location", 0, 5, 2, key="Gate location")
    food_drink = st.slider("Food and drink", 0, 5, 4, key="Food and drink")
    boarding = st.slider("Online boarding", 0, 5, 4, key="Online boarding")
    comfort  = st.slider("Seat comfort", 0, 5, 4, key="Seat comfort")
    entertainment = st.slider("Inflight entertainment", 0, 5, 3, key="Inflight entertainment")
    onboard_services = st.slider("On-board service", 0, 5, 4, key="On-board service")
    leg_room = st.slider("Leg room service", 0, 5, 2, key="Leg room service")
    bag_handling =st.slider("Baggage handling", 0, 5, 3, key="Baggage handling") 
    Checkin_service = st.slider("Checkin serviceg", 0, 5, 4, key="Checkin service")
    inflight_service = st.slider("Inflight service", 0, 5, 4, key="Inflight service")
    Cleanliness = st.slider("Cleanliness", 0, 5, 4, key="Cleanliness")
    dep_delay_minute = st.number_input("Departure Delay in Minutes (0-60)", 0, 60, 15, key= "Departure Delay in Minutes")
    arrival_delay_minute = st.number_input("Arrival Delay in Minutes (0-60)", 0, 60, 15, key= "Arrival Delay in Minutes")

    input_data = {'Gender': gender,
    'Customer Type': custoner_type,
    'Age': age,
    'Type of Travel': travel_type,
    'Class': class_t,
    'Flight Distance': distance,
    'Inflight wifi service': in_service,
    'Departure/Arrival time convenient': dept_arrival,
    'Ease of Online booking': online_booking,
    'Gate location': gate_loaction,
    'Food and drink': food_drink,
    'Online boarding': boarding,
    'Seat comfort': comfort,
    'Inflight entertainment': entertainment,
    'On-board service': onboard_services,
    'Leg room service': leg_room,
    'Baggage handling': bag_handling,
    'Checkin service' : Checkin_service,
    'Inflight service': inflight_service,
    'Cleanliness': Cleanliness,
    'Departure Delay in Minutes' : dep_delay_minute ,
    'Arrival Delay in Minutes' : arrival_delay_minute
    }

    #seperating columns 
    cat_columns = ["Gender", "Type of Travel", "Class", "Customer Type"]
    num_columns = ['Age', 'Type of Travel',
       'Class', 'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']

    df_input = pd.DataFrame([input_data])

    #one hot encoding
    df_cat_encoded = pd.get_dummies(df_input[cat_columns])

    df_final = pd.concat([df_input[num_columns], df_cat_encoded], axis=1)

    for col in trained_class_columns:
        if col not in df_final:
            df_final[col] = 0
    df_final = df_final[trained_class_columns]

    label_map = {
    1: "Satisfied 😊",
    0: "Neutral/Dis-satisfied 😕"
    } 
          
    if st.button("Predict"):
        prediction = class_model.predict(df_final)[0]
        st.success(f"Predicted Satisfaction: {label_map[prediction]}")

def thank():
    st.title("Thank you")
    st.image("C:/Users/LONE PIRATE.LAPTOP-PAANLTJP/OneDrive/Pictures/hand-lettering-thank-you-flowery-vector.jpg")
    st.subheader("By Abinash")

pages = {
    "Home" : homepage,
    "Flight Price" : homepage1,
    "EDA Flight price" : eda_flight,
    "PRICING" : price_predict,
    "Customer satisfaction" : homepage2,
    "EDA satisfaction" : eda_satisfaction,
    "SATISFACTION" : customer_satisfaction,
    "END" : thank
}
selection = st.sidebar.radio("choose a page",list(pages.keys()))
if selection:
    pages[selection]()

