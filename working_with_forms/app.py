from flask import Flask,render_template,redirect,url_for,flash
from forms import SigninForm,SignupForm
app=Flask(__name__)

app.config["SECRET_KEY"]="this_is_a_secret_key"
@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html",title="Home") 

@app.route("/signup",methods=["GET","POST"])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully registered {form.username.data}")
        return redirect(url_for("home"))
    return render_template("signup.html",title="Signup",form=form)

@app.route("/signin",methods=["GET","POST"])
def signin():
    form=SigninForm()
    if form.validate_on_submit():
        flash(f"Successfully Signed In ")
        return redirect(url_for("home"))
    return render_template("signin.html",title="Signin",form=form)


if __name__=="__main__":
    app.run(debug=True)