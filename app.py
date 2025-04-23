import json
import os
from flask import Flask, request, jsonify
from flask_serverless import FlaskServerless

app = Flask(__name__)
serverless = FlaskServerless(app)

# Cargar las notas desde un archivo JSON
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as f:
            return json.load(f)
    return []

# Guardar las notas en el archivo JSON
def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

@app.route('/add_note', methods=['POST'])
def add_note():
    content = request.form['content']
    notes = load_notes()
    note_id = len(notes) + 1
    new_note = {'id': note_id, 'content': content}
    notes.append(new_note)
    save_notes(notes)
    return jsonify({"message": "Nota publicada con éxito!"}), 200

# Exportar la aplicación para Netlify
handler = serverless.handler
