def NoteEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "desc":item["desc"],
        "Is_important":item["Is_important"]
    }

def NotesEntity(items) -> list:
    return {NoteEntity(item) for item in items}