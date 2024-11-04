from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route("/adm")
def adm():
    return render_template("admin.html")

@admin.route("/viewcompany",methods=['get','post'])
def viewcompany():
   data={}
   d="select * from company inner join login using(login_id)"
   result=select(d)
    
   data['view']=result
   
   if 'action' in request.args:
       action=request.args['action']
       id=request.args['id']
   else:
       action=None
       
   if action=='approve':
        qry="update login set usertype='company' where login_id='%s'"%(id)
        update(qry)
        return '''<script>alert("accepted");window.location="/viewcompany"</script>'''
    
   if action=='reject':
        qry1="delete from login where login_id='%s'"%(id)
        delete(qry1)
        return '''<script>alert("rejected");window.location="/viewcompany"</script>'''

   return render_template('viewcompany.html',data=data) 
   
@admin.route("/viewuser",methods=['get','post'])
def viewuser():
    data={}
    du="select * from user"
    result=select(du)
    
    data['view']=result
   
       
    return render_template('viewuser.html',data=data)    

@admin.route("/viewcomplaints",methods=['get','post'])
def viewcomplaints():
    data={}
    dc="select * from complaints"
    result=select(dc)
    
    data['view']=result
    
    return render_template('viewcomplaints.html',data=data)  

  
@admin.route("/viewjobvaccancies",methods=['get','post'])
def viewjobvaccancies():
    data={}
    dv="select * from job_vaccancy"
    result=select(dv)
    
    data['view']=result
    
    return render_template("viewjobvaccancies.html",data=data)


@admin.route("/addjobcategory",methods=['get','post'])

def addjobcategory():
    
    data={}
    dj="select * from job_category"
    result=select(dj)
    
    data['view']=result

    if "submit" in request.form:
        jobcategory=request.form['jbname']
        b="insert into job_category values(null,'%s')"%(jobcategory)
        insert(b)
        
        return '''<script>alert("added");window.location="addjobcategory"</script>'''
    
    return render_template("addjobcategory.html",data=data)       
    
    
    
@admin.route("/sendreply",methods=['get','post'])
def sendreply():
    id=request.args['id']
    if "submit" in request.form:
        rly=request.form['reply']
        
        qry="update complaints set reply='%s' where complaint_id='%s'"%(rly,id)
        update(qry)
        
        # return '''<script>alert("success");window.location='/viewcomplaints'</script>'''
        
    return render_template("sendreply.html")

@admin.route("/user_complaints",methods=['get','post'])
def user_complaints():
   data={}
   d="select * from complaints inner join user on user.login_id=complaints.sender_id where sender_type='user'"
   result=select(d)
    
   data['view']=result
   return render_template("user_complaints.html",data=data)    
   
@admin.route("/company_complaints",methods=['get','post'])
def company_complaints():
   data={}
   d="select * from complaints inner join company on company.company_id=complaints.sender_id where sender_type='company'"
   result=select(d)
    
   data['view']=result
   return render_template("company_complaints.html",data=data)   
    


@admin.route("/company_posts",methods=['get','post'])
def company_posts():
    data={}
    d="select * from company_post inner join company using(company_id)"
    result=select(d)
    data['view']=result
    
    if 'action' in request.args:
       action=request.args['action']
       id=request.args['id']
    else:
       action=None
    
    if action=='delete':
        qry1="delete from company_post where company_post_id ='%s'"%(id)
        delete(qry1)
        return '''<script>alert("deleted");window.location="/company_posts"</script>'''
    
    return render_template('company_posts.html',data=data) 
  
