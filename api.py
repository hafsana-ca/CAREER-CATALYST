from datetime import datetime
import uuid
from flask import *
from database import *
# import fitz

api=Blueprint('api',__name__)


@api.route('/userreg')
def userreg():
    data={}
    
    fn=request.args['fname']
    ln=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['mail']
    un=request.args['uname']
    pwd=request.args['pwd']
    
    
    a="insert into login values(null,'%s','%s','user')"%(un,pwd)
    id=insert(a)
    
    b="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fn,ln,place,phone,email)
    ar=insert(b)
    
    print(ar,"###############")
    
    if ar:
        data['status']='success'
    else:
        data['status']='failed'
        
    return str(data)
    
    
@api.route('/userlogin')
def userlogin():
    data={}
    
    un=request.args['uname']
    pwd=request.args['pwd']
    
    x="select * from login where username='%s' and password='%s'"%(un,pwd)
    res=select(x)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    return str(data)



@api.route('/usercom')
def usercom():
    data={}
    com=request.args['com']
    loginid=request.args['loginid']
    
    qry="insert into complaints values(null,'%s','user','%s','pending',curdate())"%(loginid,com)
    res=insert(qry)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='send'

    return str(data)
           
    
@api.route('/viewcomplaint')
def viewcomplaint():
    data={}
    
    loginid=request.args['loginid']
    qry="select * from complaints where sender_id='%s'"%(loginid)
    res=select(qry)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']='failed'
    data['method']='Reply'

    return str(data)


@api.route('/Viewcompanies')
def Viewcompanies():
    data={}
    

    qry="select * from company"
    res=select(qry)
    print(res,"/////////////////////;llllllllllllllll")
    
    if res:
        data['status']="success"
        data['data']=res
        
    else:
        data['status']='failed'
    data['method']='Reply'

    return str(data)
    
    
@api.route('/View_jobs')
def View_jobs():
    data={}
    
    companyid=request.args['id']
    
    print(companyid,"/////////////////////")

    qry="select * from job_vaccancy where company_id='%s'"%(companyid)
    res=select(qry)
    print(res)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="job"

    return str(data)



@api.route('/Viewinternship')
def Viewinternship():
    data={}
    
    companyid=request.args['id']

    qry="select * from internship where company_id='%s'"%(companyid)
    res=select(qry)
    print(res)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="internship"

    return str(data)


@api.route('/Viewcompanypost')
def Viewcompanypost():
    data={}
    
    companyid=request.args['id']

    qry="select * from company_post left join blog using(company_post_id) where company_id='%s'"%(companyid)
    res=select(qry)
    print(res)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="post"

    return str(data)

@api.route('/sendapplication')
def sendapplication():
    data={}
    
    vacid=request.args['id']
    userid=request.args['log_id']
    qry="select user_id from user where login_id='%s'"%(userid)
    uid=select(qry)
    aa=uid[0]['user_id']
    
    qry1="insert into job_application values(null,'%s','%s',curdate(),'pending')"%(vacid,aa)
    res=insert(qry1)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="application"

    return str(data)


@api.route('/applyinternship')
def applyinternship():
    data={}
    
    internid=request.args['id']
    userid=request.args['log_id']
    qry="select user_id from user where login_id='%s'"%(userid)
    uid=select(qry)
    aa=uid[0]['user_id']
    
    qry1="insert into internship_application values(null,'%s','%s',curdate(),'pending')"%(internid,aa)
    res=insert(qry1)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="applyforinternship"

    return str(data)
    

@api.route('/addcomment')
def addcomment():
    data={}
    
    postid=request.args['id']
    userid=request.args['log_id']
    qry="select user_id from user where login_id='%s'"%(userid)
    uid=select(qry)
    aa=uid[0]['user_id']
    
    qry1="insert into company_post values(null,'%s','%s','%s','%s',curdate())"%(postid,aa)
    res=insert(qry1)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="addcomment"

    return str(data)


@api.route('/comments')
def comments():
    data={}
    
    com=request.args['com']
    loginid=request.args['loginid']
    post_id=request.args['post_id']
    
    kk="insert into comments values(null,'%s','%s','%s',curdate())"%(post_id,loginid,com)
    res=insert(kk)
    
    if res:
        
        data['status']="success"
        
    else:
        data['status']="failed"
        
    return str(data)

    
