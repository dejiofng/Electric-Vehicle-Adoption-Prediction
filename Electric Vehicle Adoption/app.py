import streamlit as st
import pickle

model = pickle.load(open('model.pickle', 'rb'))

def run():
    st.set_page_config(
        page_title="EV Adoption Predictor",
        page_icon="🚗",
        layout="wide"
    )

    st.title("Electric Vehicle Adoption Behaviour")
    st.write("Enter user information to predict vehicle adoption likelihood.")

    st.header("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (in years)", value=45, min_value=18, max_value=100)

        ann_inc = st.number_input("Annual Income ($)", value=44312)

    with col2:    
        edu = st.selectbox("Select Education Level:", ["Bachelor", "High School", "Master", "PhD"])
        edu_mapping = {"Bachelor": 0, "High School": 1, "Master": 2, "PhD": 3}
        edu_encoded = edu_mapping[edu]

        loc = st.selectbox("Select Location:", ["Rural", "Suburban", "Urban"])
        loc_mapping = {"Rural": 0, "Suburban": 1, "Urban": 2}
        loc_encoded = loc_mapping[loc]
    


    st.header("🚘 Vehicle Information")

    col1, col2 = st.columns(2)

    with col1:
        car = st.selectbox("Select Car Type:", ["Hatchback", "SUV", "Sedan", "Truck"])
        car_mapping = {"Hatchback": 0, "SUV": 1, "Sedan": 2, "Truck": 3}
        car_encoded = car_mapping[car]

        vehicle_age = st.number_input("Vehicle Age (yrs)", value=6)

    with col2:
        fuel_expense = st.number_input("Fuel Expense Per Month", value=295)

        weekly_trav = st.number_input("Weekly Travel Distance (km)", value=229)

    
    st.header("🔌 Charging Information")

    col1, col2 = st.columns(2)

    with col1:
        home_charging = st.selectbox("Home Charging Available? ", ["Yes", "No"])
        home_charging_mapping = {"Yes": 1, "No": 0}
        home_charging_encoded = home_charging_mapping[home_charging]

        nearest_charging = st.number_input("Nearest Charging Station (km)", value=7)

    with col2:
        charging_station = st.number_input("Charging Station Accessibility", value=6)

        electricity_cost = st.number_input("Electricity Cost per KWh", value=0.25, min_value=0.0, max_value=0.8, step=0.01)

    
    st.header("🌱 EV Attitude & Awareness")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        env_awareness = st.slider("Environmental Awareness Score", 0.0, 10.0, 7.0)

        tech_affinity = st.slider("Technology Affinity Score", 0.0, 10.0, 7.0)

    with col2:
        gov_awareness = st.slider("Government Incentive Awareness", 0.0, 10.0, 6.0)

        ev_knowledge = st.slider("Electric Vehicle Knowledge Score", 0.0, 10.0, 6.0)

    with col3:
        range_anxiety = st.slider("Range Anxiety Score", 0.0, 10.0, 5.0)

        battery_concern = st.slider("Battery Replacement Concern", 0.0, 10.0, 5.0)

    ev_exp = st.selectbox("Electric Vehicle Experience", ["Yes", "No"])
    ev_exp_mapping = {"Yes": 1, "No": 0}
    ev_exp_encoded = ev_exp_mapping[ev_exp]

    daily_com = st.number_input("Daily Commute (km)", value=35)

    monthly_energy = st.number_input("Monthly Energy Consumption (KWh)", value=186)

    monthly_charging = st.number_input("Monthly Charging Cost", value=40)

    if st.button("Submit"):
        features = [[age, ann_inc, edu_encoded, loc_encoded, daily_com, weekly_trav, car_encoded, vehicle_age, fuel_expense, charging_station, nearest_charging, home_charging_encoded, electricity_cost, env_awareness, gov_awareness, tech_affinity, range_anxiety, battery_concern, ev_knowledge, ev_exp_encoded, monthly_energy, monthly_charging]]
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]
        prediction = int(prediction)
        output_mapping = {0: "Low", 1: "Medium", 2: "High"}
        if prediction == 2:
            st.success("High likelihood of adopting an EV")
            st.success(f"Confidence: {probs[prediction] * 100:.1f}%")
        elif prediction == 1:
            st.warning("Moderate likelihood of adopting an EV")
            st.warning(f"Confidence: {probs[prediction] * 100:.1f}%")
        else:
            st.error("Low likelihood of adopting an EV")
            st.error(f"Confidence: {probs[prediction] * 100:.1f}%")


run()
if st.button("Reset"):
    st.rerun()