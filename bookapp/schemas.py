from ninja import Schema

class BookSchema(Schema):
    name:str
    title: str
    author: str
    description: str
