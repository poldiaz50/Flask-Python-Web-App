from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            usuario=form.usuario.data,
            email=form.email.data,
            password_hash=form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #si no hay errores de las validaciones
        for err_msg in form.errors.values():
            print(f'Hubo un error creando un usuario: {err_msg}')
            
    return render_template("register.html", form=form)
