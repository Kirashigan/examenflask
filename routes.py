from flask import render_template,url_for
from . import app, models


@app.route('/')
@app.route('/accueil')
def accueil():
    return render_template('accueil.html',title='Boutique de souvenir')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',title='Boutique de souvenir')

@app.route('/tous_user')
def tous_user():
    liste_user = Vue_Utilisateur.query.all()
    return render_template('tous_utilisateur.html', title='Boutique de souvenir', liste_user=liste_user)