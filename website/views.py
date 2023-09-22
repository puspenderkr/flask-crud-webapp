from flask import Blueprint, render_template, request, flash, jsonify, abort, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user,)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    note = Note.query.get(task_id)

    if not note:
        abort(404)  # Task with the specified ID not found, return a 404 error.

    if note.user_id != current_user.id:
        abort(403)  # Unauthorized access, return a 403 error.

    return jsonify({
        'id': note.id,
        'data': note.data,
        'date': note.date.strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': note.user_id
    })

@views.route('/tasks/<int:task_id>/edit', methods=['GET'])
@login_required
def edit_task(task_id):
    note = Note.query.get(task_id)

    if not note:
        abort(404)  # Task with the specified ID not found, return a 404 error.

    if note.user_id != current_user.id:
        abort(403)  # Unauthorized access, return a 403 error.

    return render_template("edit.html", task=note, user=current_user)

@views.route('/tasks/<int:task_id>', methods=['PUT', 'POST'])
@login_required
def update_task(task_id):
    note = Note.query.get(task_id)

    if not note:
        abort(404)  # Task with the specified ID not found, return a 404 error.

    if note.user_id != current_user.id:
        abort(403)  # Unauthorized access, return a 403 error.

    if request.method == 'POST':
        new_data = request.form.get('data')

        if not new_data:
            flash('Data is required for the update.', category='error')
        else:
            note.data = new_data
            db.session.commit()
            flash('Task updated successfully!', category='success')

    return redirect(url_for('views.home'))
