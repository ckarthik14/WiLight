from flask import Flask, jsonify, render_template, request, url_for, redirect

current_data = [{"led1":"off", "led2":"off", "led3":"off"}]

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=['GET','POST'])
def data():

    if request.method == "GET":
        return jsonify(current_data)

    elif request.method == "POST":

        for i in range(1,4):
            print('shit', i)
            key = 'led'
            n = str(i)

            off = 'b' + n + 'off'
            on = 'b' + n + 'on'

            if request.form[key] == on:
                current_data[0][key + n] = "on"

            elif request.form[key] == off:
                current_data[0][key + n] = "off"

            else:
                pass

        return redirect("/")

