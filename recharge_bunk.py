from flask import *
from database import *
bunk=Blueprint('bunk',__name__)
import random


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

@bunk.route('/bunk_home')
def bunk_home():
    return render_template('bunk_home.html')


@bunk.route('/bunk_add_faculty',methods=['get','post'])
def bunk_add_faculty():
	data={}
	qry="select * from faculty inner join charging_center using(center_id) where center_id='%s'"%(session['bunk_id'])
	data['comp']=select(qry)
	if 'submit' in request.form:
		name=request.form['name']
		desc=request.form['desc']
		q="INSERT INTO `faculty` VALUES(NULL,'%s','%s','%s')"%(session['bunk_id'],name,desc)
		insert(q)
		return redirect(url_for('bunk.bunk_add_faculty'))
	return render_template('bunk_add_faculty.html',data=data)	

@bunk.route('/bunk_update_faculty',methods=['get','post'])
def bunk_update_faculty():
	data={}
	session['type_id']=type_id=request.args['type_id']
	qry="select * from faculty inner join charging_center using(center_id) where faculty_id='%s'"%(type_id)
	data['up']=select(qry)
	if 'update' in request.form:
		name=request.form['name']
		desc=request.form['desc']
		q="update  `faculty` set fac_name='%s',description='%s' where faculty_id='%s'"%(name,desc,session['type_id'])
		a=update(q)
		if a:
			flash("Updated Successfully")
			return redirect(url_for('bunk.bunk_add_faculty',type_id=type_id))
	return render_template('bunk_update_faculty.html',data=data)	



@bunk.route('/bunk_update_power',methods=['get','post'])
def bunk_update_power():
    data={}
    q="select * from charging_center where center_id='%s'"%(session['bunk_id'])
    data['res']=select(q)
    print(data['res'])
    if 'submit' in request.form:
        power=request.form['power']
        qr="update charging_center set power='%s' where center_id='%s'"%(power,session['bunk_id'])
        update(qr)
        return redirect(url_for('bunk.bunk_update_power'))
    return render_template("bunk_update_power.html",data=data)


@bunk.route('/bunk_delete_faculty',methods=['get','post'])
def bunk_delete_faculty():
	data={}
	type_id=request.args['type_id']
	q="delete from `faculty` where faculty_id='%s'"%(type_id)
	a=update(q)
	if a:
		flash("Deleted Successfully")
		return redirect(url_for('bunk.bunk_add_faculty'))
	return render_template('bunk_add_faculty.html',data=data)


@bunk.route('/bunk_verify_otp',methods=['get','post'])
def bunk_verify_otp():
    data={}
    # q="SELECT * FROM `user` INNER JOIN booking USING(user_id) WHERE center_id='%s'"%(session['bunk_id'])
    # data['res']=select(q)
    if 'submit' in request.form:
        otp=request.form['otp']
        q1="select * from booking where otp='%s' and center_id='%s'"%(otp,session['bunk_id'])
        res=select(q1)
        if res:
            booking_id=res[0]['booking_id']
            qry = "SELECT * FROM `booking` INNER JOIN `charging_center` USING(`center_id`) INNER JOIN `user` USING(`user_id`) WHERE booking_id='%s'" % (booking_id)
            data['req'] = select(qry)
            return render_template('bunk_otp_details.html',data=data)
        else:
            flash("Wrong otp")
    return render_template('bunk_verify_otp.html', data=data)



@bunk.route('/bunk_view_booking',methods=['get','post'])
def bunk_view_booking():
    data={}
    qry="SELECT * FROM `booking` INNER JOIN `charging_center` USING(`center_id`) INNER JOIN `user` USING(`user_id`) WHERE center_id='%s'"%(session['bunk_id'])
    data['req']=select(qry)
    if 'action' in request.args:
         action=request.args['action']
         bid=request.args['bid']
         id=request.args['uid']
    else:
         action=None
    if action=='accept':
            w="update booking set status='booked' where booking_id='%s'"%(bid)
            update(w)
            q0="select * from user where user_id='%s'"%(id)
            ra=select(q0)
            umail=ra[0]['email']

            print(umail)

            
            ############################
            rd=random.randrange(1000,9999,4)
            # msg=str(rd)
            msg="Your request Accepted"
            data['rd']=rd
            print(rd)
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('projectsriss2020@gmail.com','vroiyiwujcvnvade')
            except Exception as ex:
                print("Couldn't setup email!!"+str(ex))
            msg = MIMEText(msg)
            
            msg['Subject'] = 'EV Booking Status'
            
            msg['To'] = umail
            
            msg['From'] = 'projectsriss2020@gmail.com'
            
            try:
                gmail.send_message(msg)
                print(msg)
                # flash("EMAIL SENED SUCCESFULLY")
                session['rd']=rd
                # return redirect(url_for('public.enterotp'))
                # return redirect(url_for('staff.staff_view_users'))
            except Exception as ex:
                print("COULDN'T SEND EMAIL", str(ex))
                # return redirect(url_for('public.forgotpassword'))
                # return redirect(url_for('staff.staff_view_users'))
                ################################



                flash("Updated Successfully")
                return redirect(url_for('bunk.bunk_view_booking'))
    if action=='reject':
         w="update booking set status='rejected' where booking_id='%s'"%(bid)
         update(w)
         flash("Updated Successfully")
         return redirect(url_for('bunk.bunk_view_booking'))
    return render_template('bunk_view_booking.html',data=data)


