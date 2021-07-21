from Python.daos.note_dao import NoteDAO

class NoteService:

    note_dao = NoteDAO()

    def make_note(self, url, note_name, note_content):
        return note_dao.make_note(url, note_name, note_content)
