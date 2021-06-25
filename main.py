from flask import Flask, flash, render_template, request, redirect, url_for
from tasks import add

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        data = {}

        data["first"] = int(request.form.get("first"))
        data["second"] = int(request.form.get("second"))

        result = add.apply_async(args=[data], duration=20)
        flash(f"Result: {data['first']} + {data['second']} = {result.get()}")

        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
