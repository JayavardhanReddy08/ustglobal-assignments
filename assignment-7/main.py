from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Bookstore API")
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]
class Book(BaseModel):
    id: int
    title: str
    author: str
class UpdateBook(BaseModel):
    title: str
    author: str
@app.get("/books")
def get_books():
    return books
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.post("/books")
def add_book(book: Book):
    for b in books:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book.dict())
    return book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: UpdateBook):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
