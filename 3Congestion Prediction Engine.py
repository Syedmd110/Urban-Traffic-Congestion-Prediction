# ============================================================
# MODULE 3
# Congestion Prediction Engine
# ============================================================

import pandas as pd
import os

from sklearn.ensemble import RandomForestRegressor


def load_data():

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "urban_traffic_project_dataset.csv"
    )

    return pd.read_csv(file_path)


def train_model(data):

    data = data.copy()

    data["Date"] = pd.to_datetime(data["Date"])

    data["Year"] = data["Date"].dt.year
    data["Month"] = data["Date"].dt.month
    data["Day"] = data["Date"].dt.day
    data["DayOfWeek"] = data["Date"].dt.dayofweek

    data["Hour"] = (
        data["Travel_Time"]
        .str.split(":")
        .str[0]
        .astype(int)
    )

    features = [
        "Year",
        "Month",
        "Day",
        "DayOfWeek",
        "Hour",
        "Vehicle_Type",
        "Starting_Road",
        "Destination_Road"
    ]

    X = data[features]

    y = data["Traffic_Volume"]

    X = pd.get_dummies(X)

    model = RandomForestRegressor(
        n_estimators=50,
        random_state=42
    )

    model.fit(X, y)

    return model, X.columns


def predict_traffic(
    model,
    model_columns,
    date,
    time,
    vehicle_type,
    start,
    destination
):

    date = pd.to_datetime(date)

    hour = int(time.split(":")[0])

    input_data = pd.DataFrame([{

        "Year": date.year,

        "Month": date.month,

        "Day": date.day,

        "DayOfWeek": date.dayofweek,

        "Hour": hour,

        "Vehicle_Type": vehicle_type,

        "Starting_Road": start,

        "Destination_Road": destination

    }])

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(
        columns=model_columns,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]

    prediction = round(prediction, 2)

    # Congestion classification

    if prediction < 20:

        congestion = "Low"

    elif prediction < 40:

        congestion = "Medium"

    else:

        congestion = "High"


    # Alert generation

    if congestion == "High":

        alert = "Severe Congestion Alert"

    elif congestion == "Medium":

        alert = "Moderate Traffic"

    else:

        alert = "Traffic is Normal"


    return prediction, congestion, alert


# ------------------------------------------------------------
# Run Module 3 separately
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("MODULE 3")
    print("Congestion Prediction Engine")
    print("======================================")

    data = load_data()

    print("\nTraining Machine Learning model...")

    model, columns = train_model(data)

    print("Model trained successfully.")

    print("\nEnter journey details")

    vehicle_type = input(
        "Vehicle Type (Car/Bike/Bus/Auto): "
    )

    start = input(
        "Starting Road: "
    )

    destination = input(
        "Destination Road: "
    )

    date = input(
        "Date (YYYY-MM-DD): "
    )

    time = input(
        "Time (HH:MM): "
    )


    prediction, congestion, alert = predict_traffic(

        model,

        columns,

        date,

        time,

        vehicle_type,

        start,

        destination
    )


    print("\n========== PREDICTION ==========")

    print(
        "Predicted Traffic Volume:",
        prediction
    )

    print(
        "Congestion Level:",
        congestion
    )

    print(
        "Alert:",
        alert
    )