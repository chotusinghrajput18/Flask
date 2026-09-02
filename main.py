from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/mul/<int:x>/<int:y>")
def mul(x, y):
    return f"Result: {x * y}"

@app.route("/myfunc")
def fun():
    return render_template("index.html")

@app.route("/redirect")
def redirect_to_mul():
    return redirect(url_for("mul", x=5, y=10))

@app.route("/redirect2/<int:x>/<int:y>", methods=["GET"])
def redirect_to_mul_with_params(x, y):
    return redirect(url_for("mul", x=x, y=y))

if __name__ == "__main__":
    app.run(debug=True)
