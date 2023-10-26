from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'nombre': 'Telefono', 'barcode': '893212299897', 'precio': 500},
        {'id': 2, 'nombre': 'Laptop', 'barcode': '123985473|65', 'precio': 900},
        {'id': 3, 'nombre': 'Teclado', 'barcode': '231985128446', 'precio': 150},
    ]
    return render_template('market.html', items=items)
    