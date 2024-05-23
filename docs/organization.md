
# Project Organization

If you are developing locally and would like to split up all models into their own files, you are recommended to adopt an approach similar to the following, where all models inherit from the base model after it has been configured.

## Project Structure

Example project file structure:

```
- my_project/
  - db.py
  - models/
    - order.py
    - product.py
```

## File Contents

Example \"db.py" file contents:

```py
# this is the "my_project/db.py" file...

from gspread_models.base import BaseModel

BaseModel.bind(
    credentials_filepath="/path/to/google-credentials.json",
    document_id="your-document-id"
)

# now you can import the base model from here,
# ... and child model classes will use the configured document and credentials
```

Example \"product.py" file contents:

```py
# this is the "my_project/models/product.py" file...

from my_project.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "image_url"]
```

Example \"order.py" file contents:

```py
# this is the "my_project/models/order.py" file...

from my_project.db import BaseModel

class Order(BaseModel):

    SHEET_NAME = "orders"

    COLUMNS = ["customer_email", "product_id", "unit_price", "quantity"]
```

See the [Flask Sheets Template](https://github.com/prof-rossetti/flask-sheets-template-2024/tree/main/app) for an example implementation of models split across multiple files.
