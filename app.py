
import streamlit as st
import pickle
import numpy as np

# Load trained model and scaler
model = pickle.load(open("classifier.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Kidney Disease Prediction", layout="centered")
st.title("🩺 Kidney Disease Prediction App")

st.markdown("Enter patient information to predict the risk of **Kidney Disease**.")

# Input features
age = st.number_input("Age", min_value=0.0)
bp = st.number_input("Blood Pressure", min_value=0.0)
sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
al = st.selectbox("Albumin", [0, 1, 2, 3, 4, 5])
su = st.selectbox("Sugar", [0, 1, 2, 3, 4, 5])
rbc = st.selectbox("Red Blood Cells", ['normal', 'abnormal'])
pc = st.selectbox("Pus Cell", ['normal', 'abnormal'])
pcc = st.selectbox("Pus Cell clumps", ['present', 'notpresent'])
ba = st.selectbox("Bacteria", ['present', 'notpresent'])
bgr = st.number_input("Blood Glucose Random", min_value=0.0)
bu = st.number_input("Blood Urea", min_value=0.0)
sc = st.number_input("Serum Creatinine", min_value=0.0)
sod = st.number_input("Sodium", min_value=0.0)
pot = st.number_input("Potassium", min_value=0.0)
hemo = st.number_input("Hemoglobin", min_value=0.0)
pcv = st.number_input("Packed Cell Volume", min_value=0.0)
wc = st.number_input("White Blood Cell Count", min_value=0.0)
rc = st.number_input("Red Blood Cell Count", min_value=0.0)
htn = st.selectbox("Hypertension", ['yes', 'no'])
dm = st.selectbox("Diabetes Mellitus", ['yes', 'no'])
cad = st.selectbox("Coronary Artery Disease", ['yes', 'no'])
appet = st.selectbox("Appetite", ['good', 'poor'])
pe = st.selectbox("Pedal Edema", ['yes', 'no'])
ane = st.selectbox("Anemia", ['yes', 'no'])

if st.button("Predict"):
    # Categorical mapping
    rbc = 1 if rbc == 'normal' else 0
    pc = 1 if pc == 'normal' else 0
    pcc = 1 if pcc == 'present' else 0
    ba = 1 if ba == 'present' else 0
    htn = 1 if htn == 'yes' else 0
    dm = 1 if dm == 'yes' else 0
    cad = 1 if cad == 'yes' else 0
    appet = 1 if appet == 'good' else 0
    pe = 1 if pe == 'yes' else 0
    ane = 1 if ane == 'yes' else 0

    input_data = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr,
                            bu, sc, sod, pot, hemo, pcv, wc, rc,
                            htn, dm, cad, appet, pe, ane]])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🩸 The patient is likely to have **Kidney Disease**.")
    else:
        st.info("✅ The patient is **not likely** to have Kidney Disease.")
