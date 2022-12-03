from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import DataRequired , ValidationError


def checkInt(field):
        if type(field.data) != int:
            raise ValidationError('Please enter the numerical data')

class Predict_Form(FlaskForm):

    sepal_length = StringField('Sepal Length',validators=[DataRequired(),checkInt])
    sepal_width = StringField('Sepal Width',validators=[DataRequired(),checkInt])
    petal_length = StringField('Petal Length',validators=[DataRequired(),checkInt])
    petal_width = StringField('Petal Width',validators=[DataRequired(),checkInt])
    submit = SubmitField('Predict')
    