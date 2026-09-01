from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/mul/<int:x>/<int:y>")
def mul(x, y):
    return f"Result: {x * y}"

@app.route("/myfunc")
def fun():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
