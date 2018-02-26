from wtforms import Form, BooleanField, IntegerField, StringField, DecimalField, validators
from server.forms.form_utils import *



class ConsultationForm(Form):
    def regarding_validator(field):
        message='Choose one.'
        if not field.data in regarding_dropdown():
            raise ValidationError(message)

    def regarding_dropdown(*args):
        list = ['Association Management', 'Residential Property Management', 'Available Properties', 'Listing Properties', 'Employment Opportunities', 'Other']
        return list

    first_name = StringField('First Name', [validators.DataRequired(message=required()),
                                            validators.Length(min=1, max=30, message=len_error_msg(min=1, max=30))])
    last_name  = StringField('Last Name', [validators.DataRequired(message=required()),
                                            validators.Length(min=1, max=30, message=len_error_msg(min=1, max=30))])
    email      = StringField('Email', [validators.DataRequired(message=required()),
                                        validators.Length(min=1, max=30, message=len_error_msg(min=1, max=100)),
                                        validators.Email(message='Please enter a valid email.')])
    phone_num  = StringField('Phone Number', [validators.Length(min=10,max=11, message='Please enter a valid phone number.')])
    regarding  = StringField('Regarding', [validators.DataRequired(message=required()),
                                            regarding_validator])
    msg        = StringField('Message', [validators.Length(max=1000, message=len_error_msg(max=1000))])





class PropertyForm(Form):
    name       = StringField('Property Name', [validators.Length(max=200, message=len_error_msg(max=200)), 
                                                validators.DataRequired(message=required())])
    address_l1 = StringField('Address Line 1', [validators.Length(min=1, max=200, message=len_error_msg(min=1, max=200)), 
                                                validators.DataRequired(message=required())])
    address_l2 = StringField('Address Line 2', [validators.Length(max=200, message=len_error_msg(max=200))])
    city       = StringField('City', [validators.Length(min=1, max=200, message=len_error_msg(min=1,max=200)), 
                                        validators.DataRequired(message=required())])
    state      = StringField('State', [validators.Length(min=2, max=2, message=len_error_msg(fixed=2)), 
                                        validators.DataRequired(message=required())])
    zipcode    = StringField('Zipcode', [validators.Length(min=5, max=5, message=len_error_msg(fixed=5)), 
                                            validators.DataRequired(message=required())])
    type       = StringField('Property Type', [validators.Length(max=200, message=required()), 
                                            validators.DataRequired(message=required())])
    beds       = DecimalField('Beds', [validators.NumberRange(min=0, message=int_error_msg(min=0)), 
                                        decimal_check, 
                                        validators.DataRequired(message=required())])
    baths      = DecimalField('Baths', [validators.NumberRange(min=0, message=int_error_msg(min=0)), 
                                        decimal_check, 
                                        validators.DataRequired(message=required())])
    price      = IntegerField('Price', [validators.NumberRange(min=0, message=int_error_msg(min=0)), 
                                        validators.DataRequired(message=required())])
    for_sale   = BooleanField('For Sale')
    for_rent   = BooleanField('For Rent')
    area       = IntegerField('Area (sq ft)', [validators.NumberRange(min=0, message=int_error_msg(min=0)), 
                                                validators.DataRequired(message=required())])
    notes      = StringField('Notes/Comments', [validators.Length(max=2000, message=len_error_msg(max=2000))])

