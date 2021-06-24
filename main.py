from flask import Flask, flash, render_template, request, redirect, url_for
from celery import Celery

app = Flask(__name__)
client = Celery(app.name,
                broker="redis://localhost:6379/0",
                backend="redis://localhost:6379/0")


@client.task
def add(data):
    return data["first"] + data["second"]


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        data = {}

        data["first"] = int(request.form.get("first"))
        data["second"] = int(request.form.get("second"))

        flash(add.apply_async(args=[data], duration=20))
        flash("Numbers added!")

        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
