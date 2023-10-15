from flask import *
from database import *

from ev_review import *
from ev_ch_3 import estimate_charging_time

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				flash("Login successful")
				return redirect(url_for('admin.admin_home'))
			elif res[0]['usertype']=="bunk":
				qry="select * from charging_center where login_id='%s'"%(session['lid'])
				res=select(qry)
				if res:
					session['bunk_id']=res[0]['center_id']
					flash("Login successful")
					return redirect(url_for('bunk.bunk_home'))
				else:
					flash("Invalid")
			elif res[0]['usertype']=="service_center":
				qry="select * from service_center where login_id='%s'"%(session['lid'])
				res=select(qry)
				session['center_id']=res[0]['center_id']
				flash("Login successful")
				return redirect(url_for('center.center_home'))
	return render_template('login.html')	


@public.route('/recharge_bunk_registeration',methods=['get','post'])
def recharge_bunk_registeration():
	if 'submit' in request.form:
		firstname=request.form['firstname']
		place=request.form['place']
		latitude=request.form['latitude']
		phone=request.form['phone']
		email=request.form['email']
		longitude=request.form['longitude']
		ppu=request.form['ppu']
		power = request.form['power']
		username=request.form['username']
		password=request.form['password']
		qry="insert into login values(null,'%s','%s','pending')"%(username,password)
		lid=insert(qry)
		q="INSERT INTO `charging_center` VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,firstname,phone,email,latitude,longitude,place,ppu,power)
		q=insert(q)
		if q:
			flash("Registered successfully")
			return redirect(url_for('public.login'))			
	return render_template('bunk_register.html')


# @public.route('/service_center_registeration',methods=['get','post'])
# def service_center_registeration():
# 	if 'submit' in request.form:
# 		firstname=request.form['firstname']
# 		lastname=request.form['lastname']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		email=request.form['email']
# 		latitude=request.form['latitude']
# 		longitude=request.form['longitude']
# 		username=request.form['username']
# 		password=request.form['password']
# 		qry="insert into login values(null,'%s','%s','service_center')"%(username,password)
# 		lid=insert(qry)
# 		q="INSERT INTO `service_center` VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,firstname,lastname,place,phone,email,latitude,longitude)
# 		q=insert(q)
# 		if q:
# 			flash("Registered successfully")
# 			return redirect(url_for('public.login'))			
# 	return render_template('center_registeration.html')


# @public.route('/')
# def User_view_bunk_review():
# 	data={}
# 	q="select * from feedback"
# 	res=select(q)
# 	review_dict={}
# 	for i in res:
# 		bunk_id=i['center_id']
# 		if bunk_id not in review_dict:
# 			qry="select distinct feedback from feedback where center_id='%s'"%(bunk_id)
# 			r1=select(qry)
# 			print(r1)
# 			for row in r1:
# 				review_dict[bunk_id]=r1
# 				print(review_dict[bunk_id])
# 				feedback=review_pred(row['feedback'])
# 				print(feedback)
# 	return render_template("reviewminingtest.html",data=data)

@public.route('/User_view_bunk_review',methods=['get','post'])
def viewrating():
    data={}
    clevel=40
    dlevel=80
    ctym=estimate_charging_time(clevel,dlevel)
    print(ctym)
    return render_template('reviewminingtest.html')



