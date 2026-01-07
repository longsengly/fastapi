from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI"}

# I create list book
books = [
    {"id": 1, "title": "Python Basics", "author": "Long Ti", "pages": 365},
    {"id": 2, "title": "Python Basics", "author": "Long Ti", "pages": 365},
    {"id": 3, "title": "Python Basics", "author": "Long Ti", "pages": 365}
]

# create class name Book
class Book(BaseModel):
    title: str
    author: str
    pages: int

# api for take book
@app.get("/books")
def get_books(limit: int | None = None):
    """Get all books, optionally limited by count."""

    if limit:
        return {"books": books[:limit]}
    return {"books": books}

# show id
@app.get("/book/{book_id}")
def get_book(book_id: int):
    """Get a specific book by ID."""
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def create_book(book: Book):
    """Create a new book entry."""
    new_book = {
        "id": len(books) +1, 
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }
    books.append(new_book)
    return new_book