from flask import *
from database import *

public=Blueprint('pub',__name__)

@public.route('/',methods=['get','post'])
def home():
    return render_template("home.html")

@public.route("/login",methods=['post','get'])
def login():
    if 'register' in request.form:
        companyname=request.form['cname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        aboutcompany=request.form['abtcompany']
        companylicenseno=request.form['licenseno']
        username=request.form['uname']
        password=request.form['pwd']
        
        a="insert into login values(null,'%s','%s','pending')"%(username,password)
        id=insert(a)
        
        b="insert into company values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,companyname,place,phone,email,aboutcompany,companylicenseno)
        insert(b)
    if 'submit' in request.form:
      uname=request.form['uname'] 
      psw=request.form['pass'] 
      
      x="select * from login where username='%s' and password='%s'"%(uname,psw)
      res=select(x)
      utype=res[0]['usertype']
      session['lid']=res[0]['login_id']
      
      
      
      if utype=='admin':
        return redirect(url_for("admin.adm"))
      elif utype=='user':
        obj="select * from login where login_id='%s'"%(session['lid'])
        select(obj)
        return redirect(url_for("user.usr"))
      elif utype=='company':
        obj="select * from company where login_id='%s'"%(session['lid'])
        we=select(obj)
        session['c_id ']=we[0]['company_id']
        
       
        
        return redirect(url_for("cmpy.companyhome"))
   
    
    return render_template("login.html")

@public.route("/registration",methods=['post','get'])
def reg():
    if 'reg' in request.form:
        firstname=request.form['fname']
        lastname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['uname']
        password=request.form['pwd']
        
        a="insert into login values(null,'%s','%s','user')"%(username,password)
        id=insert(a)
        
        b="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,place,phone,email)
        insert(b)
    
    return render_template("registration.html")

@public.route("/companyregistration",methods=['post','get'])
def companyreg():
    if 'register' in request.form:
        companyname=request.form['cname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        aboutcompany=request.form['abtcompany']
        companylicenseno=request.form['licenseno']
        username=request.form['uname']
        password=request.form['pwd']
        
        a="insert into login values(null,'%s','%s','pending')"%(username,password)
        id=insert(a)
        
        b="insert into company values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,companyname,place,phone,email,aboutcompany,companylicenseno)
        insert(b)
    return render_template("companyregistration.html")


