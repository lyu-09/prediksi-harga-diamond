import os
import pandas as pd
import joblib
import requests

# ------------------------------
# CONFIG
# ------------------------------
MODEL_PATH = "model_diamond.pkl"
MODEL_URL = "https://drive.google.com/uc?export=download&id=14_boCk2eyAY93kSVP0TSEgW4N5yCAvHb"  # ganti YOUR_FILE_ID

# ------------------------------
# DOWNLOAD MODEL JIKA BELUM ADA
# ------------------------------
if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    try:
        response = requests.get(MODEL_URL, stream=True)
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("Model downloaded!")
    except Exception as e:
        raise RuntimeError(f"Failed to download model: {e}")

# ------------------------------
# LOAD MODEL
# ------------------------------
model = joblib.load(MODEL_PATH)

# ------------------------------
# FUNCTION PREDIKSI
# ------------------------------
def predict_price(input_data: dict):
    """
    input_data: dictionary
    """
    df_input = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    for col, value in input_data.items():
        if col in df_input.columns:
            df_input[col] = value
    return model.predict(df_input)[0]

# ------------------------------
# TEST EXAMPLE
# ------------------------------
if __name__ == "__main__":
    example_input = {
        "carat":0.5, "depth":61, "table":55,
        "x":5.1, "y":5.0, "z":3.1,
        "cut_Ideal":1, "cut_Premium":0,
        "color_E":1, "clarity_VVS1":0
    }
    price = predict_price(example_input)
    print("Predicted Diamond Price:", price)