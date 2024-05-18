# gspread-models-py

Model based ORM interface into Google Sheets, using the `gspread` package.

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

In addition to the book-specific attributes of "title", "author", and "year", the base model will manage a unique identifier "id" (always the first column in the sheet) as well as a timestamp "created_at" (always the last column in the sheet).

**Step 3:** Setup a corresponding sheet for this model.

For the example above example above, create a sheet called "books", and specify an initial row of column headers: "id", "title", "author", "year", and "created_at" (in this specific order).



## Query Interface

The base model provides an intuitive query interface for any child class that inherits from it.

### Creating Records

Creating and persisting a new record:

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

When creating a new instance of the `SpreadsheetService`, you can use either a local credentials JSON file, or a credentials object, to authenticate to Google APIs.

### A) Credentials Filepath

If using a service account credentials JSON file, pass the string filepath as the `credentials_filepath` parameter:

```py
SpreadsheetService(credentials_filepath="/path/to/google-credentials.json", document_id="...")
```

If you are new to using service accounts:

   + Follow the [Google Cloud Setup Guide](/docs/GOOGLE_CLOUD.md) to setup a Google Cloud project with a service account access to the Google Sheets API, obtain a service account credentials JSON file, and note the path to this file (i.e. the `credentials_filepath`).
  + Follow the [Google Sheets Setup Guide](/docs/GOOGLE_SHEETS.md) to setup a Google Sheet document and share editor access with your service account. Note the identifier of this document (i.e. the `document_id`).


### B) Credentials Object

Otherwise if using a credentials object, for example in Google Colab, pass it as the `credentials` parameter:

```py
from google.colab import auth
auth.authenticate_user()

from google.auth import default
creds, _ = default()
print(type(creds)) #> google.auth.Credentials

SpreadsheetService(credentials=creds, document_id="...")
```

See the Demo Notebook for an example of authenticating in Google Colab using a credentials object.


## Usage Examples

Here are additional usage examples:

  + Local Development: [`Book` class](/test/models/book.py) and [`Book` tests](test/models_test.py)

  + Notebook (Google Colab): [Demo Notebook](https://nbviewer.org/github/s2t2/gspread-models-py/blob/main/notebooks/gspread_models_package_demo_v102.ipynb)

  + Web Application (Flask): [Flask Sheets Template](https://github.com/prof-rossetti/flask-sheets-template-2024)


To add your own example(s) to this list, feel free to open a new issue or pull request.


## [Contributing](/.github/CONTRIBUTING.md)

## [License](/LICENSE)
