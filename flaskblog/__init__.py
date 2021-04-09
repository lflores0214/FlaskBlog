import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from decouple import config

GMAIL_USER = config('GMAIL_USER')
GMAIL_PASS = config('GMAIL_PASS')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4f49b0f7a880f50cdda741e13a3e203'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = GMAIL_USER
app.config['MAIL_PASSWORD'] = GMAIL_PASS
mail = Mail(app)




from flaskblog import routes