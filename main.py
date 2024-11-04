from flask import *

from admin import admin
from public import public
from user import user
from company import company
from api import api

from flask_mail import Mail

from email.mime.text import MIMEText
import smtplib




app=Flask(__name__,template_folder="template")


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'lbetter24x7@gmail.com'
# app.config['MAIL_PASSWORD'] = 'jjwrgcahofexprck'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


   
app.secret_key='efsef'

app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(user)
app.register_blueprint(company)
app.register_blueprint(api)

app.run(debug=True,port=5018,host="0.0.0.0")