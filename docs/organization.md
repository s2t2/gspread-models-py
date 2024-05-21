
# Model File Organization

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
