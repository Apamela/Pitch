from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('pitch review', validators=[Required()])
    submit = SubmitField('Submit')
class PitchForm(FlaskForm):
    title = TextAreaField('Title',validators = [Required()])
	description = TextAreaField(" the pitch you need",validators=[Required()])
    submit = SubmitField('Submit')
class UpvoteForm(FlaskForm):
      submit = SubmitField()
class Downvote(FlaskForm):
    submit = SubmitField()