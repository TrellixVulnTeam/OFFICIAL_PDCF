from server.models.users import Users
from server.models.properties import Properties, PropertyTypes, Cities
from server.models.associations import Associations

from server.models.roles import Roles, Emails
from passlib.hash import sha256_crypt
# from flask_mail import Message


from server import db

users = [{
	'first':'mirai',
	"last":'kuriyama',
	'email':'mirai@gmail.com',
	'password':'party123',
	'is_admin':True,
	'is_verified':True
	},
	{
	'first': 'rikka',
	'last':'takanashi',
	'email':'rikka@gmail.com',
	'password':'party123',
	'is_admin':False
	}]

properties = [{
	'name':'property1',
	'address_l1': '123 center st',
	'address_l2':'',
	'city':'Los Angeles',
	'state': 'CA',
	'zipcode': '11111',
	'type':'condo',
	'beds':2,
	'baths': 1,
	'price': 1000,
	'for_sale':True,
	'for_rent':True,
	'area':1000,
	'notes':'This is a beautiful condo',
	'poster_id':1,
	'images':''
	},
	{
	'name':'property2',
	'address_l1': '123 middle st',
	'address_l2':'apt no. 123',
	'city':'Sacramento',
	'state': 'CA',
	'zipcode': '22222',
	'type':'apartment',
	'beds':3,
	'baths': 1.5,
	'price': 2500,
	'for_sale':False,
	'for_rent':True,
	'area':2000,
	'notes':'This is a beautiful apartment',
	'poster_id':1,
	'images':''
	},
	{
	'name':'property3',
	'address_l1': '321 center st',
	'address_l2':'',
	'city':'Reno',
	'state': 'NV',
	'zipcode': '33333',
	'type':'duplex',
	'beds':1,
	'baths': 0,
	'price': 1000,
	'for_sale':False,
	'for_rent':True,
	'area':500,
	'notes':'This is a beautiful duplex',
	'poster_id':1,
	'images':''
	},
	{
	'name':'property4',
	'address_l1': '123 center st',
	'address_l2':'',
	'city':'Sacramento',
	'state': 'FL',
	'zipcode': '44444',
	'type':'condo',
	'beds':2.5,
	'baths': 1,
	'price': 3000,
	'for_sale':True,
	'for_rent':False,
	'area':2300,
	'notes':'This is a beautiful condo',
	'poster_id':1,
	'images':''
	}]
associations=[{
	'acn_name':'acn1',
	'acn_loc':'acn_loc1'
	},{
	'acn_name':'acn2',
	'acn_loc':'acn_loc2'
	},{
	'acn_name':'acn3',
	'acn_loc':'acn_loc3'
	}]
roles=[{
	'role_name':'Consultation Form Sender'
	}
	,{
	'role_name':'Consultation Form Receiver'
	}]

emails=[{
	'email':'hwptesting@gmail.com'
	},
	{
	'email':'cooljoshua11@gmail.com'
	}]
	

def testdb_init(properties, users):
	for u in users:
		try:
			user = Users.query.filter_by(email=u['email']).one()
		except:
			user = Users(u)
			db.session.add(user)
			db.session.flush()
			# print('user added')
	
	print('in props')
	for p in properties:
	
		try:
			type = PropertyTypes.query.filter_by(type_name=p['type']).one()
			p['type'] = type.type_id
		except:
			type = PropertyTypes(type_name=p['type'])
			db.session.add(type)
			db.session.flush()
			p['type'] = type.type_id
			# print('property type added')
	
		try:
			city = Cities.query.filter_by(city_name=p['city']).one()
			p['city'] = city.city_id

		except:
			city = Cities(city_name=p['city'])
			db.session.add(city)
			db.session.flush()
			p['city'] = city.city_id
			# print('city added')
	
		try:
			prop = Properties.query.filter_by(name=p['name']).one()
		except:
			new_prop = Properties(p)
			db.session.add(new_prop)
			# print('property added')

	for a in associations:
		asn = Associations(a['acn_name'], a['acn_loc'])
		db.session.add(asn)

	for e in emails:
		try:
			email = Emails.query.filter_by(email = e['email']).one()
		except:
			email = Emails(e['email'])
			db.session.add(email)
			db.session.flush()


	for r in roles:
		try:
			role = Roles.query.filter_by(role_name = r['role_name']).one()
		except:
			role = Roles(r['role_name'])
			db.session.add(role)
			db.session.flush()
			if r['role_name'] == 'Consultation Form Sender':
				email = Emails.query.filter_by(email=emails[0]['email']).one()
				role.add_email(email)
			elif r['role_name'] == 'Consultation Form Receiver':
				email = Emails.query.filter_by(email=emails[1]['email']).one()
				role.add_email(email)



	try:
		db.session.commit()
		print('users and properties added')
	except:
		db.session.rollback()
		print('db init failed or already done before')

testdb_init(properties, users)
