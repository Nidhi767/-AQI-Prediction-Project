# 🌫️ Air Quality Index (AQI) Prediction System

ML-powered web application that predicts Air Quality Index (AQI) for Indian cities using machine learning (Stacking Ensemble – Random Forest, Gradient Boosting, Extra Trees, XGBoost) and provides a user-friendly Flask interface.

---

## 🔍 Project Overview

This project predicts AQI based on major air pollutants (PM2.5, PM10, NO2, SO2, CO, O3) along with spatial (latitude, longitude) and temporal (hour, month, day) features.  
Two real-world Excel datasets of Indian cities were merged, cleaned, and used to train a machine learning pipeline that is deployed as a Flask web app.

Main goals:
- Build an end‑to‑end ML pipeline: data preprocessing → model training → evaluation → deployment.
- Provide a simple web UI for real‑time AQI prediction.
- Classify AQI into categories such as *Good*, *Satisfactory/Moderate*, *Moderate to Poor*, *Poor*, *Very Poor*, and *Severe*.

---

## 🧠 Machine Learning Approach

- **Datasets**:  
  - `Dataset_AQI4-5.xlsx`  
  - `Dataset_AQI30-4.xlsx`  
  (City-wise AQI and pollutant readings across India)

- **Features**:
  - Categorical: `City`
  - Numeric: `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3`, `Latitude`, `Longitude`, `Hour`, `Month`, `Day`

- **Preprocessing**:
  - Replace `"-"` with `NaN`
  - Convert columns to numeric where possible
  - Parse `Time` to datetime and extract `Hour`, `Month`, `Day`
  - Median imputation for missing numeric values
  - `OneHotEncoder` for `City`
  - `StandardScaler` for numeric features
  - All wrapped in a `ColumnTransformer` + `Pipeline`

- **Models Trained**:
  - RandomForestRegressor
  - GradientBoostingRegressor
  - ExtraTreesRegressor
  - XGBRegressor
  - StackingRegressor (Random Forest + Gradient Boosting + Extra Trees → XGBoost as final estimator)

- **Target**:
  - Continuous AQI value (regression)

---

## 💻 Tech Stack

- **Language**: Python
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `openpyxl`
- **Web Framework**: Flask
- **Frontend**: HTML, CSS, Font Awesome (in `templates/index.html`)
- **Model Persistence**: `pickle` (`model.pkl`)

---

## 🚀 How to Run Locally

1. **Clone the repository**
git clone https://github.com/Nidhi767/-AQI-Prediction-Project.git
cd -AQI-Prediction-Project

2. **Create and activate a virtual environment (optional but recommended)**
python -m venv venv

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the Flask app**
python app.py

5. **Open in browser**

Go to:  
`http://127.0.0.1:5000`

Enter city, pollutant values, latitude/longitude and time → click **Predict AQI** to see predicted value and category.

## 📸 Screenshots
![AQI Predictor UI](Screenshot%202025-12-09%20214220.png)
![Training Output](Screenshot%202025-12-09%20215222.png)

## ✨ Future Improvements

- Deploy on a cloud platform (Render / Railway / Heroku).
- Add city dropdown with predefined locations.
- Add historical AQI plots and explainable feature importance.
- Extend to forecasting (predict future AQI using time-series models).

---

## 🙌 Credits

- Developed by Nidhi as part of **Infosys Springboard Virtual Internship 6.0**.  
- Datasets: Publicly available Indian city AQI measurements.

