from . import app, db
from flask_sqlalchemy import SQLAlchemy

class Vue_Utilisateur(db.Model):
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), unique=True, nullable=False)
    prenom = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)


def __repr__(self):
    return (f'{self.id_utilisateur}: {self.nom}: {self.prenom}: {self.email}')