from flask import Flask, flash, render_template, request, redirect, url_for
from celery import Celery

app = Flask(__name__)
app.config.from_object("config")

client = Celery(app.name,
                broker=app.config['CELERY_BROKER_URL'],
                backend=app.config['CELERY_RESULT_BACKEND'])
client.conf.update(app.config)


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
