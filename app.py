from flask import Flask, redirect, url_for, render_template
d=Flask(__name__)

@d.route("/hello")
def hello():
    return "Hello World\nHello World\nHello World\nHello World\nHello World\nHello World" 

@d.route("/python/<name>")
def fname(name):
    if name:
        return f"Your name is {name}"
    return 

@d.route("/my/<mob>")
def mobile(mob):
    if mob:
        return f"Your phone No: {mob}"
    return "Nothing to show"

@d.route("/myproject/<na>")
def display(na):
    if na=="chotu":
        return redirect(url_for('fname',name=na))
    else:
        return redirect(url_for('mobile',mob=na))
        

@d.route("/myfunc")
def fun():
    return render_template("index.html")

@d.route("/sub/<int:a>/<int:b>")
def sub(a,b):
    return f"Difference : {a*b}"


@d.route("/mul/<int:a>/<int:b>")
def sub(a,b):
    return f"Difference : {a-b}"

if __name__=="__main__":
    d.run(debug=True)