@api.route('/Addcompanyreview')
def Addcompanyreview():
    data={}
    
    comid=request.args['cid']
    userid=request.args['log_id']
    review=request.args['review']
    rating=request.args['rating']

    qry="select user_id from user where login_id='%s'"%(userid)
    uid=select(qry)
    print(uid)
    aa=uid[0]['user_id']
    
    qry1="insert into company_review values(null,'%s','%s','%s','%s',curdate())"%(comid,aa,review,rating)
    res=insert(qry1)
    
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"

    return str(data)
    
    
    
    

@api.route('/upload_pdf',methods=['get','post'])
def upload_pdf():
    data = {}
    
    print("///////////////////////")


    import random
    import string
    import fitz
    text = ''

    def generate_random_alphanumeric(length):
        if length < 1:
            raise ValueError("Length must be at least 1")
        
        random_string = random.choice(string.ascii_letters)  # First character is an alphabet
        random_string += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - 1))
        
        return random_string

    # Example: Generate a random alphanumeric string of length 8
    random_string = generate_random_alphanumeric(8)
    print(random_string)


    log_id=request.form['login_id']
    pdf=request.files['pdf']
    path1='static/resume/'+str(uuid.uuid4())+pdf.filename
    print(path1)
    # path1='/Users/mcbk/Riss/2023-2024 Project Modules/Kerala Varma Clg/KnowItRight/Know_it_right_android/app/src/main/assets/'+random_string+pdf.filename

    pdf.save(path1)

    print("pdf : ",pdf)
    # Open the PDF file in read-binary mode
    with open(path1, 'rb') as pdf_file:
        # Create a PyPDF2 PdfReader object
        pdf_reader = fitz.open(pdf_file)
        print("pdf_reader : ",pdf_reader)

        # Get the number of pages in the PDF file
        num_pages = pdf_reader.page_count
        print("num_pages : ",num_pages)

        # Iterate through all the pages and extract the text
        
        for page_num in range(num_pages):
            page = pdf_reader.load_page(page_num)
            page_text = page.get_text()
            print("page_text : ",page_text)
            text += page_text

        print(text)

    # Sample resume text
    resume_text = text.replace("'", "''")
    print("resume_text : ",resume_text)

    qq="SELECT * FROM `resume` WHERE user_id =(SELECT user_id FROM user WHERE login_id='%s')"%(log_id)
    res=select(qq)
    if res:
        q1="UPDATE `resume` SET `file`='%s',`resume_skills`='%s' WHERE resume_id='%s'"%(path1,resume_text,res[0]['resume_id'])
        result=update(q1)
    else:

        q="""INSERT INTO `resume`(`resume_id`, `user_id`, `file`, `resume_skills`)
        VALUES (null,(select user_id from user where login_id='%s'),'%s','%s')"""%(log_id,path1,resume_text)
        result=insert(q)
        

    # result =1
    if result:
        data['status'] = "success"
        data['data'] = result
    else:
        data['status'] = 'failed'
    data['method'] = "upload_pdf"
    print(data)
    return str(data)

@api.route('/view_pdf',methods=['get','post'])
def view_pdf():
    data = {}

    log_id=request.args['login_id']


    qq="SELECT * FROM `resume` WHERE user_id =(SELECT user_id FROM user WHERE login_id='%s')"%(log_id)
    result=select(qq)
    if result:
        print(result,"00000000000000")
        
        
        data['status'] = "success"
        data['data']=result
        # print(data['data'])
        # file_path = result[0]['file']
        # print(result[0]['file'])

        # file_name = os.path.basename(file_path)
        # data['data'] =file_name
        # print("file_name : "+file_name)
    else:
        data['status'] = 'failed'
    data['method'] = "view_pdf"
    return str(data)


@api.route('/User_view_my_post')
def User_view_my_post():
    data = {}
    login_id=request.args['login_id']

    # q = """SELECT *,concat(first_name,' ',last_name) as user_name FROM `user_post` inner join user using(user_id) where login_id='%s' order by date DESC""" % (login_id)
    q = """SELECT *,concat(first_name,' ',last_name) as user_name FROM `user_post` inner join user using(user_id)  order by date DESC""" 
    result = select(q)
    if result:
        data['status'] = "success"
        data['data']=result
    else:
        data['status'] = 'failed'
    data['method']="User_post"
    return str(data)



