

import os
#from datetime import datetime, timezone

from gspread import Spreadsheet as Document, Worksheet
from dotenv import load_dotenv
import pytest

load_dotenv()

CI_ENV = (os.getenv("CI", default="false") == "true")
CI_SKIP_MESSAGE = "taking a lighter touch to testing on the CI server, to reduce API usage and prevent rate limits"

@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_document(service):
    assert isinstance(service.doc, Document)

@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_sheets(service):
    sheets = service.sheets
    assert isinstance(sheets, list)

    for sheet in sheets:
        assert isinstance(sheet, Worksheet)
