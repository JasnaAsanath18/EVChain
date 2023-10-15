from flask import *
from database import *
import uuid
import json
from web3 import Web3,HTTPProvider
# from Crypto.Hash import scrypt


admin=Blueprint('admin',__name__)


# -----------------------------------------------------------------------------------

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = r'C:\\RISS PROJECTS D\\Jawahar College\\ev chain\\ev\build\\contracts\\evchain.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x3e8181fA42b85FE3d575A3e19bD4377b64de966D'



# --------------------------------------------------------------------------------------


@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')


@admin.route('/admin_verify_bunk',methods=['get','post'])
def admin_verify_bunk():
	data={}
	q="select * from charging_center inner join login using (login_id)"
	res=select(q)
	data['mechanic']=res
	# centerid=res[0]['center_id']
	# centername=res[0]['center_name']
	# phone=res[0]['phone']
	# email=res[0]['email']
	# latitude=res[0]['latitude']
	# longitude=res[0]['longitude']
	# place=res[0]['place']

	if 'action' in request.args:
		action=request.args['action']
		mid=request.args['cid']
	else:
		action=None
	if action=="approve":
		print("mid",mid)
		q = "select * from charging_center where center_id='%s'"%(mid)
		res = select(q)

		centerid = res[0]['center_id']
		centername = res[0]['center_name']
		phone = res[0]['phone']
		email = res[0]['email']
		latitude = res[0]['latitude']
		longitude = res[0]['longitude']
		place = res[0]['place']
		print("data:", centerid, centername)
		# ----------------------------------------------

		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		blocknumber = web3.eth.get_block_number()

		# contract function name


		message2 = contract.functions.add_info(blocknumber,int(centerid),centername,phone,email,latitude,longitude,place).transact()
		print("ssssssssssssssssssssssssssssssss",message2)


		# message2 = contract.functions.add_info(blocknumber,int(centerid),centername,phone,email,latitude,longitude,place).transact()
		res1 = []



		q="update login set usertype='bunk' where login_id=(select login_id from charging_center where center_id='%s')"%(mid)
		update(q)
		flash("accepted")
		return redirect(url_for('admin.admin_verify_bunk'))
	if action=="reject":
		
		q="update login set usertype='rejected' where login_id=(select login_id from charging_center where center_id='%s')"%(mid)
		update(q)
		flash("rejected")
		return redirect(url_for('admin.admin_verify_bunk'))			
	return render_template('admin_verify_bunk.html',data=data)

@admin.route('/admin_view_complaint',methods=['get','post'])
def admin_view_complaint():
	data={}
	q="(SELECT `complaint`,`reply`,`date`,`email`,`phone`,complaint_id,CONCAT(firstname,' ',lastname,'(user)')AS sender FROM complaint INNER JOIN `user` ON complaint.`sender_id`=user.`login_id`)UNION(SELECT `complaint`,`reply`,`date`,`email`,`phone`,complaint_id,CONCAT(center_name,' ','(charging station)')AS sender FROM complaint INNER JOIN `charging_center` ON complaint.`sender_id`=charging_center.`login_id`)"
	res=select(q)
	data['comp']=res
	return render_template('admin_view_complaint.html',data=data)

@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
	complaint_id=request.args['complaint_id']
	if 'submit' in request.form:
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s' "%(reply,complaint_id)
		update(q)
		flash("replied")
		return redirect(url_for('admin.admin_view_complaint'))

	return render_template('admin_send_reply.html')



@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	q="select * from feedback inner join user using(user_id) inner join charging_center using(center_id)"
	res=select(q)
	data['feed']=res
	return render_template('admin_view_feedback.html',data=data)


@admin.route('/admin_view_user',methods=['get','post'])
def admin_view_user():
	data={}
	q="select * from user inner join login where usertype='user'"
	res=select(q)
	data['user']=res
	return render_template('admin_view_user.html',data=data)


@admin.route('/admin_manage_faq',methods=['get','post'])
def admin_manage_faq():
	if 'submit' in request.form:
		q=request.form['question']
		p=request.form['answer']
		r="insert into faq values(null,'%s','%s')"%(q,p)
		update(r)
		return redirect(url_for('admin.admin_manage_faq'))
	return render_template("admin_manage_faq.html")