@api.route('/User_add_post')
def User_add_post():
	data = {}
	login_id = request.args['log_id']
	c_title = request.args['c_title']
	complaint= request.args['complaint']
	q = """INSERT INTO `user_post`
	VALUES (null,(select user_id from user where login_id='%s'),'%s','%s','text',curdate())""" % (login_id,c_title,complaint)
	result = insert(q)
	if result:
		data['status'] = "success"
	else:
		data['status'] = 'failed'
	data['method']="User_add_post"
	return str(data)



@api.route('/Multi_file_upload',methods=['get','post'])
def Multi_file_upload():
	data = {}

	login_id=request.form['log_id']
	print("login_id : ",login_id)
	file=request.files['file']
	path="static/"+str(uuid.uuid4())+file.filename
	file.save(path)
	ff=file.filename
	result_list = ff.split('.')
	print(result_list[1])
	
	print("FILES : ",file)
	c_title = request.form['title']
	q = """INSERT INTO `user_post`
	VALUES (null,(select user_id from user where login_id='%s'),'%s','%s','%s',curdate())""" % (login_id,c_title,path,result_list[1])
	result = insert(q)

	
	data['status'] = "success"
		
	data['method']="Multi_file_upload"
	return str(data)


@api.route('/User_view_comments')
def User_view_comments():
	data = {}

	user_post_ids=request.args['user_post_ids']

	q = """SELECT * FROM `comments` c inner join login l on c.user_id=l.login_id WHERE c.`user_post_id`='%s' order by c.comment_id desc""" % (user_post_ids)
	result = select(q)
	if result:
		data['status'] = "success"
		data['data']=result
	else:
		data['status'] = 'failed'
	data['method']="User_view_comments"
	return str(data)


@api.route('/User_add_comments')
def User_add_comments():
	data = {}
	login_id = request.args['log_id']
	comments= request.args['comments']
	user_post_ids=request.args['user_post_ids']

	q = """INSERT INTO comments
	VALUES (null,'%s','%s','%s',curdate())""" % (user_post_ids,login_id,comments)
	result = insert(q)
	if result:
		data['status'] = "success"
	else:
		data['status'] = 'failed'
	data['method']="User_add_comments"
	return str(data)

import re

@api.route('/User_view_job_vacancy')
def User_view_job_vacancy():
    data = {}
    login_id = request.args['login_id']
    qq = "SELECT * FROM `resume` WHERE `user_id`=(select `user_id` from user where login_id='%s')" % (login_id)
    ress = select(qq)

    q = "SELECT * FROM `job_vaccancy` INNER JOIN job_category USING(job_category_id) INNER JOIN company USING(company_id)"
    result = select(q)

    # Initialize an empty list to store the individual skills
    all_skills = []

    # Iterate through each dictionary in the 'result' list
    for c_skill in result:
        # Append the 'skills' value to the list
        all_skills.extend(skill.strip() for skill in c_skill['skills'].split(','))

    # Sample resume text
    resume_text = ress[0]['resume_skills']

    # Preprocessing
    resume_text = re.sub(r'[^\w\s]', '', resume_text)  # Remove punctuation
    resume_text = resume_text.lower()  # Convert to lowercase
    
    print(all_skills,resume_text)

    # Matching skills

    # matches = [skill for skill in all_skills if re.search(skill.lower(), resume_text)]
    # Assuming `all_skills` is a list of skills and `resume_text` is the resume text
    matches = [skill for skill in all_skills if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text, flags=re.IGNORECASE)]
    # Scoring matches
    score = len(matches)
    print("score : ", score)
    matched_job_vacancies=""

    # Filtering resumes
    threshold = 2  # Set threshold for matches
    if score >= threshold:
        # Filter job vacancies based on matches
        matched_job_vacancies = [job for job in result if any(re.search(skill.lower(), job['skills'].lower()) for skill in matches)]
        print('Matched Job Vacancies:', matched_job_vacancies)
    else:
        print('Resume does not match')

    if matched_job_vacancies:
        data['status'] = "success"
        data['data'] = matched_job_vacancies
    else:
        data['status'] = 'failed'
    data['method'] = "User_view_job_vacancy"
    return str(data)




