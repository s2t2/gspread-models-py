# gspread-models


The [`gspread-models`](https://github.com/s2t2/gspread-models-py) package is an Object Relational Mapper (ORM) for the Google Sheets API. It provides a straightforward and intuitive model-based query interface, making it easy to interact with Google Sheets as if it were more like a database. This package offers a fast and flexible way to get up and running with a Google Sheets database, for rapid prototyping and development in Python.

Key Features:

 + **Read and Write Data:** Seamlessly read and write data to and from Google Sheets.
 + **Easy Setup:** Minimal schema requirements make it simple to get started.
 + **Intuitive Query Interface:** Familiar object-oriented query methods inspired by ActiveRecord (Ruby) and SQLAlchemy (Python).
 + **Auto-incrementing ID**: Automatically manages a primary key "id" column.
 + **Timestamps**: Automatically manages a "created_at" timestamp column.
 + **Datetime Handling**: Converts datetime columns to Python datetime objects for easier manipulation.
 + **Flexible Migrations**: Easily update the schema by modifying your Google Sheet and updating the corresponding list of columns.



## Installation

Install this package from PyPI:

```sh
pip install gspread_models
```


## Quick Start

**Step 1:** Bind the base model to your spreadsheet document and your credentials (see "Authentication" for more details):

```py
from gspread_models.base import BaseModel
from gspread_models.service import SpreadsheetService

BaseModel.service = SpreadsheetService(
    document_id="your-document-id",
    credentials_filepath="/path/to/google-credentials.json"
)
```

**Step 2:** Define your own light-weight class that inherits from the base model:

```python

class Book(BaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year"]

```

When defining your class, specify a `SHEET_NAME` as well as a list of sheet-specific `COLUMNS`.

**Step 3:** Setup a corresponding sheet for this model.

For the example above, create a sheet called "books", and specify an initial row of column headers: "id", "title", "author", "year", and "created_at".

> NOTE: In addition to the sheet-specific attributes ("title", "author", and "year"), the base model will manage metadata columns, including a unique identifier ("id") as well as a timestamp ("created_at").



## Query Interface

Classes that inherit from the base model will have access to an intuitive query interface.

### Creating Records

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

### Listing Records

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

### Finding a Record

Find a specific record, given its unique identifier:

```py
book = Book.find(4)

print(book.id) #> 4
print(book.title) #> "The Great Gatsby"
print(book.author) #> "F. Scott Fitzgerald"
print(book.year) #> 1925
print(book.created_at) #> datetime object
```

### Filtering Records

Filter records based on matching conditions (returns records that match ALL criteria):

```py
books = Book.where(author="J.K. Rowling")
print(len(books)) #> 2
```

```py
books = Book.where(title="The Great Gatsby", year=2020)
print(len(books)) #> 0
```

### Destroying Records

Clear the sheet by removing all records:

```py
Book.destroy_all()
```

This operation leaves the column headers intact.





## Authentication

When creating a new instance of the `SpreadsheetService`, in order to authenticate to Google APIs, you can use either a service account credentials JSON file, or a credentials object.

**A) Credentials Filepath**

If using a service account credentials JSON file, pass the string filepath as the `credentials_filepath` parameter:

```py
SpreadsheetService(credentials_filepath="...", document_id="...")
```

**B) Credentials Object**

Otherwise if using a credentials object (google.auth.Credentials), pass it as the `creds` parameter:

```py
SpreadsheetService(creds="...", document_id="...")
```

See the [Demo Notebook](/notebooks/gspread_models_package_demo_v102.ipynb) for an example of authenticating in Google Colab using a credentials object.


## Model File Organization

If you are developing locally and would like to split up all models into their own files, you are recommended to adopt an approach similar to the following, where all models inherit from the base model after it has been configured.

Project file structure:

```
- project_dir/
  - db.py
  - models/
    - order.py
    - product.py
```

File contents:

```py
# this is the "db.py" file...

from gspread_models.service import SpreadsheetService
from gspread_models.base import BaseModel

BaseModel.service = SpreadsheetService(
    credentials_filepath="/path/to/google-credentials.json",
    document_id="your-document-id"
)
```

```py
# this is the "models/product.py" file...

from project.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "image_url"]
```

```py
# this is the "models/order.py" file...

from project.db import BaseModel

class Order(BaseModel):

    SHEET_NAME = "orders"

    COLUMNS = ["customer_email", "product_id", "unit_price", "quantity"]
```

See the [Flask Sheets Template](https://github.com/prof-rossetti/flask-sheets-template-2024) for an example implementation of models split across multiple files.



## [Contributing](/.github/CONTRIBUTING.md)

Contributions welcome! Feel free to open an issue and/or submit a pull request.

## Acknowlegements

This package is built on top of the awesome [`gspread`](https://github.com/burnash/gspread) package.

## [License](/LICENSE)
