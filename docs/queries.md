
# Query Interface

Classes that inherit from the base model will have access to an intuitive query interface.

## Creating Records

Creating and persisting a new record (i.e. writing data to the sheet):

```py
Book.create({"title": "My Book", "author": "Me", "year": 2050})
```

Creating multiple records at once:

```py
Book.create_all([
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
])
```

## Listing Records

Fetching all records from the sheet:

```py
books = Book.all()
print(len(books)) #> 13

for book in books:
    print(book.id, "|", book.title, "|", book.author)

#> 1 | My Book | Me
#> ...
#> 12 | Harry Potter and the Philosopher's Stone | J.K. Rowling
#> 13 | Harry Potter and the Chamber of Secrets | J.K. Rowling
```

## Finding a Record

Find a specific record, given its unique identifier:

```py
book = Book.find(4)

print(book.id) #> 4
print(book.title) #> "The Great Gatsby"
print(book.author) #> "F. Scott Fitzgerald"
print(book.year) #> 1925
print(book.created_at) #> datetime object
```

## Filtering Records

Filter records based on matching conditions (returns records that match ALL criteria):

```py
books = Book.where(author="J.K. Rowling")
print(len(books)) #> 2
```

```py
books = Book.where(title="The Great Gatsby", year=2020)
print(len(books)) #> 0
```

## Destroying Records

Clear the sheet by removing all records:

```py
Book.destroy_all()
```

This operation leaves the column headers intact.
