

from gspread import Spreadsheet as Document, Worksheet
#import pytest

#from conftest import CI_ENV, CI_SKIP_MESSAGE

#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_document(service):
    assert isinstance(service.doc, Document)

#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_sheets(service):
    sheets = service.sheets
    assert isinstance(sheets, list)

    for sheet in sheets:
        assert isinstance(sheet, Worksheet)
