from flask import Flask,render_template,url_for
from employees import employees_data

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Your name is {name}</h1>"

@app.route("/employees/")
def employees():
    return render_template('employees.html', title="Employees",data=employees_data)

@app.route("/employees/manager")
def manager():
    return render_template('manager.html', title="Manager",data=employees_data)


if __name__=="__main__":
    app.run(debug=True)