
from datetime import datetime
#from time import sleep

#import pytest

from gspread import Spreadsheet as Document, Worksheet
from gspread_models.service import GOOGLE_CREDENTIALS_FILEPATH
from gspread_models.base import BaseModel
#from pandas import DataFrame

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID #, TEST_SLEEP
from test.models.book import Book

#
# DOCUMENT BINDING
#

def assert_base_model_is_bound():
    service = BaseModel.service
    assert service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    assert isinstance(service.doc, Document)

    service = Book.service
    assert service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    assert isinstance(service.doc, Document)
    assert isinstance(Book.sheet, Worksheet)

def test_document_binding_with_creds_filepath():
    assert BaseModel.service == None
    assert Book.service == None
    BaseModel.bind(document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID, credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH)
    assert_base_model_is_bound()
    BaseModel.service = None

def test_document_binding_with_creds(creds):
    assert BaseModel.service == None
    assert Book.service == None
    BaseModel.bind(document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID, credentials=creds)
    assert_base_model_is_bound()
    BaseModel.service = None


#
# QUERY INTERFACE
#

def test_model_context_fixture(model_context):
    # model_context is using the test document:
    assert BaseModel.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    # including for child classes:
    assert Book.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

def test_child_model(model_context):
    # model context has already been configured to use the test document:
    assert Book.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    sheet = Book.sheet
    assert isinstance(sheet, Worksheet)
    assert sheet.title == "books"

    # DESTROY ALL:
    Book.destroy_all()

    # SEED RECORDS:
    Book.seed()

    # FIND ALL:
    books = Book.all()
    assert len(books) == 12

    # ... WITH DATAFRAME SUPPORT:
    #books_df = Book.all(as_df=True)
    #assert isinstance(books_df, DataFrame)
    #assert len(books_df) == 12
    #assert books_df.columns.tolist() == ["id", "title", "author", "year", "created_at"]

    # CREATE:

    Book.create(dict(title="My Book", author="Me", year=2024))

    # ... persists the record to sheet:
    books = Book.all()
    assert len(books) == 13
    assert books[-1].title == "My Book"

    # FIND:
    book = Book.find(3)
    assert book.id == 3
    assert book.title == "The Great Gatsby"
    assert book.year == 1925
    assert isinstance(book.created_at, datetime)
    #assert isinstance(book.updated_at, datetime)

    # FILTER BY:
    # returns as many items that match that criteria:
    books = Book.where(author="J.K. Rowling")
    assert len(books) == 2
    # returns only the items that match ALL conditions:
    books = Book.where(title="The Great Gatsby", year=2020)
    assert not any(books)

    # SAVE:
    # given a dictionary of compatible attributes:
    #new_book = Book(dict(title="My Book", author="Me", year=2024))
    #new_book.save()
    # ... or keyword args:
    #new_book = Book(title="Another Book", author="You", year=2024)
    #new_book.save()
    # ... BUT IT STILL WORKS WITH EXISTING OBJECTS FETCHED FROM THE SHEET:
    #existing_book = books[0]
    #existing_book.title = "Updated Title"
    #existing_book.save()
    #book = Book.find(title="Updated Title")
    #assert book.title == "Updated Title"
