from daos.note_dao import NoteDAO


class NoteService:
    dao_note = NoteDAO()

    @classmethod
    def make_note(cls, url, note_name, note_content):
        return cls.dao_note.make_note(url, note_name, note_content)

    @classmethod
    def get_all_notes(cls):
        return cls.dao_note.get_all_notes()