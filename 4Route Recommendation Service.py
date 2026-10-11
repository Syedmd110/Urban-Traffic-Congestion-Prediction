# ============================================================
# MODULE 4
# Route Recommendation Service
# ============================================================

import pandas as pd
import os


def load_data():

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "urban_traffic_project_dataset.csv"
    )

    return pd.read_csv(file_path)


def recommend_routes(
    data,
    start,
    destination
):

    route_data = data[
        (data["Starting_Road"] == start) &
        (data["Destination_Road"] == destination)
    ]

    if len(route_data) == 0:

        return []


    recommendations = (

        route_data

        .groupby(
            [
                "Alternate_Junction",
                "Alternate_Road"
            ]
        )

        ["Traffic_Volume"]

        .mean()

        .reset_index()
    )


    recommendations = recommendations.sort_values(
        "Traffic_Volume"
    )


    result = []


    for _, row in recommendations.head(3).iterrows():

        traffic = round(
            row["Traffic_Volume"],
            2
        )


        if traffic < 20:

            level = "Low"

        elif traffic < 40:

            level = "Medium"

        else:

            level = "High"


        result.append({

            "junction":
                row["Alternate_Junction"],

            "road":
                row["Alternate_Road"],

            "traffic":
                traffic,

            "congestion":
                level
        })


    return result


# ------------------------------------------------------------
# Run Module 4 separately
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("MODULE 4")
    print("Route Recommendation Service")
    print("======================================")

    data = load_data()

    start = input(
        "Starting Road: "
    )

    destination = input(
        "Destination Road: "
    )


    routes = recommend_routes(
        data,
        start,
        destination
    )


    print("\n========== ALTERNATE ROUTES ==========")


    if len(routes) == 0:

        print(
            "No alternate route data found."
        )

    else:

        for i, route in enumerate(
            routes,
            1
        ):

            print("\nRoute", i)

            print(
                "Junction:",
                route["junction"]
            )

            print(
                "Road:",
                route["road"]
            )

            print(
                "Traffic:",
                route["traffic"]
            )

            print(
                "Congestion:",
                route["congestion"]
            )