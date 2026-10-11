# ============================================================
# MODULE 5
# Analytics Dashboard
# ============================================================

import pandas as pd
import os


def load_data():

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "urban_traffic_project_dataset.csv"
    )

    return pd.read_csv(file_path)


def get_dashboard_data(data):

    total_records = len(data)


    average_traffic = round(
        data["Traffic_Volume"].mean(),
        2
    )


    low = len(
        data[
            data["Congestion_Level"] == "Low"
        ]
    )


    medium = len(
        data[
            data["Congestion_Level"] == "Medium"
        ]
    )


    high = len(
        data[
            data["Congestion_Level"] == "High"
        ]
    )


    alerts = len(
        data[
            data["Alert"] ==
            "Severe Congestion Alert"
        ]
    )


    junction_data = (

        data

        .groupby("Starting_Road")

        ["Traffic_Volume"]

        .mean()

        .round(2)

        .to_dict()
    )


    return {

        "total_records":
            total_records,

        "average_traffic":
            average_traffic,

        "low":
            low,

        "medium":
            medium,

        "high":
            high,

        "alerts":
            alerts,

        "junction_data":
            junction_data
    }


# ------------------------------------------------------------
# Run Module 5 separately
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("MODULE 5")
    print("Analytics Dashboard")
    print("======================================")

    data = load_data()

    result = get_dashboard_data(data)


    print("\n========== CITY TRAFFIC ANALYTICS ==========")

    print(
        "Total Records:",
        result["total_records"]
    )

    print(
        "Average Traffic:",
        result["average_traffic"]
    )

    print(
        "Low Congestion:",
        result["low"]
    )

    print(
        "Medium Congestion:",
        result["medium"]
    )

    print(
        "High Congestion:",
        result["high"]
    )

    print(
        "Severe Alerts:",
        result["alerts"]
    )


    print("\nJunction-wise Traffic:")

    for junction, traffic in (
        result["junction_data"].items()
    ):

        print(
            junction,
            ":",
            traffic
        )