from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    MAIL_USERNAME = config('GMAIL_USER')
    MAIL_PASSWORD = config('GMAIL_PASS')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
