from python.database import db
import requests
import re

class NoteDAO:

    def create_note(self, note):
        sql = "INSERT INTO notes VALUES(%s, %s) RETURNING *"
        cursor = db.create_connection().cursor()
        cursor.execute(sql, (note.id, note.text))
        returned_note = cursor.fetchone()

        return returned_note

    def view_note(self, id):
        sql = "SELECT * FROM notes WHERE id = %s"
        cursor = db.create_connection().cursor()
        cursor.execute(sql, [id])
        returned_note = cursor.fetchone()

        return returned_note

    def save_note(self, url, note_name, note_content):
        open(note_name, 'wb').write(note_content)

        return note_content
