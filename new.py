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

@my.route("/home")
def home():
    return redirect(url_for("ask"))

@my.route("/about")
def about():
    return redirect(url_for("ask"))

@my.route("/contact")
def contact():
    return redirect(url_for("ask"))

@my.route("/help")
def help():
    return redirect(url_for("ask"))

@my.route("/services")
def services():
    return redirect(url_for("ask"))

@my.route("/products/<item>")
def products(item):
    return redirect(url_for("main",name=item))

@my.route("/products/<item>/<int:quantity>")
def products_quantity(item, quantity):
    return redirect(url_for("main", name=f"{item} (Quantity: {quantity})"))

@my.route("/services/<service>/<int:level>")
def services_level(service, level):
    return redirect(url_for("main", name=f"{service} (Level: {level})"))

@my.route("/services/<service>")
def service(service):
    return redirect(url_for("main",name=service))

@my.route("/div/<int:x>/<int:y>")
def div(x, y):
    if y != 0:
        return f"Result: {x / y}"
    else:
        return "Error: Division by zero is not allowed."

@my.route("/sub/<int:x>/<int:y>")
def sub(x, y):
    return f"Result: {x - y}"

@my.route("/mul/<int:x>/<int:y>")
def mul(x, y):
    return f"Result: {x * y}"

@my.route("/mod/<int:x>/<int:y>")
def mod(x, y):  
    if y != 0:
        return f"Result: {x % y}"
    else:
        return "Error: Modulus by zero is not allowed."

@my.route("/pow/<int:x>/<int:y>", methods=["GET"])
def power(x, y):
    return f"Result: {x ** y}"

@my.route("/floor/<int:x>/<int:y>")
def floor_div(x, y):
    if y != 0:
        return f"Result: {x // y}"
    else:
        return "Error: Floor division by zero is not allowed."

if __name__=="__main__":
    my.run(debug=True)