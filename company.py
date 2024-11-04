import uuid
from flask import *
from database import *

from email.mime.text import MIMEText
import smtplib
import string

from flask_mail import Mail

company=Blueprint('cmpy',__name__)


@company.route("/companyhome")
def companyhome():
    return render_template("companyhome.html")

@company.route("/viewjobcategory",methods=['get','post'])
def viewjobcategory():
    data={}
    d="select * from job_category"
    result=select(d)
    data['view']=result
    return render_template('viewjobcategory.html',data=data) 


@company.route("/addjobsandskills",methods=['get','post'])
def addjobsandskills():  
    data={}
    id=request.args['id']    
    dj="select * from job_vaccancy inner join company using(company_id) where job_category_id='%s'  and company_id='%s'"%(id, session['c_id '])
    result=select(dj)
    
    data['view']=result

    if "submit" in request.form:
        jobtitle=request.form['title']
        jobtitle=jobtitle.replace("'","''")
        jobdescription=request.form['des']
        jobdescription=jobdescription.replace("'","''")
        skills=request.form['skills']
        skills=skills.replace("'","''")

        

        b="insert into job_vaccancy values(null,'%s','%s','%s','%s','%s')"%(id,session['c_id '],jobtitle,jobdescription,skills)
        insert(b)
        
        return '''<script>alert("added");window.location="/viewjobcategory"</script>'''
      
    
    return render_template("addjobsandskills.html",data=data) 
      
    
@company.route("/viewuserpost",methods=['get','post'])
def viewuserpost():
   data={}
   d="select * from user_post inner join user using (user_id)"
   result=select(d)
    
   data['view']=result
   return render_template('viewuserpost.html',data=data)   

@company.route("/addcomments",methods=['get','post'])
def addcomments():
    id=request.args['id']
    
    data={}
    dj="select * from comments c inner join login l on c.user_id=l.login_id where  user_post_id='%s'"%(id)
    result=select(dj)
    
    data['view']=result
    
    if "submit" in request.form:
        comments=request.form['comments']

        b="insert into comments values(null,'%s','%s','%s',curdate())"%(id,session['c_id '],comments)
        insert(b)
        
        return '''<script>alert("added");window.location="viewuserpost"</script>''' 
    return render_template('addcomments.html',data=data)   
 


@company.route("/viewjobapplicants",methods=['get','post'])
def viewjobapplicants():
   data={}
   d="select *,user.phone as Phone,user.email as Email,user.place as Place from job_application inner join user using(user_id) inner join job_vaccancy using(job_vaccancy_id) inner join company using(company_id) where company.company_id='%s'"%(session['c_id '])
   result=select(d)
    
   data['view']=result
   if 'action' in request.args:
       action=request.args['action']
       id=request.args['id']
   else:
       action=None
       
   if action=='accept':
        qry="update job_application set status='accept' where job_application_id='%s'"%(id)
        res=update(qry)
        r="select * from user inner join job_application using(user_id) inner join job_vaccancy using(job_vaccancy_id) inner join company using(company_id) where user_id=(select user_id from job_application where job_application_id='%s')"%(id)
        e=select(r)
        a=e[0]['user_id']
        
        p="select * from user where user_id='%s'"%(a)
        s=select(p)
        print(p,"ppppppppppppppppppppppp")

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('lbetter24x7@gmail.com','jjwrgcahofexprck')
            print("##############",s[0]['email'])
            msg = MIMEText("Dear {}, We are thrilled to inform you that your application for the {} at {} has been accepted! We were impressed by your qualifications and experience, and we believe that you will be a valuable addition to our team. Please let us know if you have any questions or need any further information. We look forward to welcoming you aboard and wish you great success in your new role at {}. Best regards".format(e[0]['first_name'],e[0]['job_title'],e[0]['company_name'],e[0]['company_name']))
            msg['Subject'] = 'Your Job Application has been Accepted!'
            msg['To'] = s[0]['email']
            msg['From'] = 'lbetter24x7@gmail.com'

            gmail.send_message(msg)
            return '''<script>alert("accepted");window.location="/viewjobapplicants"</script>'''
            # return redirect(url_for('company.viewjobapplicants'))
        except Exception as ex:
            print("Couldn't send email", str(ex))
            return '''<script>alert("error");window.location="/viewjobapplicants"</script>'''
        
   if action=='reject':
        qry1="delete from job_application where job_application_id='%s'"%(id)
        delete(qry1)
        return '''<script>alert("rejected");window.location="/viewjobapplicants"</script>'''
    
    
    
   return render_template('viewjobapplicants.html',data=data)
   

@company.route('/companyviewpdf')
def companyviewpdf():
    data={}
    id=request.args['id']
    r="select * from resume where user_id='%s'"%(id)
    res=select(r)
    data['view']=res
    
    
    return render_template('companyviewpdf.html',data=data)


