from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
    
)

class SignupForm(FlaskForm):

    username=StringField(
        "User Name",
        validators=[DataRequired(),Length(2,25)]
    )
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )

    gender=SelectField(
        "Gender",
        choices=["Male","Female","Other"],
        validators=[Optional()]
    )
    dob=DateField(
        "Date of Birth",
        validators=[DataRequired()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30)]
    )
    confirm_pasasword=PasswordField(
        "Confirm Password",
        validators=[DataRequired(),Length(5,30),EqualTo("password")]
    )
    submit=SubmitField(
        "Sign Up",
    )

class SigninForm(FlaskForm):
    
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30)]
    )
    remember_me=BooleanField(
        "Remember Me"
    )
    submit=SubmitField(
        "Sign In",
    )