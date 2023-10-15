from flask import *
from database import *
import uuid
from ev_review import *

admin=Blueprint('admin',__name__)



@admin.route('/adminhome')
def adminhome():
	if session.get('login_id') is None:

		return redirect (url_for('public.login'))
	else:
		return render_template('admin_home.html')





# @admin.route('/addprofile',methods=['get','post'])
# def addprofile():
# 	data={}
# 	if 'save' in request.form:
# 		name=request.form['na']
# 		place=request.form['pl']
# 		phone=request.form['ph']
# 		email=request.form['em']
# 		q="insert into profile values(null,'%s','%s','%s','%s')"%(name,place,phone,email)
# 		insert(q)
# 		p="select * from profile"
# 		rs=select(p)
# 		data['view']=rs
# 		return redirect(url_for('admin.addprofile'))

# 	return render_template('admin_addprofile.html',data=data)



@admin.route('/profile',methods=['get','post'])
def profile():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		q="select * from profile"
		res=select(q)
		data['view']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else: 
			action=None

		if action=='update':
			q2="select * from profile where profile_id='%s' "%(id)
			res1=select(q2)
			data['up']=res1

		if 'update' in request.form:
			na=request.form['name']
			pl=request.form['place']
			ph=request.form['phone']
			em=request.form['email']
			q3="update profile set name='%s',place='%s',phone='%s',email='%s' where profile_id='%s'"%(na,pl,ph,em,id)
			update(q3)
			return redirect(url_for('admin.profile'))
		return render_template('admin_profile.html',data=data)





@admin.route('/managectgry',methods=['get','post'])
def managectgry():
	if session.get('login_id')is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		if 'submit' in request.form:
			ctgry=request.form['ctgry']
			p="insert into category values(null,'%s')"%(ctgry)
			insert(p)
		qry="select * from category"
		res=select(qry)
		data['view']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else: 
			action=None

		if action=='update':
			qry1="select * from category where category_id='%s' "%(id)
			res1=select(qry1)
			data['up']=res1

		if 'update' in request.form:
			cat=request.form['ctgry']
			qry3="update category set category='%s' where category_id='%s'"%(cat,id)
			update(qry3)


		if action=='delete':
			q="delete from category where category_id='%s'"%(id)
			delete(q)
			return redirect(url_for('admin.managectgry'))
		return render_template('manage_category.html',data=data)








@admin.route('/managearts',methods=['get','post'])
def managearts():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		if 'submit' in request.form:
			cid=request.form['cat']
			arts=request.form['arts']
			image=request.files['img']
			amnt=request.form['amnt']
			path='static/'+str(uuid.uuid4())+image.filename
			image.save(path)
			
			q0="select * from arts where arts='%s'"%(arts)
			res2=select(q0)
			
			if res2:
				flash('already exist')
			else:
				p="insert into arts values(null,'%s','%s','%s','%s')" %(cid,arts,path,amnt)
				insert(p)
				return redirect(url_for('admin.managearts'))
		q="select * from arts inner join category using(category_id)"
		res=select(q)
		data['view']=res
		q1="select * from category"
		data['cat']=select(q1)	

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else: 
			action=None

		if action=='update':
			q1="select * from arts where arts_id='%s' "%(id)
			res1=select(q1)
			data['up']=res1

		if 'update' in request.form:
			arts=request.form['arts']
			image=request.files['img']
			path='static/'+str(uuid.uuid4())+image.filename
			image.save(path)
			amnt=request.form['amnt']
			q3="update arts set arts='%s',image='%s',amount='%s' where arts_id='%s'"%(arts,path,amnt,id)
			update(q3)

		if action=='delete':
			q4="delete from arts where arts_id='%s'"%(id)
			delete(q4)
		
			return redirect(url_for('admin.managearts'))

		return render_template('manage_arts.html',data=data)




@admin.route('/managesize',methods=['get','post'])
def managesize():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		p="select * from size inner join category using(category_id)"
		ress=select(p)
		data['view']=ress

		q3="select * from category"
		rr=select(q3)
		data['category']=rr

		if 'submit' in request.form:
			catgy=request.form['category']
			size=request.form['size']
			amount=request.form['amnt']
			q="insert into size values(null,'%s','%s','%s')"%(catgy,size,amount)
			insert(q)
			return redirect(url_for('admin.managesize'))
		
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else: 
				action=None

		if action=='update':
			qry1="select * from size  where size_id='%s'"%(id)
			res1=select(qry1)
			data['up']=res1

		if 'update' in request.form:
			si=request.form['size']
			am=request.form['amnt']
			qry3="update size set sizee='%s',amount='%s' where size_id='%s'"%(si,am,id)
			update(qry3)
			return redirect(url_for('admin.managesize'))


		if action=='delete':
			q="delete from size where size_id='%s'"%(id)
			delete(q)
			return redirect(url_for('admin.managesize'))
		return render_template('manage_size.html',data=data)


