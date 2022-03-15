from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    pas_astr = PasswordField('пароль астронавта', validators=[DataRequired()])
    id_cap = BooleanField('id капитана', validators=[DataRequired()])
    pas_cap = PasswordField('пароль капитана', validators=[DataRequired()])
    submit = SubmitField("Доступ")