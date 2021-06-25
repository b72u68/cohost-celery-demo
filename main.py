from flask import Flask, flash, render_template, request, redirect, url_for
from tasks import add, subtract, multiply, divide

app = Flask(__name__)
app.config.from_pyfile("config.py")


def get_data(request):
    data = {}

    if not (request.form["first"].strip() and request.form["second"].strip()):
        return None

    data["first"] = int(request.form.get("first"))
    data["second"] = int(request.form.get("second"))

    return data


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            result = add.apply_async(args=[data], duration=20)
            flash("Result: %d + %d = %d" %
                  (data["first"], data["second"], result.get()))

    return redirect(url_for("home"))


@app.route("/subtract", methods=["POST", "GET"])
def subtract_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            result = subtract.apply_async(args=[data], duration=20)
            flash("Result: %d - %d = %d" %
                  (data["first"], data["second"], result.get()))

    return redirect(url_for("home"))


@app.route("/multiply", methods=["POST", "GET"])
def multiply_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            result = multiply.apply_async(args=[data], duration=20)
            flash("Result: %d x %d = %d" %
                  (data["first"], data["second"], result.get()))

    return redirect(url_for("home"))


@app.route("/divide", methods=["POST", "GET"])
def divide_numbers():
    if request.method == "POST":
        data = get_data(request)

        if data:
            result = divide.apply_async(args=[data], duration=20)
            flash("Result: %d ÷  %d = %d" %
                  (data["first"], data["second"], result.get()))

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
