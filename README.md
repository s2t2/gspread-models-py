# gspread-models-py

Model based ORM interface into Google Sheets, using the `gspread` package.

## Installation

Install this package from PyPI:

```sh
pip install gspread_models
```

## Setup

Follow the [Google Cloud Setup Guide](/admin/GOOGLE_CLOUD.md) to setup a Google Cloud project with a service account access to the Google Sheets API, obtain a service account credentials JSON file.

Follow the [Google Sheets Setup Guide](/admin/GOOGLE_SHEETS.md) to setup a Google Sheet document and share editor access with your service account.

## Usage Example

### Sheet Setup

To setup this example, create a sheet called "products", and populate the first row with the following column headers (including metadata columns):

  + `id`
  + `name`
  + `description`
  + `price`
  + `url`
  + `created_at`
  + `updated_at`

The column names and order must match the `COLUMS` defined in the model class (see below). The `id` column should be first, and the timestamps (`created_at` and `updated_at`) should be last.

### Model Class Definition

Define your own light-weight class that inherits from the base model:

```py
from gspread_models.base import BaseModel

# your custom model class, which inherits from BaseModel:
class Product(BaseModel):

    # the name of the sheet to use for this model class:
    SHEET_NAME = "products"

    # the model-specific columns (excluding metadata columns):
    COLUMNS = ["name", "description", "price", "url"]

```

In addition to the model-specific `COLUMNS` list, the base model will manage **metadata columns**, including:
  + an auto-incrementing integer (`id`), which acts as the record's unique identifier
  + auto-updating timestamps (`created_at` and `updated_at`)



### Query Interface

The base model provides an intuitive query interface.

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




#### Creating Records

If the model class defines `SEEDS` as a list of dictionaries (see [`product.py`](/test/models/product.py) example), you can populate the sheet with these initial values:

```py
Product.seed()
```

Creating and persisting new records:

```py
Product.create(name="Blueberries", price=3.99, description="organic blues")
```

```py
Product.create_all([{"name":"Product X"}, {"name":"Product Y"}])
```

#### Initializing and Saving Records

After initializing a new record (whether it has previously been persisted or not), invoking `.save()` persists that record to the sheet:

```py
product = Product(name="Blueberries", price=3.99, description="organic blues", url=None)
product.save()
```

#### Destroying Records

Clear the sheet by removing all records:

```py
Product.destroy_all()
```

## [Contributing](/CONTRIBUTING.md)

## [License](/LICENSE)
