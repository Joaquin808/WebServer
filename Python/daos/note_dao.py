from database import db
import requests
import re
import os.path
from pathlib import Path


class NoteDAO:

    # def create_note(self, note):
    #     sql = "INSERT INTO notes VALUES(%s, %s) RETURNING *"
    #     cursor = db.connection.cursor()
    #     cursor.execute(sql, (note.id, note.text))
    #     returned_note = cursor.fetchone()
    #
    #     return returned_note
    #
    # def view_note(self, id):
    #     sql = "SELECT * FROM notes WHERE id = %s"
    #     cursor = db.connection.cursor()
    #     cursor.execute(sql, [id])
    #     returned_note = cursor.fetchone()
    #
    #     return returned_note
    
    # Note location for all of my notes on the raspberry pi
    note_file_path = "/media/pi/notes"

    @classmethod
    def make_note(cls, url, note_name, note_content):
        # Where all of my notes are being saved on my desktop computer
        file_path = "G:/WebServer/Python/Notes"
        # Combines the directory and file name in order to download to save
        # to the correct location
        complete_file = os.path.join(cls.note_file_path, note_name + ".txt")
        # Opens the directory and file in order to edit it
        file = open(complete_file, 'w')
        # Writes the content to the file to save
        file.write(note_content)
        file.close()

        return note_content

    @classmethod
    def get_all_notes(cls):
        txt_folder = Path(cls.note_file_path).rglob('*.txt')
        files = [x for x in txt_folder]
        print(files)
        # for name in files:
        #     f = open(name, 'r')
        #     content = f.readlines()
        #     print(f'Content of %s:\n %s' %(name, content))
        content = {}
        for name in files:
            try:
                f = open(name, 'r')
                name = name.stem
                content[name] = f.readlines()[0]
                f.close()
            except Exception as e:
                print(e)

        print(content)
        return content

    @classmethod
    def update_note(cls, note_name, note_content):
        txt_folder = Path(cls.note_file_path).rglob('*.txt')


if __name__ == '__main__':
    NoteDAO.get_all_notes()
