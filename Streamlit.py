import streamlit as st

from PIL import Image

def homepage1():
    st.title("WELCOME TO FLIGHT PRICE PREDICTION")
    st.image("D:/Guvi/Projects/Flight/miscellaneous/generated-image.png")

def show_eda():
    st.title("Exploratory Data Analysis (EDA)")
    st.subheader("Total Stops vs Price")
    image1 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/stop_vs_price.png")
    st.image(image1, caption="Total_Stops vs Price", use_container_width=True)

    st.subheader("Arline Vs pricing")
    image2 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/arlineprice.png")
    st.image(image2, use_container_width=True)

    st.subheader("Heatmap")
    image3 = Image.open("D:/Guvi/Projects/Flight/streamlit EDA/heatmap.png")
    st.image(image3, use_container_width=True)

def price_predict():
    import mlflow
    import mlflow.pyfunc
    import pandas as pd

    st.title("Flight Price Prediction")

    st.subheader("Enter Flight Details")
    airline = st.selectbox("Airline", ["IndiGo", "Air India", "SpiceJet", "Vistara", "GoAir", "Trujet"])
    source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Banglore"])
    destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata", "Banglore"])
    date_of_journey = st.date_input("Date of Journey")
    dep_time = st.time_input("Departure Time")
    arr_time = st.time_input("Arrival Time")
    total_stops = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops", "3 stops", "4 stops"])

    if st.button("Predict Price"):
        input_df = pd.DataFrame({
            "Airline": [airline],
            "Source": [source],
            "Destination": [destination],
            "Date_of_Journey": [date_of_journey.strftime("%d/%m/%Y")],
            "Dep_Time": [dep_time.strftime("%H:%M")],
            "Arrival_Time": [arr_time.strftime("%H:%M")],
            "Total_Stops": [total_stops]
        })

        try:
            model_uri = "models:/XGBoostFlightModel@Production"
            model = mlflow.pyfunc.load_model(model_uri)

            prediction = model.predict(input_df)

            st.success(f"Predicted Flight Price: ₹ {prediction[0]:,.2f}")
        
        except Exception as e:
            st.error(f"Prediction failed: {e}")


            



def thank():
    st.title("Thank you")
    st.image("C:/Users/LONE PIRATE.LAPTOP-PAANLTJP/OneDrive/Pictures/hand-lettering-thank-you-flowery-vector.jpg")
    st.subheader("By Abinash")

pages = {
    "Home" : homepage1,
    "EDA" : show_eda,
    "PRICING" : price_predict,
    "END" : thank
}
selection = st.sidebar.radio("choose a page",list(pages.keys()))
if selection:
    pages[selection]()

