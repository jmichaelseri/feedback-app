from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, \
    RadioField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    service = SelectField('Services', choices=[
        ('Feedback on shipping', 'Shipping'),
        ('Feedback on price', 'Price'),
        ('Feedback on offers', 'Offers'),
        ('Feedback on user experience', 'User Experience')
    ])
    rating = RadioField('Rating', choices=[
        ('1', '1'), ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5'), ('6', '6'),
        ('7', '7'), ('8', '8'),
        ('9', '9'), ('10', '10')
    ], validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Send')
