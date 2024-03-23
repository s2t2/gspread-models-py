# gspread-models-py

Model based interface into Google Sheets, using the `gspread` package.


## Installation

Install this package from PyPI:

```sh
pip install gspread_models
```

## Setup

Follow the [Google Cloud Setup Guide](/admin/GOOGLE_CLOUD.md) to setup a Google Cloud project with a service account access to the Google Sheets API, obtain a service account credentials JSON file.

Follow the [Google Sheets Setup Guide](/admin/GOOGLE_SHEETS.md) to setup a Google Sheet document and share editor access with your service account.

## Usage

### Sheet Setup

For this example, create a sheet called "products", and populate the first row with the following column headers:

  + `id`
  + `name`
  + `description`
  + `price`
  + `url`
  + `created_at`


### Model Class Definition

Define your own light-weight class that inherits from the base model:

```py
from gspread_models.base import BaseModel

class Product(BaseModel):

    # designates the name of the sheet to use for this model class
    SHEET_NAME = "products"

    # designates the model-specific columns
    COLUMNS = ["name", "description", "price", "url"]

```

> FYI: In addition to the model-specific column names defined in the class, the base model will add metadata fields, including: an auto-incrementing integer (`id`) as the record's unique identifier, as well as timestamps (`created_at` and `updated_at`).

> NOTE: the model-specific list of columns (`COLUMNS`) needs to exactly match the column names and column order already setup in the corresponding sheet. To clarify, `COLUMNS` should exclude the metadata columns.

### Query Interface

The base model provides intuitive model-based query interface.

#### Find All Records

Invoke `find_all()` to return all records from the sheet. This will wrap the records in your custom class, which converts any timestamp strings to datetime objects

```py
Product.find_all()
```

#### Find Record

Invoke `find()` to return a record given its unique identifier:

```py
Product.find(by_id=1)
```

#### Filtering Records

Filter records based on class-specific attribute values (returns records that match ALL criteria):

```py
Product.filter_by(name="Strawberries")

Product.filter_by(name="Strawberries", price=1000)
```

#### Creating Records

Creating new records:

```py
product_attrs = dict(name="Blueberries", price=3.99, description="organic blues", url=None)
Product.create(product_attrs)
```

#### Saving Records

After initializing a new record (whether it has previously been persisted or not), invoking `.save()` persists that record to the sheet:

```py
product_attrs = dict(name="Blueberries", price=3.99, description="organic blues", url=None)
product = Product(product_attrs)
product.save()
```

#### Seeding Records

If you add `SEEDS` (list of dictionaries) to your model class definition, `.seed_all()` will populate the sheet with these initial values:

```py
from gspread_models.base import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'Strawberries',
            'description': 'Juicy organic strawberries.',
            'price': 4.99,
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Cup of Tea',
            'description': 'An individually-prepared tea or coffee of choice.',
            'price': 3.49,
            'url': 'https://picsum.photos/id/225/360/200'
        },
        {
            'name': 'Textbook',
            'description': 'It has all the answers.',
            'price': 129.99,
            'url': 'https://picsum.photos/id/24/360/200'
        }
    ]
```

Populate the database with seeds:

```py
Product.seed_all()
```

## [Contributing](/CONTRIBUTING.md)

## [License](/LICENSE)
