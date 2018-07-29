from flask import Flask, jsonify, render_template, request, url_for, redirect

# Initializing all LEDs to be off
current_data = [{"led1": "off", "led2": "off", "led3": "off"}]

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Index Page
@app.route("/")
def index():
    return render_template("index.html")


# Actual site for LED controlling
@app.route("/light")
def light():
    return render_template("light.html")


# Description for the Website
@app.route("/about")
def about():
    return render_template("about.html")


# Route for uploading JSON Data
@app.route("/data", methods=['GET', 'POST'])
def data():

    # Get current LED states from Raspberry Pi
    if request.method == "GET":
        return jsonify(current_data)

    elif request.method == "POST":

        # checking for button press on the form
        for i in range(1, 4):
            key = 'led'
            n = str(i)

            off = 'b' + n + 'off'
            on = 'b' + n + 'on'

            # set state of LED to on
            if request.form[key] == on:
                current_data[0][key + n] = "on"

            # set state of LED to off
            elif request.form[key] == off:
                current_data[0][key + n] = "off"

            else:
                pass

        return redirect("/light")