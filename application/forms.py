from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

class UploadForm(FlaskForm):
    title = StringField('Title',
            validators=[
                DataRequired(),
                Length(min=4, max=100)
                ]
            )

    category = SelectField('Category',
            validators=[
                DataRequired()
                ], choices = [("ACTIVITY", "Activity"),("MOOD", "Mood")]
            )
    link = StringField('Link',
            validators=[
                DataRequired(),
                Length(min=10, max=100)

            ]
        )
    submit = SubmitField('Submit')



class RegistrationForm(FlaskForm):
    
    first_name = StringField('First Name',
            validators=[
                DataRequired(),
                Length(min=2,max=30)
            ])
    last_name = StringField('Last Name',
            validators=[
                DataRequired(),
                Length(min=3, max=30)
            ])



    email = StringField('Email',
            validators = [
               DataRequired(), 
                Email()
            ]
        )
    password = PasswordField('Password',
            validators = [
                DataRequired(),
            ]
        )

    confirm_password = PasswordField('Confirm Password',
            validators = [
                DataRequired(),
                EqualTo('password')
            ]
        )

    submit = SubmitField('Sign Up')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )

    password = PasswordField('Password', 
            validators=[
                DataRequired()

            ]
        )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