@api.route('/User_view_more_about_job')
def User_view_more_about_job():
	data = {}
	job_vacancy_ids = request.args['job_vacancy_ids']
	q = "SELECT * FROM `job_vaccancy` INNER JOIN job_category USING(job_category_id) INNER JOIN company USING(company_id) where job_vaccancy_id='%s'"%(job_vacancy_ids)
	result = select(q)

	if result:
		data['status'] = "success"
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = "User_view_more_about_job"
	return str(data)



# Function to calculate date difference
def calculate_date_difference(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    difference = end_date - start_date
    return difference.days


@api.route('/User_apply_job')
def User_apply_job():
	data = {}
	job_vacancy_ids = request.args['job_vacancy_ids']
	login_id=request.args['login_id']

	qq="SELECT * FROM `job_application` WHERE `user_id`=(SELECT `user_id` from user WHERE login_id='%s') and `job_vaccancy_id`='%s' ORDER BY `date` desc"%(login_id,job_vacancy_ids)
	res=select(qq)
	if res:
		dd=res[0]['date']

		current_date = datetime.now().strftime("%Y-%m-%d")
		print(current_date)

		# Calculate date difference
		date_difference = calculate_date_difference(dd, current_date)
		print("date_difference : ",date_difference)
		if date_difference > 60:
			q="INSERT INTO `job_application` VALUES (null,'%s',(SELECT `user_id` from user WHERE login_id='%s'),curdate(),'pending')"%(job_vacancy_ids,login_id)
			insert(q)
			data['status']="success"
		else:
			data['status']='You Have Already Applied'
	else:
		q="INSERT INTO `job_application` VALUES (null,'%s',(SELECT `user_id` from user WHERE login_id='%s'),curdate(),'pending')"%(job_vacancy_ids,login_id)
		insert(q)
		data['status']="success"

	data['method'] = "User_apply_job"
	return str(data)



# @api.route('/Multi_file_upload')
# def Multi_file_upload():
#     data={}
    
#     file=request.files['file']
#     userid=request.args['log_id']
#     qry="select user_id from user where login_id='%s'"%(userid)
#     uid=select(qry)
#     aa=uid[0]['user_id']
    
   
    
#     if res:
#         data['status']="success"
#         data['data']=res
#     else:
#         data['status']="failed"

#     return str(data)

@api.route('/Multi_file_upload_resume',methods=['get','post'])
def Multi_file_upload_resume():
	data = {}

	login_id=request.form['log_id']
	print("login_id : ",login_id)
	file=request.files['file']
	path="static/"+str(uuid.uuid4())+file.filename
	file.save(path)
	ff=file.filename
	result_list = ff.split('.')
	print(result_list[1])
	
	print("FILES : ",file)
	# c_title = request.form['title']
	# q = """INSERT INTO `resume`
	# VALUES (null,(select user_id from user where login_id='%s'),'%s','%s',curdate())""" % (login_id,,path,result_list[1])
	# result = insert(q)

	
	data['status'] = "success"
		
	data['method']="Multi_file_upload"
	return str(data)

@api.route("/UserProfile")
def UserProfile():
    data={}
    id = request.args['id']
    q="select * from user where login_id='%s'"%(id)
    result = select(q)

    if result:
        data['status'] = "success"
        data['data'] = result
    else:
        data['status'] = 'failed'
    data['method'] = "view"
    return str(data)

@api.route("/ViewMyApplications")
def ViewMyApplications():
    data={}
    id = request.args['id']
    q="select * from job_application inner join job_vaccancy using(job_vaccancy_id) where user_id=(select user_id from user where login_id='%s')"%(id)
    result = select(q)

    if result:
        data['status'] = "success"
        data['data'] = result
    else:
        data['status'] = 'failed'
    data['method'] = "view"
    return str(data)





@api.route("/viewpro")
def viewpro():
    data={}
    id = request.args['id']
    q="select * from user where login_id='%s'"%(id)
    result = select(q)

    if result:
        data['status'] = "success"
        data['data'] = result
    else:
        data['status'] = 'failed'
    data['method'] = "view"
    return str(data)



@api.route('/uppro')
def uppro():
    data={}
    id=request.args['id']
    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    email=request.args['email']
    phone=request.args['phone']
    
    
    qry="update user set first_name='%s',last_name='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,place,phone,email,id)
    res=update(qry)
    if res:
        data['status']="success"
        data['method']="up"
    return str(data)