@bunk.route('/bunk_addprice',methods=['get','post'])
def bunk_addprice():
      bid=request.args['bid']
      if 'submit' in request.form:
            price=request.form['price']
            
            q="update booking set amount='%s',status='price added' where booking_id='%s'"%(price,bid)
            update(q)
            flash("Amount Added")
            return redirect(url_for('bunk.bunk_view_booking'))

      return render_template("bunk_addprice.html")


@bunk.route('/bunk_verify_user',methods=['get','post'])
def bunk_verify_user():
	data={}
	q="select * from user inner join login using (login_id)"
	res=select(q)
	data['mechanic']=res
	if 'action' in request.args:
		action=request.args['action']
		mid=request.args['cid']
	else:
		action=None
	if action=="approve":
		
		q="update login set usertype='user' where login_id=(select login_id from user where user_id='%s')"%(mid)
		update(q)
		flash("accepted")
		return redirect(url_for('bunk.bunk_verify_user'))
	if action=="reject":
		
		q="update login set usertype='rejected' where login_id=(select login_id from user where user_id='%s')"%(mid)
		update(q)
		flash("rejected")
		return redirect(url_for('bunk.bunk_verify_user'))			
	return render_template('bunk_verify_user.html',data=data)

@bunk.route('/bunk_send_complaint',methods=['get','post'])
def bunk_send_complaint():
    data={}
    q="select * from complaint where sender_id='%s'"%(session['lid'])
    data['comp']=select(q)
    if 'sub_send' in request.form:
        complaint=request.form['complaint']
        q="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['lid'],complaint)
        insert(q)
        flash("Complaint Sent")
        return redirect(url_for('bunk.bunk_send_complaint'))			
    return render_template("bunk_send_complaint.html",data=data)

    
# @bunk.route('/bunk_view_type',methods=['get','post'])
# def bunk_view_type():
#     data={}
#     qry="SELECT * FROM `station_type` WHERE `type_id` NOT IN(SELECT `type_id` FROM `my_type` WHERE `bunk_id`='%s')"%(session['bunk_id'])
#     ss=data['type']=select(qry)
#     # if ss:
#     return render_template('bunk_view_types.html',data=data)
#     # else:
#     #     return redirect(url_for('bunk.bunk_home'))	
        
        
# @bunk.route('/bunk_add_as_service',methods=['get','post'])
# def bunk_add_as_service():
    
#     type_id=request.args['type_id']
#     q="INSERT INTO `my_type` VALUES(NULL,'%s','%s')"%(session['bunk_id'],type_id)
#     q=insert(q)
#     if q:
#         flash("Added as your Service")
#     return redirect(url_for('bunk.bunk_view_type'))	


# @bunk.route('/Manage_bunk_profile',methods=['get','post'])
# def Manage_bunk_profile():
#     data={}
#     qry="select * from bunk where `bunk_id`='%s'"%(session['bunk_id'])
#     data['pro']=select(qry)
#     if 'submit' in request.form:
#         firstname=request.form['firstname']
#         place=request.form['place']
#         phone=request.form['phone']
#         email=request.form['email']
#         latitude=request.form['latitude']
#         longitude=request.form['longitude']
#         q="update bunk set name='%s',place='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where bunk_id='%s'"%(firstname,place,latitude,longitude,phone,email,session['bunk_id'])
#         update(q)
#         flash("Updated successfully")
#         return redirect(url_for('bunk.Manage_bunk_profile'))
#     return render_template('bunk_manage_profile.html',data=data)
   

     
# @bunk.route('/bunk_view_request',methods=['get','post'])
# def bunk_view_request():
#     data={}
#     qry="SELECT * FROM `rechargerequest` INNER JOIN `my_type` USING(`my_type_id`) INNER JOIN `user` USING(`user_id`) WHERE `my_type`.bunk_id='%s'"%(session['bunk_id'])
#     data['req']=select(qry)
#     return render_template('bunk_view_request.html',data=data)
     
# @bunk.route('/bunk_view_payment',methods=['get','post'])
# def bunk_view_payment():
#     data={}
#     rrequest_id=request.args['rrequest_id']
#     qry="SELECT * FROM `payment`  WHERE `requestedfor`='rechargerequest'  AND requested_id='%s'"%(rrequest_id)
#     ss=data['pay']=select(qry)
#     if not ss:
#         flash('Not Payed')
#         return redirect(url_for('bunk.bunk_view_request'))
#     return render_template('bunk_view_payment.html',data=data)

# @bunk.route('/bunk_send_service_charge',methods=['get','post'])
# def bunk_send_service_charge():
#     data={}
#     if "rrequest_id" in request.args:
#         session['rrequest_id']=request.args['rrequest_id']
#     if "submit" in request.form:
#         amnt=request.form['reply']
#         qry="update rechargerequest set amount='%s',status='accepted' where rrequest_id='%s'"%(amnt,session['rrequest_id'])
#         ss=data['pay']=update(qry)
#         if  ss:
#             flash('Sent Successfully')
#             return redirect(url_for('bunk.bunk_view_request'))
#     return render_template('bunk_send_service_charge.html')
     
   
# @bunk.route('/bunk_view_compliants',methods=['get','post'])
# def bunk_view_compliants():
#     data={}
#     qry="SELECT * FROM `complaint` INNER JOIN `login` ON `complaint`.`receiver_id`=`login`.`login_id` WHERE login_id='%s'"%(session['lid'])
#     data['req']=select(qry)
#     return render_template('bunk_view_compliants.html',data=data)  

# @bunk.route('/bunk_view_type',methods=['get','post'])
# def bunk_view_type():
#     data={}
#     qry="SELECT * FROM `my_type` WHERE `bunk_id`='%s'"%(ssession['bunk_id'])
#     data['req']=select(qry)
#     return render_template('bunk_view_types.html',data=data)   
#  	