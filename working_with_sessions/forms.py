from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    
)

class LoginForm(FlaskForm):
    
    username=StringField(
        "User Name",
        validators=[DataRequired()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30)]
    )
    submit=SubmitField(
        "Sign In",
    )