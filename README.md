# gspread-models-py

Model based ORM interface into Google Sheets. Read and write data to and from Google Sheets using a high-level class-based interface. This package is built on top of the awesome `gspread` package.

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

When defining your class, specify a `SHEET_NAME` as well as a list of `COLUMNS` in the sheet.

**Step 3:** Setup a corresponding sheet for this model.

For the example above example above, create a sheet called "books", and specify an initial row of column headers: "id", "title", "author", "year", and "created_at" (in this specific order). In addition to the sheet-specific attributes of "title", "author", and "year", the base model will manage a unique identifier "id" (always the first column in the sheet) as well as a timestamp "created_at" (always the last column in the sheet).



## Query Interface

The base model provides an intuitive query interface for any child class that inherits from it.

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
    print(book.id, book.title, book.author)
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

Otherwise if using a credentials object (google.auth.Credentials), pass it as the `credentials` parameter:

```py
SpreadsheetService(credentials="...", document_id="...")
```

[See](https://nbviewer.org/github/s2t2/gspread-models-py/blob/main/notebooks/gspread_models_package_demo_v102.ipynb) the [Demo Notebook](/notebooks/gspread_models_package_demo_v102.ipynb) for an example of authenticating in Google Colab using a credentials object.


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

## [License](/LICENSE)
