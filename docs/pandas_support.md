


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

If you would like to integrate pandas DataFrame functionality into your child classes, you can leverage inheritence to overwrite the `all()` method of the base model, to optionally return data in DataFrame format:

```py

from pandas import DataFrame

class MyBaseModel(BaseModel):

    @classmethod
    def all(cls, as_df=False):
        """Fetches all records from a given sheet. Overwrites parent method to optionally use a dataframe approach.

            Params :

                as_df (bool) : whether or not to return the data as a DataFrame
        """
        records = cls.sheet.get_all_records()
        if as_df:
            df = DataFrame([dict(cls(record)) for record in records])
            df.index = df["id"]
            return df
        else:
            return [cls(record) for record in records]


MyBaseModel.service = service
```

```py
class MyBook(MyBaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year"]

```

```py
books_df = MyBook.all(as_df=True)
books_df.head()

#> id title                   author              year  created_at
#> 1  To Kill a Mockingbird   Harper Lee          1960  2024-05-22 21:36:25.582605+00:00
#> 2  1984                    George Orwell       1949  2024-05-22 21:36:25.582738+00:00
#> 3  The Great Gatsby        F. Scott Fitzgerald 1925  2024-05-22 21:36:25.582778+00:00
#> 4  The Catcher in the Rye  J.D. Salinger       1951  2024-05-22 21:36:25.582813+00:00
#> 5  Pride and Prejudice     Jane Austen         1813  2024-05-22 21:36:25.582846+00:00
```
