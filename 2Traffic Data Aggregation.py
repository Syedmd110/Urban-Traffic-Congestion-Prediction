# ============================================================
# MODULE 2
# Traffic Data Aggregation
# ============================================================

import pandas as pd
import os


def load_traffic_data():

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "urban_traffic_project_dataset.csv"
    )

    data = pd.read_csv(file_path)

    return data


def get_total_records(data):

    return len(data)


def get_average_traffic(data):

    return round(
        data["Traffic_Volume"].mean(),
        2
    )


def get_vehicle_summary(data):

    return data.groupby(
        "Vehicle_Type"
    )["Traffic_Volume"].mean().round(2)


def get_junction_summary(data):

    return data.groupby(
        "Starting_Road"
    )["Traffic_Volume"].mean().round(2)


# ------------------------------------------------------------
# Run Module 2 separately
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("MODULE 2")
    print("Traffic Data Aggregation")
    print("======================================")

    data = load_traffic_data()

    print("\nDataset loaded successfully.")

    print(
        "\nTotal Traffic Records:",
        get_total_records(data)
    )

    print(
        "Average Traffic Volume:",
        get_average_traffic(data)
    )

    print("\nVehicle-wise Traffic:")
    print(get_vehicle_summary(data))

    print("\nStarting Road-wise Traffic:")
    print(get_junction_summary(data))

    print("\nFirst 5 Records:")
    print(data.head())