@company.route("/company_sendcomplaints",methods=['get','post'])
def company_sendcomplaints():
    data={}
    dj="select * from complaints where sender_id='%s'"%(session['c_id '])
    result=select(dj)
    
    data['view']=result
    
    
    if'submit' in request.form:
        comp=request.form['sendcomplaint']
        
        qry="insert into complaints values(null,'%s','company','%s','pending',curdate())"%(session['lid'],comp)
        insert(qry)
        return '''<script>alert("added");window.location="company_sendcomplaints"</script>'''  
    return render_template("company_sendcomplaints.html",data=data)


@company.route("/addinternship",methods=['get','post'])

def addinternship():
    
    data={}
    dj="select * from internship where company_id='%s'"%(session['c_id '])
    result=select(dj)
    
    data['view']=result

    if "submit" in request.form:
        title=request.form['title']
        duration=request.form['duration']
        fees=request.form['fees']
        syl=request.form['syllabus']
        b="insert into internship values(null,'%s','%s','%s','%s','%s')"%(session['c_id '],title,duration,fees,syl)
        insert(b)
        return '''<script>alert("added");window.location="addinternship"</script>'''  
    
    return render_template("addinternship.html",data=data)



@company.route("/companypost",methods=['get','post'])
def companypost():
    
    data={}
    
    dj="select * from company_post where company_id='%s'"%(session['c_id '])
    result=select(dj)
    data['view']=result
    
    
    
    if "submit" in request.form:
        title=request.form['title']
        title=title.replace("'","''")
        link=request.form['link']
        post=request.files['post']
        postType=request.form['posttype']
        
        
        path='static/' + str(uuid.uuid4()) + post.filename
        post.save(path)
        b="insert into company_post values(null,'%s','%s','%s','%s',curdate(),'%s')"%(session['c_id '],title,path,postType,link)
        insert(b)
        return '''<script>alert("added");window.location="companypost"</script>'''  
    
    return render_template("companypost.html",data=data)

            
         
# @company.route("/viewcompanyblog",methods=['get','post'])
# def viewcompanyblog():
    
#     data={}
#     id=request.args['id']
    
#     dj="select * from company_post where company_post_id='%s'"%(id)
#     result=select(dj)
#     data['view']=result
    
#     if "submit" in request.form:
#         des=request.form['des']
        
#         b="insert into blog values(null,'%s','%s')"%(id,des)
#         insert(b)
    
#     return render_template("viewblog.html",data=data)


       
# @company.route("/viewcompanyblog", methods=['GET', 'POST'])
# def viewcompanyblog():
#     data = {}
#     id = request.args.get('id')
    
#     if id:
#         dj = "SELECT * FROM company_post WHERE company_post_id='%s'" % id
#         result = select(dj)
#         data['view'] = result
    
#     if request.method == 'POST':
#         des = request.form.get('des')
#         if des:
#             b = "INSERT INTO blog VALUES (null, '%s', '%s')" % (id, des)
#             insert(b)
#             return '''<script>alert("added");window.location="companypost"</script>'''  

#     return render_template("viewblog.html", data=data)

@company.route("/viewcompanyblog",methods=['get','post'])
def viewcompanyblog():
    
    data={}
    id=request.args['id']

    dj="select * from company_post where company_post_id='%s'"%(id)
    result=select(dj)
    
    data['view']=result
    
    if "submit" in request.form:
        des=request.form['des']
        des=des.replace("'","''")
       

        b="insert into blog values(null,'%s','%s')" % (id,des)
        insert(b)
        
        return '''<script>alert("added");window.location="/companypost"</script>''' 
    return render_template('viewblog.html',data=data)   

    


@company.route("/internship_applicants",methods=['get','post'])
def internship_applicants():
   data={}
   r="select user.*,internship_application.*,internship.*,company.company_id from user inner join internship_application using(user_id) inner join internship using(internship_id) inner join company using(company_id) where company_id='%s'"%(session['c_id '])
   result=select(r)
    
   data['view']=result
   if 'action' in request.args:
       action=request.args['action']
       id=request.args['id']
   else:
       action=None
       
   if action=='accept':
        qry="update internship_application set status='accept' where internship_application_id='%s'"%(id)
        res=update(qry)
        r="select * from user inner join internship_application using(user_id) inner join internship using(internship_id) inner join company using(company_id) where user_id=(select user_id from internship_application where internship_application_id='%s')"%(id)
        e=select(r)
        a=e[0]['user_id']
        
        p="select * from user where user_id='%s'"%(a)
        s=select(p)
 
   if action=='reject':
        qry1="delete from internship_application where internship_application_id='%s'"%(id)
        delete(qry1)
        return '''<script>alert("rejected");window.location="/internship_applicants"</script>'''
   return render_template('internship_applicants.html',data=data)

@company.route("/companyreview",methods=['get','post'])
def companyreview():
   data={}
   d="select * from company_review inner join user using (user_id) where company_id='%s'"%(session['c_id '])
   result=select(d)
    
   data['view']=result
   return render_template('companyreview.html',data=data)   




   