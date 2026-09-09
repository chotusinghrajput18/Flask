from flask import Flask, redirect, url_for, render_template
d=Flask(__name__)

@d.route("/hello",methods=["GET"])
def hello():
    return "Hello World\nHello World" 

@d.route("/python/<name>", methods=["GET"])
def fname(name):
    if name:
        return f"Your name is {name}"
    return 

@d.route("/my/<mob>", methods=["GET"])
def mobile(mob):
    if mob:
        return f"Your phone No: {mob}"
    return "Nothing to show"

@d.route("/myproject/<na>", methods=["GET"])
def display(na):
    if na=="chotu":
        return redirect(url_for('fname',name=na))
    else:
        return redirect(url_for('mobile',mob=na))

@d.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a,b):
    return f"Sum : {a+b}"

@d.route("/div/<int:a>/<int:b>", methods=["GET"])
def div(a,b):
    if b != 0:
        return f"Result: {a / b}"
    else:
        return "Error: Division by zero is not allowed."    
@d.route("/myfunc", methods=["GET"])
def fun():
    return render_template("index.html")

@d.route("/sub/<int:a>/<int:b>", methods=["GET"])
def sub(a,b):
    return f"Difference : {a-b}"

@d.route("/mul/<int:a>/<int:b>", methods=["GET"])
def mul(a,b):
    return f"Product : {a*b}"

@d.route("/mod/<int:a>/<int:b>", methods=["GET"])
def mod(a,b):
    if b != 0:
        return f"Result: {a % b}"
    else:
        return "Error: Modulus by zero is not allowed."

@d.route("/pow/<int:a>/<int:b>", methods=["GET"])
def power(a,b):
    return f"Result: {a ** b}"

@d.route("/floor/<int:a>/<int:b>", methods=["GET"])
def floor_div(a,b):
    if b != 0:
        return f"Result: {a // b}"
    else:
        return "Error: Floor division by zero is not allowed."

@d.route("/home",methods=["GET","POST"])
def home_page():
    return render_template("index.html")

@d.route("/redirect", methods=["GET"])
def redirect_to_mul():
    return redirect(url_for("mul", a=5, b=10))

if __name__=="__main__":
    d.run(debug=True)