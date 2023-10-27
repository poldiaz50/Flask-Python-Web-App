from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    usuario = StringField(label='Nombre de Usuario:', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Password:' , validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Crear Cuenta')