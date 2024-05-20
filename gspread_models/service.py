

import os
from typing import List
from functools import cached_property

from dotenv import load_dotenv
from gspread import service_account, authorize, Worksheet, Spreadsheet
from gspread.exceptions import WorksheetNotFound #, SpreadsheetNotFound

from gspread_models.date_parser import DateParser

load_dotenv()

DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)
GOOGLE_SHEETS_DOCUMENT_ID = os.getenv("GOOGLE_SHEETS_DOCUMENT_ID", default="OOPS, Please get the spreadsheet identifier from its URL, and set the 'GOOGLE_SHEETS_DOCUMENT_ID' environment variable accordingly...")

class SpreadsheetService(DateParser):

    def __init__(self, credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH, document_id=GOOGLE_SHEETS_DOCUMENT_ID, creds=None):
        """Params:
            Optionally pass creds (google.auth.compute_engine.credentials.Credentials) for example for use in colab notebook:

                    from google.colab import auth
                    from google.auth import default

                    auth.authenticate_user()
                    creds, _ = default()

                    service = SpreadsheetService(creds=creds)
        """
        if creds:
            self.client = authorize(creds)
        else:
            self.client = service_account(filename=credentials_filepath)

        self.document_id = document_id

        print("SPREADSHEET SERVICE...")
        print("DOCUMENT ID:", self.document_id)

    @cached_property
    def doc(self) -> Spreadsheet:
        """Get the given document."""
        return self.client.open_by_key(self.document_id)

    @property
    def sheets(self) -> List[Worksheet]:
        """List all sheets in the given document."""
        return self.doc.worksheets()

    def get_sheet(self, sheet_name) -> Worksheet:
        """Get a specific sheet in the document."""
        return self.doc.worksheet(sheet_name)

    def find_or_create_sheet(self, sheet_name) -> Worksheet:
        """access a sheet within the document, or create if not exists"""
        try:
            sheet = self.doc.worksheet(sheet_name)
            print(f"FOUND SHEET: '{sheet_name}'")
        except WorksheetNotFound:
            print(f"CREATING NEW SHEET ('{sheet_name}')...")
            sheet = self.doc.add_worksheet(title=sheet_name, rows="3", cols="3") # rows and cols are required. can be overwritten later?
            # consider adding columns based on self.COLUMNS
        return sheet




if __name__ == "__main__":

    from pprint import pprint


    ss = SpreadsheetService()

    print("SHEETS:")
    sheets = ss.sheets
    for sheet in sheets:
        #print(type(sheet)) #> <class 'gspread.worksheet.Worksheet'>
        print("...", sheet)

    sheet_name = input("Please choose a sheet name: ") or sheets[0].title
    print(sheet_name)

    #sheet, records = ss.get_records(sheet_name)
    sheet = ss.get_sheet(sheet_name)
    records = sheet.get_all_records()

    print("RECORDS:")
    print(len(records))
    for record in records:
        print("-----")
        pprint(record)
