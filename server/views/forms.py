from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify
from flask_login import login_required, logout_user, login_user, current_user

from server.models.users import Users
from server.models.roles import Roles
from server.models.properties import Properties
from passlib.hash import sha256_crypt
from flask_mail import Message


from server.utils.hwp_email_template import html_consultation_form
# from validate_email import validate_email

from server.forms.forms import ConsultationForm, ContactForm
from sqlalchemy import or_
from server.utils.query_utils import serialize, get_associations

import json

from server import db, mail

mod = Blueprint('forms', __name__)


@mod.route('/consultation-form', methods=['POST'])
def consultation_form_post():

	form = ConsultationForm(request.form)

	if not form.validate():
		abort(400)


	name = form['first_name'].data + " " + form['last_name'].data
	email_content = html_consultation_form(name = name,
										email = form['email'].data,
										phone_num =form['phone_num'].data,
										regarding = form['regarding'].data,
										msg = form['msg'].data
										)

	try:
		sender = Roles.query.filter_by(role_name='Consultation Form Sender').one()
		print(sender)
		receivers = Roles.query.filter_by(role_name='Consultation Form Receiver').one()
	except:
		abort(400)

	# recipients = receivers.emails
	recipients = [r.email for r in receivers.emails]
	sender = [s.email for s in sender.emails]

	msg = Message()
	msg.html = email_content
	msg.recipients = recipients
	msg.sender = sender
	msg.subject = 'Consultation Form Submission'

	mail.send(msg)

	#send email

	return 1

@mod.route('/consultation-form', methods=['POST'])
def contact_form_post():
	return 1