@admin.route('/addartworks',methods=['get','post'])
def addartworks():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		if 'upload' in request.form:
			upimg=request.files['upimg']
			path='static/'+str(uuid.uuid4())+upimg.filename
			upimg.save(path)
			des=request.form['des']
			q0="select * from artworks where description='%s'"%(des)
			res1=select(q0)
			
			if res1:
				flash('already exist')
			else:
				q="insert into artworks values(null,'%s','%s')"%(path,des)
				insert(q)
		p="select * from artworks"
		res=select(p)
		data['view']=res
		

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']

		else: 
			action=None

		if action=='update':
			p1="select * from artworks where artworks_id='%s' "%(id)
			res1=select(p1)
			data['up']=res1

		if 'update' in request.form:
			image=request.files['upimg']
			path='static/'+str(uuid.uuid4())+image.filename
			image.save(path)
			des=request.form['des']
			p3="update artworks set upload_image='%s',description='%s' where artworks_id='%s'"%(path,des,id)
			update(p3)



		if action=='delete':
			q="delete from artworks where artworks_id='%s'"%(id)
			delete(q)

			return redirect(url_for('admin.addartworks'))


		return render_template('add_myartworks.html',data=data)





@admin.route('/viewbooking',methods=['get','post'])
def viewbooking():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:

		data={}
		q="SELECT * FROM booking INNER JOIN `user` USING (user_id) INNER JOIN arts USING (arts_id) INNER JOIN size USING (size_id) " 
		r=select(q)
		data['book']=r
		return render_template('view_booking.html',data=data)



@admin.route('/viewpayment', methods=['get','post'])
def viewpayment():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		p="SELECT * FROM payment INNER JOIN booking USING (book_id) INNER JOIN `user` USING (user_id)"
		r1=select(p)
		data['pay']=r1
		# return redirect(url_for('admin.viewpayment'))
		return render_template('view_payment.html',data=data)




@admin.route('/viewreview', methods=['get','post'])
def viewreview():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		q="SELECT * FROM review INNER JOIN booking USING (book_id) INNER JOIN `user` USING (user_id)"
		res=select(q)
		data['review']=res
		# return redirect(url_for('admin.viewbooking'))
		return render_template('view_review.html',data=data)




@admin.route('/viewcomplaint', methods=['get','post'])
def viewcomplaint():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		q="SELECT * FROM complaint INNER JOIN `user` USING (user_id)"
		r=select(q)
		data['comp']=r
		return render_template('view_complaints.html',data=data)



@admin.route('/send_reply',methods=['get','post'])
def send_reply():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		cid=request.args['cid']
		if 'sendreply' in request.form:
			rep=request.form['reply']
			# uid=request.form['user_id']
			q="update complaint set reply='%s' where complaint_id='%s'"%(rep,cid)
			update(q)
			return redirect(url_for('admin.viewcomplaint'))
		return render_template('send_reply.html')







@admin.route('/viewcustorder', methods=['get','post'])
def viewcustorder():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		p="SELECT * ,request.amount as request_amount FROM request INNER JOIN category USING (category_id) INNER JOIN size USING (size_id)"
		res=select(p)
		data['order']=res
		return render_template('view_custorder.html',data=data)



@admin.route('/addamount',methods=['get','post'])
def addamount():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		rid=request.args['rid']
		if 'reply' in request.form:
			amnt=request.form['amount']
			q="update request set amount='%s' where request_id='%s'"%(amnt,rid)
			update(q)
			return redirect(url_for('admin.viewcustorder'))
		return render_template('add_amount.html')




@admin.route('/vieworderpay', methods=['get','post'])
def vieworderpay():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		p="SELECT * FROM payment INNER JOIN booking USING (book_id) INNER JOIN `user` USING (user_id) INNER JOIN request ON payment.payment_id=request.request_id "
		r1=select(p)
		data['orderpay']=r1
		# return redirect(url_for('admin.viewbooking'))
		return render_template('view_orderpayment.html',data=data)




@admin.route('/vieworderreview',methods=['get','post'])
def vieworderreview():
	if session.get('login_id') is None:
		return redirect (url_for('public.login'))
	else:
		data={}
		q="SELECT * FROM payment INNER JOIN booking USING (book_id) INNER JOIN `user` USING (user_id) INNER JOIN request ON payment.payment_id=request.request_id "
		r2=select(q)
		data['orderreview']=r2
		# return redirect(url_for('admin.viewbooking'))
		return render_template('view_orderreview.html',data=data)


# @admin.route('/viewrating',methods=['get','post'])
# def viewrating():
#     data={}
#     q="SELECT * FROM `review` INNER JOIN `booking` USING(`book_id`)"
#     res=select(q)
#     review_dict = {}
#     for i in res:
#         arts_id = i['arts_id']
#         if arts_id not in review_dict:
#             q1 = "SELECT DISTINCT review FROM review INNER JOIN `booking` USING(`book_id`) WHERE arts_id='%s'" % arts_id
#             r1 = select(q1)
#             for row in r1:
#                 review_dict[arts_id] = r1
#                 print(review_dict[arts_id])
#                 rating=review_pred(row['review'],arts_id)
#                 print("RRRR : ",rating)
#     return render_template('view_orderreview.html',data=data)
        

@admin.route('/viewrating',methods=['get','post'])
def viewrating():
    data={}
    q="SELECT review, arts_id FROM review INNER JOIN `booking` USING(`book_id`) GROUP BY arts_id ORDER BY review"
    res=select(q)
    review_dict = {}
    for i in res:
        arts_id = i['arts_id']
        review = i['review']
        if arts_id not in review_dict:
            review_dict[arts_id] = []
        review_dict[arts_id].append(review)
    sorted_reviews = []
    for arts_id, reviews in review_dict.items():
        rating = review_pred(reviews)
        sorted_reviews.append((arts_id, rating))
    sorted_reviews = sorted(sorted_reviews, key=lambda x: x[1], reverse=False)
    print("sorted_reviews : ",sorted_reviews)
    return render_template('view_orderreview.html', data=sorted_reviews)






















    