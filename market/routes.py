from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        #purchase item logic
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(nombre=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(
                    f"Has Comprado {p_item_object.nombre} por {p_item_object.precio}$",
                    category="success",
                )
            else:
                flash(
                    f"No tienes suficientes fondos! para comprar {p_item_object.nombre}",
                    category="danger",
                )
        #sell item logic
        sold_item = request.form.get("sold_item")
        s_item_object = Item.query.filter_by(nombre=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(
                    f"Has Devuelto este arcticulo: {s_item_object.nombre} al market",
                    category="success",
                )
            else:
                flash(
                    f"Algo salio mal devolviendo el articulo: {s_item_object.nombre}",
                    category="danger",
                )
            
        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template(
            "market.html",
            items=items,
            purchase_form=purchase_form,
            owned_items=owned_items,
            selling_form=selling_form,
        )


@app.route("/register", methods=["GET", "POST"])
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

        login_user(user_to_create)
        flash(
            f"Cuenta Creada con Exito¡ Ahora estas logeado como: {user_to_create.usuario}",
            category="success",
        )
        return redirect(url_for("market_page"))

        return redirect(url_for("market_page"))
    if form.errors != {}:  # si no hay errores de las validaciones
        for err_msg in form.errors.values():
            flash(f"Hubo un error creando el usuario: {err_msg}", category="danger")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(usuario=form.usuario.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f"Exito¡ Estas logueado como: {attempted_user.usuario}",
                category="success",
            )
            return redirect(url_for("market_page"))
        else:
            flash(
                "Nombre de usuario o password no son correctos, intente de nuevo.",
                category="danger",
            )

    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("Ud. ha salido del registro¡", category="info")
    return redirect(url_for("home_page"))
