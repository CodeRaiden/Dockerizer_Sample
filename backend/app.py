from flask import Flask, render_template, url_for, flash, redirect
from forms import UploadFileForm, RegistrationForm, LoginForm
# To upload files securely
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Secrete key which will protect against modifying cookies and cross side request
app.config['SECRET_KEY'] = 'supersecretekey'
# configuration for files to be uploaded to static/files folder
app.config['UPLOAD_FOLDER'] = 'static/files'

# # endpoint for home page
# @app.route("/")
# @app.route("/home")
# def home():
#  return "Welcome to Dockerizer home page!"

# # end point for user registration page
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#  form = RegistrationForm()
#  if form.validation_on_submit():
#   return {'message': f'user {form.username.data} is successfully logged in'}
#  return {'error': 'User sign in failed'}

# # endpoint for user login page
# @app.route('/login')
# def login():
#  form = LoginForm()
#  if form.validation_on_submit():
#   return {'message': f'user {form.username.data} is successfully logged in'}
#  return {'error': 'User log in failed'}

# # endpoint for file upload page
# @app.route("/upload", methods=['GET', 'POST'])
# def upload():
#  form = UploadFileForm()
#  if form.validate_on_submit(): # storing submitted files to static/files dir when form is valid
#   file = form.file.data # first grab the file
#   file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # then save the file
#   return {'message': f'Your file "{form.name.data}" has been successfully uploaded!'}
#  return {'error': 'Form upload unsuccessful'}

# # endpoint for about page
# @app.route("/about")
# def about():
#  return 'Dockerizer About page!'


# endpoint for home page
@app.route("/")
@app.route("/home")
def home():
 return render_template('home.html')

# end point for user registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
 form = RegistrationForm()
 if form.validate_on_submit():
  flash(f'Account created for {form.username.data}!', 'success') # displays a flash message
  return redirect(url_for('home'))
 return render_template('register.html', title='Register', form=form)

# endpoint for user login page
@app.route('/login')
def login():
 form = LoginForm()
 return render_template('login.html', title='Login', form=form)

# endpoint for file upload page
@app.route("/upload", methods=['GET', 'POST'])
def upload():
 form = UploadFileForm()
 if form.validate_on_submit(): # storing submitted files to static/files dir when form is valid
  file = form.file.data # first grab the file
  file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
  flash(f'Your file "{form.name.data}" has been successfully uploaded!', 'success')
  return redirect(url_for('home'))
 return render_template('upload.html', title='Upload', form=form)

# endpoint for about page
@app.route("/about")
def about():
 return render_template('about.html')


if __name__ == "__main__":
 app.run(debug=True)
