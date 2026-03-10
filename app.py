import streamlit as st
from predict import predict_price  # import model sudah include auto-download

st.title("💎 Diamond Price Prediction App")
st.write("Masukkan detail diamond:")

# ------------------------------
# USER INPUT
# ------------------------------
carat = st.number_input("Carat", min_value=0.01, value=0.5)
depth = st.number_input("Depth", min_value=0.0, value=61)
table = st.number_input("Table", min_value=0.0, value=55)
x = st.number_input("X (mm)", min_value=0.0, value=5.1)
y = st.number_input("Y (mm)", min_value=0.0, value=5.0)
z = st.number_input("Z (mm)", min_value=0.0, value=3.1)

cut_options = ["Ideal", "Premium", "Very Good", "Good", "Fair"]
cut = st.selectbox("Cut", cut_options)

color_options = ["D","E","F","G","H","I","J"]
color = st.selectbox("Color", color_options)

clarity_options = ["IF","VVS1","VVS2","VS1","VS2","SI1","SI2","I1"]
clarity = st.selectbox("Clarity", clarity_options)

# ------------------------------
# MAP TO DUMMY VARIABLES
# ------------------------------
cut_dict = { "Ideal":"cut_Ideal", "Premium":"cut_Premium", "Very Good":"cut_Very Good", 
             "Good":"cut_Good", "Fair":"cut_Fair" }

color_dict = { "D":"color_D","E":"color_E","F":"color_F","G":"color_G",
               "H":"color_H","I":"color_I","J":"color_J" }

clarity_dict = { "IF":"clarity_IF","VVS1":"clarity_VVS1","VVS2":"clarity_VVS2",
                 "VS1":"clarity_VS1","VS2":"clarity_VS2","SI1":"clarity_SI1",
                 "SI2":"clarity_SI2","I1":"clarity_I1"}

input_data = {
    "carat":carat,
    "depth":depth,
    "table":table,
    "x":x,
    "y":y,
    "z":z,
    cut_dict.get(cut, ""):1,
    color_dict.get(color, ""):1,
    clarity_dict.get(clarity, ""):1
}

# ------------------------------
# PREDICT BUTTON
# ------------------------------
if st.button("Predict Price"):
    price = predict_price(input_data)
    st.success(f"Predicted Diamond Price: ${price:,.2f}")