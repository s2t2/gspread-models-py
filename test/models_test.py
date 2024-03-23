



from datetime import datetime

from gspread_models.base import BaseModel
from test.models.book import Book

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID

def test_document_binding():
    test_doc_id = "testing123"
    assert BaseModel.service.document_id != test_doc_id
    assert Book.service.document_id != test_doc_id

    BaseModel.set_document_id(test_doc_id)
    assert BaseModel.service.document_id == test_doc_id
    assert Book.service.document_id == test_doc_id

def test_model_context_fixture(model_context):
    # model_context is using the test document:
    assert BaseModel.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    assert Book.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID




def test_child_model(model_context):

    # DESTROY ALL:
    Book.destroy_all()

    # SEED RECORDS:
    Book.seed_records()

    # FIND ALL:
    books = Book.find_all()
    assert len(books) == 12

    # CREATE:
    # given a dictionary of compatible attributes:
    new_book = Book(dict(title="My Book", author="Me", year=2024))
    new_book.save()
    # ... persists the record to sheet:
    books = Book.find_all()
    assert len(books) == 13
    assert books[-1].title == "My Book"

    # FIND:
    book = Book.find(3)
    assert book.id == 3
    assert book.title == "The Great Gatsby"
    assert book.year == 1925
    assert isinstance(book.created_at, datetime)
    assert isinstance(book.updated_at, datetime)

    # FILTER BY:
    # returns as many items that match that criteria:
    books = Book.filter_by(author="J.K. Rowling")
    assert len(books) == 2
    # returns only the items that match ALL conditions:
    books = Book.filter_by(title="The Great Gatsby", year=2020)
    assert not any(books)
