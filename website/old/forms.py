from flask_wtf import FlaskForm
from flask_login import current_user
from website import bcrypt

from wtforms import * #
from wtforms.validators import * #

'from models import User' 'User must be created in models or DB tables'  #this should come from BAZZ

'got any doubts?  refer to wtforms stackoverflow'

#Registeration form; all data input and validation for the registration form go here. 
class RegistrationForm(FlaskForm):
    #Flask has several unique methods of validation. The 'validators' parameter determines what aspects of submitted data are validated.
    #The 'validator' parameter technically just executes the functions specified E.G. DataRequired(), Length() so you can define
    #your own validators!

    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    #lastname = StringField('lastname', validators=[DataRequired(), Length(min=1, max=20)])
    
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    'dob = whoever doing this make sure u check the rigght validation object like if u see above we got PasswordField yano'
    'phone_number do the same here AND we are ditching profile picture'
    submit = SubmitField('Sign Up')
    
    #Validation specifically to ensure no repeat emails are accepted.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()  #THIS USER COMES FROM  BAZZ
        if user:
            raise ValidationError('That email address has been taken. Please select another email address.')

#Login form; all data input and validation for the login form go here.  
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')