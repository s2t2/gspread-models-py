


# Pandas Support

With a goal of minimizing dependencies, the `gspread-models` package does not currently provide native pandas support. However it is very easy to implement, by following the guide below.

## Formatting Records as DataFrame

FYI: It is easy to construct a pandas DataFrame containing the information fetched from the sheet, by converting the records to a list of dictionaries:

```py
from pandas import DataFrame

# fetch all records:
books = Book.all()

# convert to dataframe:
books_df = DataFrame([dict(book) for book in books])
books_df.head()

#> id title                   author              year  created_at
#> 1  To Kill a Mockingbird   Harper Lee          1960  2024-05-22 21:36:25.582605+00:00
#> 2  1984                    George Orwell       1949  2024-05-22 21:36:25.582738+00:00
#> 3  The Great Gatsby        F. Scott Fitzgerald 1925  2024-05-22 21:36:25.582778+00:00
#> 4  The Catcher in the Rye  J.D. Salinger       1951  2024-05-22 21:36:25.582813+00:00
#> 5  Pride and Prejudice     Jane Austen         1813  2024-05-22 21:36:25.582846+00:00
```

## Customizing the Base Model

It is possible to leverage inheritence to customize the behaviors of the base model, for example to create a method which returns all records in DataFrame format:

```py
from gspread_models.base import BaseModel
from pandas import DataFrame

class MyBaseModel(BaseModel):

    @classmethod
    def records_to_df(cls):
        objects = cls.all()
        df = DataFrame([dict(obj) for obj in objects])
        df.index = df["id"]
        return df


MyBaseModel.bind(credentials_filepath="...", document_id="...")
```

This way, the child class(es) can have DataFrame support by default:

```py

class MyBook(MyBaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year"]
```

```py
books_df = MyBook.records_to_df()
books_df.head()

#> id title                   author              year  created_at
#> 1  To Kill a Mockingbird   Harper Lee          1960  2024-05-22 21:36:25.582605+00:00
#> 2  1984                    George Orwell       1949  2024-05-22 21:36:25.582738+00:00
#> 3  The Great Gatsby        F. Scott Fitzgerald 1925  2024-05-22 21:36:25.582778+00:00
#> 4  The Catcher in the Rye  J.D. Salinger       1951  2024-05-22 21:36:25.582813+00:00
#> 5  Pride and Prejudice     Jane Austen         1813  2024-05-22 21:36:25.582846+00:00
```
