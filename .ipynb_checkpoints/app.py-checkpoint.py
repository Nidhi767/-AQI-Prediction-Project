from flask import Flask, request, render_template
import pickle
import pandas as pd
from datetime import datetime

# ---------------------------------
# City → Coordinates Dictionary
# ---------------------------------
city_coordinates = {
    "Delhi": (28.7041, 77.1025),
    "New Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Pune": (18.5204, 73.8567),
    "Jaipur": (26.9124, 75.7873),
    "Ahmedabad": (23.0225, 72.5714),
    "Lucknow": (26.8467, 80.9462),
    "Surat": (21.1702, 72.8311),
    "Bhopal": (23.2599, 77.4126),
    "Indore": (22.7196, 75.8577),
    "Nagpur": (21.1458, 79.0882),
    "Patna": (25.5941, 85.1376),
    "Chandigarh": (30.7333, 76.7794),
    "Gurgaon": (28.4595, 77.0266),
    "Noida": (28.5355, 77.3910),
    "Faridabad": (28.4089, 77.3178),
    "Ghaziabad": (28.6692, 77.4538)
}

app = Flask(__name__)

# -----------------------------
# Load Model
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        city = request.form.get("City")
        pm25 = request.form.get("PM2.5")
        pm10 = request.form.get("PM10")
        o3 = request.form.get("O3")
        no2 = request.form.get("NO2")
        so2 = request.form.get("SO2")
        co = request.form.get("CO")
        time_value = request.form.get("Time")

        print("FORM DATA RECEIVED:", request.form)

        if city not in city_coordinates:
            return f"<h3>Error: City '{city}' not found in database.</h3>"

        lat, lon = city_coordinates[city]

        # Convert datetime-local → normal datetime string
        if "T" in time_value:
            time_value = time_value.replace("T", " ") + ":00"

        # Must match EXACT column names your model was trained on
        features = {
            "City": city,
            "PM2.5": float(pm25),
            "PM10": float(pm10),
            "O3": float(o3),
            "NO2": float(no2),
            "SO2": float(so2),
            "CO": float(co),
            "Latitude": lat,
            "Longitude": lon,
            "Time": time_value
        }

        df = pd.DataFrame([features])

        print("DataFrame Columns:", df.columns)

        prediction = model.predict(df)[0]

        return f"<h2 style='text-align:center;'>Predicted AQI: {prediction:.2f}</h2>"

    except Exception as e:
        return f"<h3>Error Occurred: {str(e)}</h3>"


if __name__ == "__main__":
    app.run(debug=True)

