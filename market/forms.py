from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    usuario = StringField(label='Nombre de Usuario:')
    email = StringField(label='Email:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirmar Password:')
    submit = SubmitField(label='Crear Cuenta')