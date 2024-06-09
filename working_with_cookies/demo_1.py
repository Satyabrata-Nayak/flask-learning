from flask import Flask,make_response,request

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    responce=make_response("<h1>Welcome to HomePage</h1>")
    return responce

@app.route("/set_cookie")
def set_cookie():
    responce=make_response("<h1>Welcome to Set_cookie Page</h1>")
    responce.set_cookie("cookie_key","cookie_value")
    return responce

@app.route("/get_cookie")
def get_cookie():
    cookie=request.cookies.get("cookie_key")
    responce=make_response(f"Your cookie is {cookie}")
    return responce

if __name__=="__main__":
    app.run(debug=True)