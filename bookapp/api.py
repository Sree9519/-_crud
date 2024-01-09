from ninja import NinjaAPI,Schema,ModelSchema
from django.shortcuts import get_object_or_404
from typing import Optional

from .models import Book
api=NinjaAPI()
class BookSchema(ModelSchema):  # schema inherited from models
    class Meta:
        model=Book
        fields=['name','title','author','description']
#     creating new schema for get the details from user
class Booknewschema(Schema):
    name: str
    title: str
    author: str
    description: str

class Bookpatchschema(Schema): # created new schema for edit  didn't need full fields its optional
    name: Optional[str] =None
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None

@api.get("/books/{book_name}",response=BookSchema) # get the detail of one book
def book_detail(request, book_name: str):
        book = get_object_or_404(Book, name=book_name)
        return book
@api.get("/books/",response=list[BookSchema]) # list all books
def book_list(request):
    "This method list all the Books"
    return Book.objects.all()

# create book
@api.post("/books",response=BookSchema)
def create_book(request,payload:Booknewschema): # get  the details from user and add into the newschema
    book=Book.objects.create(**payload.dict())
    return book
# Delete the book
@api.delete("/books/{book_name}")
def delete_book(request,book_name:str):
    book = get_object_or_404(Book, name=book_name)
    book.delete()
    return {"sucess":True}
# update  the book
@api.patch("/books/{book_name}",response=BookSchema)
def edit_book(request,book_name:str,payload:Bookpatchschema): #  Used new schema for edit method
    book=get_object_or_404(Book,name=book_name)
    for attr,value in payload.dict(exclude_unset=True).items():
        setattr(book,attr,value)
        book.save()
    return book