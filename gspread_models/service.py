

import os
from typing import List
from functools import cached_property

from dotenv import load_dotenv
from gspread import service_account, Worksheet
from gspread.exceptions import WorksheetNotFound #, SpreadsheetNotFound

from gspread_models.date_parser import DateParser

load_dotenv()

DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)
GOOGLE_SHEETS_DOCUMENT_ID = os.getenv("GOOGLE_SHEETS_DOCUMENT_ID", default="OOPS, Please get the spreadsheet identifier from its URL, and set the 'GOOGLE_SHEETS_DOCUMENT_ID' environment variable accordingly...")

class SpreadsheetService(DateParser):

    def __init__(self, credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH, document_id=GOOGLE_SHEETS_DOCUMENT_ID):
        self.client = service_account(filename=credentials_filepath)
        self.document_id = document_id

        print("SPREADSHEET SERVICE...")
        print("DOCUMENT ID:", self.document_id)

    @cached_property
    def doc(self):
        """Get the given document. NOTE: this will make an API call."""
        return self.client.open_by_key(self.document_id) #> <class 'gspread.models.Spreadsheet'>

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

    # RECORDS

    #def write_to_sheet(self, sheet_name, records):
    #    sheet = self.doc.worksheet(sheet_name)
    #    #records = sheet.get_all_records()
    #
    #    breakpoint()
    #
    #    #values = [record.values() for record in records]
    #    sheet.append_rows(values=records)

    #def get_records(self, sheet_name):
    #    """Gets all records from a given sheet,
    #        converts datetime columns back to Python datetime objects.
    #    """
    #    #print(f"GETTING RECORDS FROM SHEET: '{sheet_name}'")
    #    sheet = self.get_sheet(sheet_name) #> <class 'gspread.models.Worksheet'>
    #    records = sheet.get_all_records() #> <class 'list'>
    #
    #    # todo: if any columns are datetime related
    #    for record in records:
    #        if record.get("created_at"):
    #            record["created_at"] = self.parse_timestamp(record["created_at"])
    #    return sheet, records

    # DELETING DATA

    #def destroy_all(self, sheet_name):
    #    """Removes all records from a given sheet, except the header row."""
    #    sheet, records = self.get_records(sheet_name)
    #    # start on the second row, and delete one more than the number of records,
    #    # ... to account for the header row
    #    sheet.delete_rows(start_index=2, end_index=len(records)+1)

    #def get_products(self):
    #    _, products = self.get_records("products")
    #    return products
    #
    #def get_orders(self):
    #    _, orders = self.get_records("orders")
    #    return records
    #
    #def get_user_orders(self, user_email):
    #    _, orders = self.get_records("orders")
    #    return [order for order in orders if order["user_email"] == user_email]


    # WRITING DATA
    #
    # FYI: we could consider implementing a locking mechanism on sheet writes, to prevent overwriting (if it becomes an issue)
    # ... however we know that if we want a more serious database solution, we would choose SQL database (and this app is just a small scale demo)

    #def write_data_to_sheet(df, sheet):
    #    header_row = df.columns.tolist()
    #
    #    rows = df.values.tolist()
    #    assert len(header_row) == len(rows[0]) # same number of columns in all rows
    #
    #    all_rows = [header_row] + rows
    #
    #    sheet.clear()
    #
    #    sheet.update(all_rows)


    #def seed_products(self):
    #    sheet, products = self.get_records("products")
    #    if not any(products):
    #        DEFAULT_PRODUCTS = [
    #            {'id': 1, 'name': 'Strawberries', 'description': 'Juicy organic strawberries.', 'price': 4.99, 'url': 'https://picsum.photos/id/1080/360/200'},
    #            {'id': 2, 'name': 'Cup of Tea', 'description': 'An individually-prepared tea or coffee of choice.', 'price': 3.49, 'url': 'https://picsum.photos/id/225/360/200'},
    #            {'id': 3, 'name': 'Textbook', 'description': 'It has all the answers.', 'price': 129.99, 'url': 'https://picsum.photos/id/24/360/200'}
    #        ]
    #        self.create_products(DEFAULT_PRODUCTS)

    #def create_products(self, new_products:list):
    #    self.create_records("products", new_products)
    #
    #def create_product(self, new_product:dict):
    #    self.create_records("products", [new_product])
    #
    #def create_orders(self, new_orders:list):
    #    self.create_records("orders", new_orders)
    #
    #def create_order(self, new_order:dict):
    #    self.create_records("orders", [new_order])



    #def create_records(self, sheet_name:str, new_records:list):
    #    model_class = {"products": Product, "orders": Order}[sheet_name]
    #
    #    sheet, records = self.get_records(sheet_name)
    #    next_row_number = len(records) + 2 # plus headers plus one
    #
    #    # auto-increment integer identifier
    #    if any(records):
    #        existing_ids = [r["id"] for r in records]
    #        next_id = max(existing_ids) + 1
    #    else:
    #        next_id = 1
    #
    #    new_rows = []
    #    for new_record in new_records:
    #        new_record["id"] = next_id
    #        new_record["created_at"] = self.generate_timestamp()
    #        new_row = model_class(new_record).to_row
    #        new_rows.append(new_row)
    #
    #        next_id += 1
    #
    #    sheet.insert_rows(new_rows, row=next_row_number)






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
