

from time import sleep
from gspread import Spreadsheet as Document, Worksheet
#import pytest

from gspread_models.service import SpreadsheetService #, GOOGLE_CREDENTIALS_FILEPATH

from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID, TEST_SLEEP


def test_document(service):
    assert isinstance(service.doc, Document)


def test_sheets(service):
    sheets = service.sheets
    assert isinstance(sheets, list)

    for sheet in sheets:
        assert isinstance(sheet, Worksheet)


def test_credentials(creds):
    # it works with google.auth.compute_engine.credentials.Credentials
    # using either parameter name (for flexibility)

    sleep(TEST_SLEEP)
    service = SpreadsheetService(creds=creds, document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID)
    assert isinstance(service.doc, Document)

    sleep(TEST_SLEEP)
    service = SpreadsheetService(credentials=creds, document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID)
    assert isinstance(service.doc, Document)
