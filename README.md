# gspread-models-py

Model based ORM interface into Google Sheets, using the `gspread` package.

## Installation

Install this package from PyPI:

```sh
pip install gspread_models
```

## Setup

Follow the [Google Cloud Setup Guide](/docs/GOOGLE_CLOUD.md) to setup a Google Cloud project with a service account access to the Google Sheets API, obtain a service account credentials JSON file. Note the path to this file (i.e. the `credentials_filepath`).

Follow the [Google Sheets Setup Guide](/docs/GOOGLE_SHEETS.md) to setup a Google Sheet document and share editor access with your service account. Note the identifier of this document (i.e. the `document_id`).

## Quick Start

**Step 1:** Bind the base model to your spreadsheet document and your credentials:

```py
from gspread_models.base import BaseModel

BaseModel.service = SpreadsheetService(
  document_id="your-document-id",
  credentials_filepath="/path/to/google-credentials.json"
)
```

**Step 2:** Define your own light-weight class that inherits from the base model. For example this `Product` class:

```python
from gspread_models.service import SpreadsheetService

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

```

**Step 3:** Setup a corresponding sheet for this model. The `Product` class example above assumes your document has a sheet called "products", with an initial row of column headers: `id`, `name`, `description`, `price`, `url`, and `created_at` (in this specific order).

> NOTE: The metadata columns `id` and `created_at` are included in the sheet (as the first, and last, columns respectively), but they are not listed in the model-specific `COLUMNS` because they are managed automatically by the base model.


## Usage Examples

Here are additional usage examples:

  + Local Development: Books Example ([model class](/test/models/book.py) and [tests](test/models_test.py))

  + Google Colab Notebook: [Demo Notebook](/notebooks/gspread_models_package_demo_v102.py)

  + Web Application: [Flask Sheets Template](https://github.com/prof-rossetti/flask-sheets-template-2024)

### Authentication

To authenticate to Google APIs, when creating a new instance of the `SpreadsheetService`, you can use either a local credentials JSON file, or a credentials object.

  + A) If using a local credentials JSON file, pass the string filepath as the `credentials_filepath` parameter. See the Quickstart Guide for an example of authenticating using the filepath option.
  + B) Otherwise if using a credentials (`google.auth.Credentials`) object, pass it as the `credentials` parameter. See the Demo Notebook for an example of authenticating in Google Colab using a credentials object.


## API

### Query Interface

The base model provides an intuitive query interface for any child class that inherits from it.

#### Creating Records

Creating and persisting new records:

```py
Product.create({"name": "Blueberries", "description":"Organic blues", "price":3.99})
```

```py
Product.create_all([{"name": "Product X"}, {"name": "Product Y"}])
```

FYI: If the model class defines a `SEEDS` variable as a list of dictionaries (see [`product.py`](/test/models/product.py) example), you can populate the sheet with these initial values:

```py
Product.seed()
```


#### Find All Records

Find all records from the sheet:

```py
Product.all()
```

#### Find Record

Find a record given its unique identifier:

```py
Product.find(1)
```

#### Filtering Records

Filter records based on class-specific attribute values (returns records that match ALL criteria):

```py
Product.where(name="Strawberries")

Product.where(name="Strawberries", price=1000)
```

#### Destroying Records

Clear the sheet by removing all records:

```py
Product.destroy_all()
```

This operation leaves the column headers intact.


## [Contributing](/.github/CONTRIBUTING.md)

## [License](/LICENSE)
