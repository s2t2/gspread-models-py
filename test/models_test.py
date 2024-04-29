



from datetime import datetime

#import pytest

from gspread import Worksheet
from gspread_models.base import BaseModel

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID #, CI_ENV, CI_SKIP_MESSAGE
from test.models.book import Book


#def test_document_binding():
#    test_doc_id = "testing123"
#    assert BaseModel.service.document_id != test_doc_id
#    assert Book.service.document_id != test_doc_id
#
#    BaseModel.set_document_id(test_doc_id)
#    assert BaseModel.service.document_id == test_doc_id
#    assert Book.service.document_id == test_doc_id



#@pytest.mark.skipif(CI_ENV, reason="Uses model context")
#def test_model_context_fixture(model_context):
#    # model_context is using the test document:
#    assert BaseModel.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
#    assert Book.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID



#@pytest.mark.skipif(CI_ENV, reason="Uses model context")
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

    # CREATE:
    # given a dictionary of compatible attributes:
    #new_book = Book(dict(title="My Book", author="Me", year=2024))
    #new_book.save()
    # ... or keyword args:
    #new_book = Book(title="Another Book", author="You", year=2024)
    #new_book.save()

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


#def test_123(model_context):
#
#
#    breakpoint()
