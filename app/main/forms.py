from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required,Email
from ..models import Subscribe

class BlogForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    content = StringField('content',validators=[Required()])
    category = SelectField('Category', choices=[('Choose Category', 'Choose Category'),('emotional', 'emotional'),('skills', 'skills')])
    review = TextAreaField('pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    
    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    title = StringField('Entre Your Name' ,validators=[Required()])
    submit = SubmitField('Subscribe')    

    def validate_email(self,data_field):
                if Subscribe.query.filter_by(email =data_field.data).first():
                    raise ValidationError('Sorry, there is an account with that email')