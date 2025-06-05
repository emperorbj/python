from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "book_name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "ISBN": "978-0743273565"
    },
    {
        "book_name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "ISBN": "978-0446310789"
    },
    {
        "book_name": "1984",
        "author": "George Orwell",
        "ISBN": "978-0451524935"
    }
]
@app.get('/books')
def get_books():
    return {
        "data": books
    }

@app.get('/books/{name}')
def get_book_by_name(name):
    for book in books:
        if book["book_name"] == name:
            return {
                "data":book
            }
            
@app.post('/books')
def add_new_book(book:dict):
    books.append(book)
    return {
        "message":"book added successfully",
        "data":books
    }