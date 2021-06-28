from config import Config
from flask import Flask, flash, render_template, request, redirect, url_for
from tasks import add, subtract, multiply, divide

app = Flask(__name__)
app.config["SECRET_KEY"] = Config.FLASK_SECRET_KEY


def get_data(request):
    if not (request.form["first"].strip() and request.form["second"].strip()):
        return None

    return [int(request.form.get("first")), int(request.form.get("second"))]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            task = add.apply_async(args=data, duration=20)
            flash("Result: %d + %d = %d" %
                  (data[0], data[1], task.get()))

    return redirect(url_for("home"))


@app.route("/subtract", methods=["POST", "GET"])
def subtract_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            task = subtract.apply_async(args=data, duration=20)
            flash("Result: %d - %d = %d" %
                  (data[0], data[1], task.get()))

    return redirect(url_for("home"))


@app.route("/multiply", methods=["POST", "GET"])
def multiply_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            task = multiply.apply_async(args=data, duration=20)
            flash("Result: %d x %d = %d" %
                  (data[0], data[1], task.get()))

    return redirect(url_for("home"))


@app.route("/divide", methods=["POST", "GET"])
def divide_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            task = divide.apply_async(args=data, duration=20)
            flash("Result: %d ÷  %d = %d" %
                  (data[0], data[1], task.get()))

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
