from pydantic import BaseModel

class Note(BaseModel):
    title : str
    desc: str
    Is_important: bool