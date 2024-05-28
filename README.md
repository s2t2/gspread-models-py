# gspread-models

[![Maintainability](https://api.codeclimate.com/v1/badges/b15f7f0acee92c24a7bc/maintainability)](https://codeclimate.com/github/s2t2/gspread-models-py/maintainability) ![continuous integration](https://github.com/s2t2/gspread-models-py/actions/workflows/python-app.yml/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


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

Install the package from PyPI:

```sh
pip install gspread_models
```

## Quick Start

### Setup

**Step 1:** Bind the base model to your Google Sheets document and your credentials (see [Authentication](./docs/authentication.md) for more details):

```py
from gspread_models.base import BaseModel

BaseModel.bind(
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

To support the example above, create a sheet called "books", and specify an initial row of column headers: "id", "title", "author", "year", and "created_at".

> NOTE: In addition to the sheet-specific attributes ("title", "author", and "year"), the base model will manage metadata columns, including a unique identifier ("id") as well as a timestamp ("created_at").

### Usage

Once you have your model class setup, you can utilize the [Query Interface](./queries.md), to read and write data to the sheet.

Writing / appending records to the sheet:

```py
Book.create_all([
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
])
```

Fetching all records from the sheet:

```py
books = Book.all()

for book in books:
    print(book.id, "|", book.title, "|", book.author)

#> 1 | To Kill a Mockingbird | Harper Lee
#> 2 | 1984 | George Orwell
#> 3 | The Great Gatsby | F. Scott Fitzgerald
#> 4 | The Catcher in the Rye | J.D. Salinger
#> 5 | Pride and Prejudice | Jane Austen
```

It is easy to create a pandas DataFrame from the returned objects by converting each to a dictionary:

```py
from pandas import DataFrame

books_df = DataFrame([dict(book) for book in books])
books_df.head()

#> id title                   author              year  created_at
#> 1  To Kill a Mockingbird   Harper Lee          1960  2024-05-22 21:36:25.582605+00:00
#> 2  1984                    George Orwell       1949  2024-05-22 21:36:25.582738+00:00
#> 3  The Great Gatsby        F. Scott Fitzgerald 1925  2024-05-22 21:36:25.582778+00:00
#> 4  The Catcher in the Rye  J.D. Salinger       1951  2024-05-22 21:36:25.582813+00:00
#> 5  Pride and Prejudice     Jane Austen         1813  2024-05-22 21:36:25.582846+00:00
```

For more details, see the usage documentation below:

  + [Query Interface](./docs/queries.md)
  + [Authentication](./docs/authentication.md)
  + [Project File Organization](./docs/organization.md)
  + [Pandas Support](./docs/pandas_support.md)

## Examples

Here are some examples that demonstrate the usage of `gspread-models` within a variety of contexts:

  + [Demo Notebook](./docs/notebooks/demo_v1_0_7.ipynb)
  + [Flask Sheets Web Application Template](https://github.com/prof-rossetti/flask-sheets-template-2024)

If you use the `gspread-models` package, you are encouraged to add your project to this list, by submitting a pull request or opening an issue.

## Contributing

Contributions welcome! Here are some reference guides to help you get started as a contributor or maintainer of this package:

  + [Contributor's Guide](./docs/CONTRIBUTING.md)
    + [Google Cloud Setup Guide](./docs/setup/google-cloud.md)
    + [Google Sheets Setup Guide](./docs/setup/google-sheets.md)
    + [GitHub Actions Setup Guide](./docs/setup/github-actions.md)

## Acknowlegements

This package is built on top of the awesome [`gspread`](https://github.com/burnash/gspread) package.

## [License](/LICENSE)
