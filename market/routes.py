from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
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
            password=form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #si no hay errores de las validaciones
        for err_msg in form.errors.values():
            flash(f'Hubo un error creando el usuario: {err_msg}', category='danger')
            
    return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template("login.html", form=form)