# @admin.route('/admin_add_service_center',methods=['get','post'])
# def admin_add_service_center():
# 	data={}
# 	qry="select * from service_center"
# 	data['sc']=select(qry)
# 	if 'submit' in request.form:
# 		firstname=request.form['firstname']
# 		# lastname=request.form['lastname']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		email=request.form['email']
# 		latitude=request.form['latitude']
# 		longitude=request.form['longitude']
# 		z="insert into service_center values(null,'%s','%s','%s','%s','%s','%s')"%(firstname,place,phone,email,latitude,longitude)
# 		insert(z)
# 		flash("Added successfully");
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		cid=request.args['cid']
# 	else:
# 		action=None
# 	if action=="delete":	
# 		q="DELETE FROM `service_center` WHERE `center_id`='%s'"%(cid)
# 		delete(q)
# 		flash("deleted")
# 		return redirect(url_for('admin.admin_add_service_center'))
# 	if action=="update":
# 		q="select * from `service_center` WHERE `center_id`='%s'"%(cid)
# 		data['mech']=select(q)	
# 	if "sub_upd" in request.form:
		
# 		firstname=request.form['firstname']
# 		# lastname=request.form['lastname']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		email=request.form['email']
# 		latitude=request.form['latitude']
# 		longitude=request.form['longitude']
# 		q="update service_center set firstname='%s',lastname='%s',place='%s',email='%s',phone='%s',latitude='%s',longitude='%s' where center_id='%s'"%(firstname,lastname,place,email,phone,latitude,longitude,cid)
# 		update(q)
# 		flash("Updated successfully")
# 		return redirect(url_for('admin.admin_add_service_center'))
# 	return render_template('admin_add_service_center.html',data=data)


# @admin.route('/admin_view_sparepart',methods=['get','post'])
# def admin_view_sparepart():
# 	data={}
# 	q="select * from sparepart inner join login using(login_id)"
# 	res=select(q)
# 	data['spare']=res
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		lid=request.args['lid']
# 	else:
# 		action=None
# 	if action=='accept':
# 		q="update login set usertype='spare' where login_id='%s'"%(lid)
# 		update(q)
# 		print(q)
# 	if action=='reject':
# 		q="update login set usertype='reject' where login_id='%s'"%(lid)
# 		update(q)	
# 	return render_template('admin_view_spareparts.html',data=data)





# @admin.route('/admin_view_payment',methods=['get','post'])
# def admin_view_payment():
# 	data={}
# 	q="select * from payment"
# 	res=select(q)
# 	data['pay']=res
# 	return render_template('admin_view_payment.html',data=data)					

# @admin.route('/admin_view_rating',methods=['get','post'])
# def admin_view_rating():
# 	data={}
# 	q="SELECT * FROM rating INNER JOIN `user` USING(`user_id`) INNER JOIN `mechanicrequest` ON `mrequest_id`=`requested_id`"
# 	res=select(q)
# 	data['rate']=res
# 	return render_template('admin_view_rating.html',data=data)		

# @admin.route('/admin_add_type',methods=['get','post'])
# def admin_add_type():
# 	data={}
# 	qry="select * from station_type"
# 	data['comp']=select(qry)
# 	if 'submit' in request.form:
# 		type=request.form['reply']
# 		voltage=request.form['voltage']
# 		q="INSERT INTO `station_type` VALUES(NULL,'%s','%s')"%(type,voltage)
# 		insert(q)
# 		return redirect(url_for('admin.admin_add_type'))
# 	return render_template('admin_add_type.html',data=data)	

# @admin.route('/admin_update_type',methods=['get','post'])
# def admin_update_type():
# 	data={}
# 	session['type_id']=type_id=request.args['type_id']
# 	qry="select * from station_type where type_id='%s'"%(type_id)
# 	data['up']=select(qry)
# 	if 'update' in request.form:
# 		type=request.form['reply']
# 		voltage=request.form['voltage']
# 		q="update  `station_type` set voltage='%s',type_name='%s' where type_id='%s'"%(voltage,type,session['type_id'])
# 		a=update(q)
# 		if a:
# 			flash("Updated Successfully")
# 			return redirect(url_for('admin.admin_add_type'))
# 	return render_template('admin_update_type.html',data=data)	



# @admin.route('/admin_delete_type',methods=['get','post'])
# def admin_delete_type():
# 	data={}
# 	type_id=request.args['type_id']
# 	q="delete from `station_type`  where type_id='%s'"%(type_id)
# 	a=update(q)
# 	if a:
# 		flash("Deleted Successfully")
# 		return redirect(url_for('admin.admin_add_type'))
# 	return render_template('admin_add_type.html',data=data)	

