from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False, unique=True)
    precio = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    descripcion = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
     return f'Item{self.nombre}'