
from gspread_models.base import BaseModel

class Book(BaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year"]

    SEEDS = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
        {"title": "To the Lighthouse", "author": "Virginia Woolf", "year": 1927},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
        {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
        {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "year": 1865},
        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997},
        {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "year": 1998},
    ]
