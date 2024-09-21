from flask import Flask, render_template, request, redirect
import firebase_admin 
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Inicializa Firebase
cred = credentials.Certificate('C:\credencial\omar-e61f4-firebase-adminsdk-v27x0-725e0d4e28.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    # Recupera contactos de la base de datos
    contacts_ref = db.collection('contacts')
    contacts = [doc.to_dict() for doc in contacts_ref.stream()]  
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    db.collection('contacts').add({'name': name, 'phone': phone})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
