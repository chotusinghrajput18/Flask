from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/mul/<int:x>/<int:y>")
def mul(x, y):
    return f"Result: {x * y}"