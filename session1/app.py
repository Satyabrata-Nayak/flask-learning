from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to HomePage</h1>"

@app.route('/about')
def about():
    return "<h1>Welcome to about Page</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Your name is {name}</h1>"


if __name__=="__main__":
    app.run(debug=True)