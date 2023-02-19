# Form file collects data for dockerization of user's application
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

 username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

 email = StringField('Email', validators=[DataRequired(), Email()])

 password = PasswordField('Password', validators=[DataRequired()])

 confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

 submit = SubmitField('Sign in')



class LoginForm(RegistrationForm):

 email = StringField('Email', validators=[DataRequired(), Email()])

 password = PasswordField('Password', validators=[DataRequired()])
 
 remember = BooleanField('Remember Me')

 submit = SubmitField('Login')


class UploadFileForm (FlaskForm):

 name = StringField('Filename', validators=[DataRequired(), Length(min=2, max=20)])

 file = FileField('file', validators=[InputRequired()])

 submit = SubmitField('Dockerize It!')