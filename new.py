from flask import Flask, render_template, url_for, redirect
my=Flask(__name__)

@my.route("/")
def ask():
    return render_template("ask.html")

@my.route("/put/<str:name>")
def main(name):
    return f"Your name is {name}"

@my.route("/aum/<int:a>/<int:b>")
def add(a,b):
    return f"Sum : {a+b}"

@my.route("/new/<str:new>")
def display(new):
    return redirect(url_for("main",name=new))

if __name__=="__main__":
    my.run(debug=True)