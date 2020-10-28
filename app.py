from flask import Flask, render_template, redirect
from models import db, connect_db, User
from secrets import KEY
from forms import Register
app = Flask(__name__)

app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///FlaskFeedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

@app.route('/')
def redirect_register():
    return redirect('/register')

@app.route('/register')
def register():
    return render_template('register.html')