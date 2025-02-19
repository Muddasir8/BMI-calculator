import streamlit as st

st.title("BMI Calculator & Health Tips 💪")

# User Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=50.0, step=0.1)

if weight and height:
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    
    # Display BMI
    st.subheader(f"Your BMI: {bmi:.2f}")

    # Show progress bar based on BMI range
    st.progress(min(int(bmi * 2), 100))  

    # Health Advice
    if bmi < 18.5:
        st.warning("You're underweight. Consider a balanced, calorie-rich diet.")
    elif 18.5 <= bmi < 24.9:
        st.success("Great! You have a normal BMI. Maintain a healthy lifestyle.")
    elif 25 <= bmi < 29.9:
        st.warning("You're overweight. Regular exercise and a balanced diet are recommended.")
    else:
        st.error("You're in the obese category. Consult a health professional.")

st.write("Stay fit and healthy! 🏋️‍♂️")