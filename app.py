from flask import Flask, request, redirect, session
import importlib.util
import os

app = Flask(__name__)
app.secret_key = "urban_traffic_project"


# ============================================================
# LOAD PROJECT MODULES
# ============================================================

def load_module(file_name):

    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        file_name
    )

    module_name = file_name.replace(".py", "").replace(" ", "_")

    spec = importlib.util.spec_from_file_location(
        module_name,
        path
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


module1 = load_module(
    "1Authentication & Role Management.py"
)

module2 = load_module(
    "2Traffic Data Aggregation.py"
)

module3 = load_module(
    "3Congestion Prediction Engine.py"
)

module4 = load_module(
    "4Route Recommendation Service.py"
)

module5 = load_module(
    "5Analytics Dashboard.py"
)


# ============================================================
# LOAD DATASET
# ============================================================

data = module2.load_traffic_data()


# ============================================================
# TRAIN MODEL
# ============================================================

model, model_columns = module3.train_model(data)


# ============================================================
# COMMON DESIGN
# ============================================================

CSS = """
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #dbeafe, #e0f2fe);
    color: #172033;
}

.nav {
    background: linear-gradient(90deg, #0f172a, #0369a1);
    color: white;
    padding: 20px 30px;
}

.nav h2 {
    display: inline;
    margin: 0;
}

.nav a {
    float: right;
    color: white;
    text-decoration: none;
    margin-left: 15px;
}

.container {
    max-width: 1100px;
    margin: 30px auto;
    padding: 20px;
}

.card {
    background: white;
    padding: 25px;
    margin-bottom: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.10);
}

input,
select {
    width: 100%;
    padding: 13px;
    margin-top: 7px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 15px;
}

label {
    display: block;
    margin-top: 18px;
    font-weight: bold;
}

button {
    width: 100%;
    padding: 14px;
    margin-top: 25px;
    border: none;
    border-radius: 8px;
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.button {
    display: inline-block;
    padding: 12px 18px;
    margin: 5px;
    background: #2563eb;
    color: white;
    text-decoration: none;
    border-radius: 8px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.item {
    background: #f1f5f9;
    padding: 15px;
    border-radius: 9px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.stat {
    background: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
}

.number {
    font-size: 32px;
    font-weight: bold;
}

.blue {
    border-top: 6px solid #2563eb;
}

.green {
    border-top: 6px solid #16a34a;
}

.yellow {
    border-top: 6px solid #f59e0b;
}

.red {
    border-top: 6px solid #dc2626;
}

.info {
    background: #e0f2fe;
    border-left: 5px solid #0284c7;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
}

.alert {
    background: #fee2e2;
    border-left: 6px solid #dc2626;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

.route {
    background: #f8fafc;
    padding: 20px;
    margin: 12px 0;
    border-left: 5px solid #0284c7;
    border-radius: 9px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #0f172a;
    color: white;
}

th,
td {
    padding: 14px;
    border-bottom: 1px solid #ddd;
    text-align: left;
}

.login-box {
    width: 420px;
    max-width: 92%;
    margin: 45px auto;
    background: white;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

.header {
    background: linear-gradient(135deg, #0f172a, #0369a1);
    color: white;
    text-align: center;
    padding: 35px 20px;
}

.logo {
    font-size: 50px;
}

.demo {
    margin-top: 20px;
    padding: 15px;
    background: #eff6ff;
    border-radius: 10px;
    color: #1e40af;
}

.prediction {
    text-align: center;
    padding: 30px;
    border-radius: 15px;
}

.prediction-number {
    font-size: 45px;
    font-weight: bold;
}

.prediction-level {
    font-size: 25px;
    font-weight: bold;
}

@media(max-width:700px) {

    .cards {
        grid-template-columns: 1fr;
    }

    .grid {
        grid-template-columns: 1fr;
    }

}

</style>
"""


# ============================================================
# LOGIN PAGE
# ============================================================

@app.route("/")
def home():

    return """
<!DOCTYPE html>

<html>

<head>

<title>
Urban Traffic Login
</title>

""" + CSS + """

</head>

<body>


<div class="header">

<div class="logo">
🚦
</div>

<h1>
Urban Traffic
</h1>

<p>
Congestion Prediction Platform
</p>

<p>
Smart Roads • Smarter Travel
</p>

</div>


<div class="login-box">

<h2>
Welcome 👋
</h2>

<p>
Login to plan your journey
</p>


<form action="/login" method="post">


<input
type="text"
name="username"
placeholder="Enter Username"
required
>


<input
type="password"
name="password"
placeholder="Enter Password"
required
>


<select name="role">

<option>
User / Student
</option>

<option>
Traffic Authority
</option>

</select>


<button type="submit">

🔐 Login

</button>


</form>


<div class="demo">

<b>
Demo Login
</b>

<br><br>

👨‍🎓 Student:
student / student123

<br><br>

👮 Authority:
admin / admin123

</div>


</div>

</body>

</html>
"""


# ============================================================
# LOGIN
# ============================================================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"].strip()

    password = request.form["password"].strip()

    role = request.form["role"].strip()


    # --------------------------------------------------------
    # STUDENT LOGIN
    # --------------------------------------------------------

    if (
        username == "student"
        and password == "student123"
        and role == "User / Student"
    ):

        session["username"] = username

        session["role"] = role

        return redirect("/journey")


    # --------------------------------------------------------
    # AUTHORITY LOGIN
    # --------------------------------------------------------

    if (
        username == "admin"
        and password == "admin123"
        and role == "Traffic Authority"
    ):

        session["username"] = username

        session["role"] = role

        return redirect("/authority")


    # --------------------------------------------------------
    # WRONG LOGIN
    # --------------------------------------------------------

    return """
<!DOCTYPE html>

<html>

<body style="
font-family:Arial;
text-align:center;
padding:80px;
background:#fee2e2;
">

<h1 style="color:#dc2626;">
❌ Login Failed
</h1>

<p>
Username, password or role is incorrect.
</p>

<a href="/">
← Back to Login
</a>

</body>

</html>
"""


# ============================================================
# STUDENT JOURNEY INPUT
# ============================================================

@app.route("/journey")
def journey():

    if "username" not in session:

        return redirect("/")


    if session["role"] != "User / Student":

        return redirect("/authority")


    return """
<!DOCTYPE html>

<html>

<head>

<title>
Plan Your Journey
</title>

""" + CSS + """

</head>


<body>


<div class="nav">

<h2>
🚦 Urban Traffic
</h2>

<a href="/logout">
Logout
</a>

</div>


<div class="container">

<div class="card">

<h1>
🛣️ Plan Your Journey
</h1>


<div class="info">

Enter your journey details.

The historical traffic dataset will be used
to predict the traffic condition.

</div>


<form action="/predict" method="post">


<label>
🚗 Vehicle Number
</label>

<input
type="text"
name="vehicle_number"
placeholder="Example: TS09AB1234"
required
>


<label>
🚘 Vehicle Type
</label>

<select name="vehicle_type">

<option>
Car
</option>

<option>
Bike
</option>

<option>
Bus
</option>

<option>
Auto
</option>

</select>


<label>
📍 Starting Point
</label>

<select name="start">

<option>
Central Market
</option>

<option>
City Mall
</option>

<option>
Railway Station
</option>

<option>
Bus Terminal
</option>

</select>


<label>
🎯 Destination
</label>

<select name="destination">

<option>
City Mall
</option>

<option>
Railway Station
</option>

<option>
Bus Terminal
</option>

<option>
Central Market
</option>

</select>


<label>
📅 Travel Date
</label>

<input
type="date"
name="date"
required
>


<label>
🕐 Travel Time
</label>

<input
type="time"
name="time"
required
>


<button type="submit">

🔍 Predict My Traffic

</button>


</form>

</div>

</div>

</body>

</html>
"""


# ============================================================
# PREDICTION RESULT
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    if "username" not in session:

        return redirect("/")


    if session["role"] != "User / Student":

        return redirect("/authority")


    vehicle_number = request.form["vehicle_number"]

    vehicle_type = request.form["vehicle_type"]

    start = request.form["start"]

    destination = request.form["destination"]

    date = request.form["date"]

    time = request.form["time"]


    # --------------------------------------------------------
    # MACHINE LEARNING PREDICTION
    # --------------------------------------------------------

    prediction, congestion, alert = module3.predict_traffic(

        model,

        model_columns,

        date,

        time,

        vehicle_type,

        start,

        destination

    )


    # --------------------------------------------------------
    # ALTERNATE ROUTE
    # --------------------------------------------------------

    routes = module4.recommend_routes(

        data,

        start,

        destination

    )


    # --------------------------------------------------------
    # CONGESTION COLOUR
    # --------------------------------------------------------

    if congestion == "Low":

        color = "#16a34a"

        background = "#dcfce7"

        icon = "🟢"


    elif congestion == "Medium":

        color = "#d97706"

        background = "#fef3c7"

        icon = "🟡"


    else:

        color = "#dc2626"

        background = "#fee2e2"

        icon = "🔴"


    # --------------------------------------------------------
    # ROUTE DISPLAY
    # --------------------------------------------------------

    route_html = ""


    if len(routes) == 0:

        route_html = """

<div class="info">

ℹ️ No alternate route information
is available.

</div>

"""


    else:

        for i, route in enumerate(routes, 1):

            if route["congestion"] == "Low":

                route_icon = "🟢"

            elif route["congestion"] == "Medium":

                route_icon = "🟡"

            else:

                route_icon = "🔴"


            route_html += """

<div class="route">

<h3>

""" + route_icon + """

Alternate Route """ + str(i) + """

</h3>


<p>

🛣️ Road:

<b>
""" + str(route["road"]) + """
</b>

</p>


<p>

📊 Traffic:

<b>
""" + str(route["traffic"]) + """
</b>

</p>


<p>

Congestion:

<b>
""" + str(route["congestion"]) + """
</b>

</p>

</div>

"""


    return """
<!DOCTYPE html>

<html>

<head>

<title>
Traffic Prediction Result
</title>

""" + CSS + """

</head>


<body>


<div class="nav">

<h2>
🚦 Urban Traffic
</h2>

<a href="/logout">
Logout
</a>

</div>


<div class="container">


<div class="card">

<h1>

""" + icon + """

Traffic Prediction Result

</h1>

<p>
Your journey analysis is ready.
</p>

</div>


<div class="card">

<h2>
🛣️ Your Journey
</h2>


<div class="grid">


<div class="item">

<b>
🚗 Vehicle Number
</b>

<br><br>

""" + vehicle_number + """

</div>


<div class="item">

<b>
🚘 Vehicle Type
</b>

<br><br>

""" + vehicle_type + """

</div>


<div class="item">

<b>
📍 Starting Point
</b>

<br><br>

""" + start + """

</div>


<div class="item">

<b>
🎯 Destination
</b>

<br><br>

""" + destination + """

</div>


<div class="item">

<b>
📅 Date
</b>

<br><br>

""" + date + """

</div>


<div class="item">

<b>
🕐 Time
</b>

<br><br>

""" + time + """

</div>


</div>

</div>


<div class="card">

<h2>
📊 Traffic Prediction
</h2>


<div
class="prediction"
style="background:""" + background + """;"
>


<div
class="prediction-number"
style="color:""" + color + """;"
>

""" + str(prediction) + """

</div>


<p>
Predicted Traffic Volume
</p>


<div
class="prediction-level"
style="color:""" + color + """;"
>

""" + icon + """

""" + congestion + """

Congestion

</div>


<div class="alert">

⚠️ """ + alert + """

</div>


</div>

</div>


<div class="card">

<h2>
🛣️ Alternate Routes
</h2>

<p>
Suggested using historical traffic information.
</p>

""" + route_html + """

</div>


<div class="card">

<a
class="button"
href="/journey"
>

🔄 New Journey

</a>


<a
class="button"
href="/analytics"
>

📈 View Analytics

</a>


<a
class="button"
href="/logout"
>

🚪 Logout

</a>

</div>


</div>

</body>

</html>
"""


# ============================================================
# TRAFFIC AUTHORITY DASHBOARD
# ============================================================

@app.route("/authority")
def authority():

    if "username" not in session:

        return redirect("/")


    if session["role"] != "Traffic Authority":

        return redirect("/journey")


    result = module5.get_dashboard_data(data)


    return """
<!DOCTYPE html>

<html>

<head>

<title>
Traffic Authority Dashboard
</title>

""" + CSS + """

</head>


<body>


<div
class="nav"
style="background:linear-gradient(90deg,#7f1d1d,#dc2626);"
>

<h2>
🚨 Traffic Authority
</h2>

<a href="/logout">
Logout
</a>

</div>


<div class="container">


<div class="card">

<h1 style="color:#991b1b;">

🚦 Authority Control Dashboard

</h1>


<p>

Welcome,

<b>
""" + session["username"] + """
</b>

</p>


<p>

Monitor traffic congestion
and severe congestion alerts.

</p>

</div>


<div class="cards">


<div class="stat blue">

<h3>
📁 Total Traffic Records
</h3>

<div class="number">

""" + str(result["total_records"]) + """

</div>

</div>


<div class="stat yellow">

<h3>
🟡 Medium Congestion
</h3>

<div class="number">

""" + str(result["medium"]) + """

</div>

</div>


<div class="stat red">

<h3>
🔴 High Congestion
</h3>

<div class="number">

""" + str(result["high"]) + """

</div>

</div>


</div>


<div class="alert">

<h2>
🚨 Severe Congestion Alerts
</h2>


<p>

The historical dataset contains

<b>
""" + str(result["alerts"]) + """
</b>

high-congestion records.

</p>


<p>

Traffic authorities can use this
information to monitor congestion.

</p>

</div>


<div class="card">

<h2>
📊 Traffic Monitoring
</h2>


<p>

Average Traffic Volume:

<b>
""" + str(result["average_traffic"]) + """
</b>

</p>


<p>

🟢 Low:

<b>
""" + str(result["low"]) + """
</b>

&nbsp;&nbsp;

🟡 Medium:

<b>
""" + str(result["medium"]) + """
</b>

&nbsp;&nbsp;

🔴 High:

<b>
""" + str(result["high"]) + """
</b>

</p>


<a
class="button"
href="/analytics"
>

📈 Open Full Analytics

</a>


</div>


</div>

</body>

</html>
"""


# ============================================================
# ANALYTICS DASHBOARD
# ============================================================

@app.route("/analytics")
def analytics():

    if "username" not in session:

        return redirect("/")


    result = module5.get_dashboard_data(data)


    rows = ""


    for junction, traffic in result["junction_data"].items():

        rows += """

<tr>

<td>
""" + str(junction) + """
</td>

<td>
""" + str(traffic) + """
</td>

</tr>

"""


    return """
<!DOCTYPE html>

<html>

<head>

<title>
Traffic Analytics
</title>

""" + CSS + """

</head>


<body>


<div class="nav">

<h2>
🚦 Urban Traffic
</h2>

<a href="/logout">
Logout
</a>

</div>


<div class="container">


<div class="card">

<h1>
📈 City Traffic Analytics
</h1>

<p>
City-wide traffic overview
</p>

</div>


<div class="cards">


<div class="stat blue">

<h3>
📁 Total Records
</h3>

<div class="number">

""" + str(result["total_records"]) + """

</div>

</div>


<div class="stat blue">

<h3>
📊 Average Traffic
</h3>

<div class="number">

""" + str(result["average_traffic"]) + """

</div>

</div>


<div class="stat green">

<h3>
🟢 Low Congestion
</h3>

<div class="number">

""" + str(result["low"]) + """

</div>

</div>


<div class="stat yellow">

<h3>
🟡 Medium Congestion
</h3>

<div class="number">

""" + str(result["medium"]) + """

</div>

</div>


<div class="stat red">

<h3>
🔴 High Congestion
</h3>

<div class="number">

""" + str(result["high"]) + """

</div>

</div>


<div class="stat red">

<h3>
🚨 Severe Alerts
</h3>

<div class="number">

""" + str(result["alerts"]) + """

</div>

</div>


</div>


<div class="card">

<h2>
🛣️ Junction-wise Traffic
</h2>


<table>

<tr>

<th>
Starting Road / Junction
</th>

<th>
Average Traffic
</th>

</tr>

""" + rows + """

</table>


<br>


<a
class="button"
href="/journey"
>

🔄 Plan New Journey

</a>


</div>


</div>

</body>

</html>
"""


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ============================================================
# START PROJECT
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=False,
        port=5000
    )