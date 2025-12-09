from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained pipeline (preprocessing + model)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Replace with the exact feature names you used in X (df.drop(['AQI'], axis=1))
# Example:
FEATURES = [
    "City",
    "PM2.5", "PM10", "NO2", "SO2", "CO", "O3",
    "Hour", "Month", "Day"
]

def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory / Moderate"
    elif aqi <= 200:
        return "Moderate to Poor"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

# ... existing imports and model loading ...

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    category = None

    if request.method == "POST":
        try:
            city = request.form.get("City")

            pm25 = float(request.form.get("PM2_5"))
            pm10 = float(request.form.get("PM10"))
            no2 = float(request.form.get("NO2"))
            so2 = float(request.form.get("SO2"))
            co = float(request.form.get("CO"))
            o3 = float(request.form.get("O3"))

            latitude = float(request.form.get("Latitude"))
            longitude = float(request.form.get("Longitude"))

            hour = int(request.form.get("Hour"))
            month = int(request.form.get("Month"))
            day = int(request.form.get("Day"))

            data = {
                "City": [city],
                "PM2.5": [pm25],
                "PM10": [pm10],
                "NO2": [no2],
                "SO2": [so2],
                "CO": [co],
                "O3": [o3],
                "Latitude": [latitude],
                "Longitude": [longitude],
                "Hour": [hour],
                "Month": [month],
                "Day": [day]
            }

            input_df = pd.DataFrame(data)
            aqi_value = model.predict(input_df)[0]
            prediction = round(float(aqi_value), 2)
            category = aqi_category(prediction)

        except Exception as e:
            prediction = None
            category = f"Error: {str(e)}"

    return render_template("index.html",
                           prediction=prediction,
                           category=category)


if __name__ == "__main__":
    app.run(debug=True)
