import streamlit as st

st.markdown("## BMI Calculator")
st.markdown("### Calculate your BMI Here:")

st.markdown("BMI (Body Mass Index) is a measure of body fat based on height and weight.")

# Input for height in meters
height = st.number_input("Enter your height in meters", min_value=0.0, format="%.2f")

# Option to convert height to feet
convert_to_feet = st.checkbox("Convert height to feet")

if convert_to_feet and height > 0:
    height_in_feet = height * 3.28084
    st.info(f"Your height in feet is {height_in_feet:.2f} ft")

# Input for weight
weight = st.number_input("Enter your weight in kg", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.2f}")

        # BMI category
        if bmi < 18.5:
            st.warning("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You are normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("You are obese")
    else:
        st.error("Please enter valid weight and height values")