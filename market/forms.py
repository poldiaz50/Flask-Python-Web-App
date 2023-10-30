from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_usuario(self, usuario_to_check):
        user = User.query.filter_by(usuario=usuario_to_check.data).first()
        if user:
            raise ValidationError("Nombre de usuario ya existe!")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Email ya existe")

    usuario = StringField(
        label="Nombre de Usuario:", validators=[Length(min=3, max=30), DataRequired()]
    )
    email = StringField(label="Email:", validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label="Password:", validators=[Length(min=6), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirmar Password:", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Crear Cuenta")


class LoginForm(FlaskForm):
    usuario = StringField(label="Nombre de usuario:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Ingresar")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Comprar Articulo")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Devolver Articulo")
