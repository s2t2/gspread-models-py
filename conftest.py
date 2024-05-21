
import pytest
import os
from time import sleep

from dotenv import load_dotenv

from gspread_models.service import SpreadsheetService
from gspread_models.base import BaseModel

load_dotenv()

# an example sheet, used for testing purposes:
GOOGLE_SHEETS_TEST_DOCUMENT_ID= os.getenv("GOOGLE_SHEETS_TEST_DOCUMENT_ID")

# number of seconds to sleep between tests (helps manage Google API rate limit):
TEST_SLEEP = int(os.getenv("TEST_SLEEP", default="3")) # maybe not necessary? / not used in model_context

# for skipping tests on CI:
CI_ENV = bool(os.getenv("CI", default="false").lower() == "true")
#CI_SKIP_MESSAGE = "taking a lighter touch to testing on the CI server, to reduce API usage and prevent rate limits"



@pytest.fixture()
def service():
    """Spreadsheet service connected to the test document. Sleeps to avoid rate limits."""
    ss = SpreadsheetService(document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID)
    assert ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    yield ss

    print("SLEEPING...")
    sleep(TEST_SLEEP)


@pytest.fixture()
def model_context(service):
    """Use this fixture and subsequent model calls will be made against the test database."""
    #BaseModel.set_document_id(GOOGLE_SHEETS_TEST_DOCUMENT_ID)
    BaseModel.service = service
    assert BaseModel.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    yield "Using test document!"

    #print("SLEEPING...")
    #sleep(TEST_SLEEP)
