
#from abc import abstractmethod
from typing import List, Dict
#from functools import cached_property
from datetime import datetime

from gspread_models.service import SpreadsheetService


class BaseModel:

    SHEET_NAME = None # abstract constant (str) to be set in child class

    COLUMNS = [] # abstract constant to be set in child class

    SEEDS = [] # abstract constant to be set in child class

    service = SpreadsheetService()

    def __init__(self, attrs:Dict):
        self.attrs = attrs

        # attributes common to all child models
        self.id = attrs.get("id")

        for col in self.COLUMNS:
            #setattr(self, col, self.attrs.get(col))
            val = self.attrs.get(col)
            #if val.startswith("20"):
            # convert datetime parsable string to datetime object, dynamically
            if self.service.validate_timestamp(val):
                val = self.service.parse_timestamp(val)
            setattr(self, col, val)

    # INSTANCE METHODS

    @property
    def created_at(self):
        """Wraps timestamp string from the sheet in a native datetime object."""
        return self.service.parse_timestamp(self.attrs.get("created_at"))

    #@property
    #def updated_at(self):
    #    """Wraps timestamp string from the sheet in a native datetime object."""
    #    return self.service.parse_timestamp(self.attrs.get("updated_at"))

    def __iter__(self):
        """Enables dictionary conversion by passing an object instance into the dict() function."""
        yield 'id', self.id
        for col in self.COLUMNS:
            yield col, getattr(self, col)
        yield 'created_at', self.created_at
        #yield 'updated_at', self.updated_at

    @property
    def row(self) -> List:
        """Returns an ordered list of JSON serializable values, for writing to the sheet."""
        values = []
        values.append(self.id)
        for col in self.COLUMNS:
            val = getattr(self, col)
            if isinstance(val, datetime):
                val = str(val)
            values.append(val)
        values.append(str(self.created_at))
        #values.append(str(self.updated_at))
        return values

    def save(self):
        print("SAVING RECORD TO SHEET:")
        print(dict(self))
        #if self.id:
        #    self.attrs["updated_at"] = self.service.generate_timestamp()
        #    self.update(dict(self))
        #return self.create(dict(self))
        return self.create_all([dict(self)])


    # CLASS METHODS

    @classmethod
    def set_document_id(cls, document_id):
        cls.service.document_id = document_id

    @classmethod
    def get_sheet(cls):
       print(f"SHEET ('{cls.SHEET_NAME}')...")
       return cls.service.get_sheet(sheet_name=cls.SHEET_NAME)



    # API

    @classmethod
    def find(cls, by_id, sheet=None):
        """Fetches a record by its unique identifier."""
        sheet = sheet or cls.get_sheet() # assumes sheet exists, with the proper headers!
        records = sheet.get_all_records()
        for record in records:
            if record.get("id") == by_id:
                return cls(record)
        return None

    @classmethod
    def all(cls, sheet=None):
        """Fetches all records from a given sheet."""
        sheet = sheet or cls.get_sheet() # assumes sheet exists, with the proper headers!
        records = sheet.get_all_records()
        return [cls(record) for record in records]

    @classmethod
    def destroy_all(cls, sheet=None):
        """Removes all records from a given sheet, except the header row."""
        sheet = sheet or cls.get_sheet()
        records = sheet.get_all_records()
        # start on the second row, and delete one more than the number of records (to account for header row)
        return sheet.delete_rows(start_index=2, end_index=len(records)+1)

    @classmethod
    def where(cls, **kwargs):
        """Filter records which match all provided values."""
        #sheet = sheet or cls.get_sheet() # assumes sheet exists, with the proper headers!
        sheet = cls.get_sheet()
        records = sheet.get_all_records()
        objs = []
        for attrs in records:
            obj = cls(attrs)

            #for k,v in kwargs.items():
            #    if getattr(obj, k) == v:
            #        objs.append(obj)

            #match_all_conditions = all(dict(obj).get(k) == v for k, v in kwargs.items())
            match_all = all(getattr(obj, k) == v for k, v in kwargs.items())

            if match_all:
                objs.append(obj)

        return objs

    @classmethod
    def create_all(cls, new_records:List[Dict], records=[]):
        """Appends new records (list of dictionaries) to the sheet.
            Adds auto-incrementing unique identifiers, and timestamp columns.
        """
        sheet = cls.get_sheet() # assumes sheet exists, with the proper headers!

        records = records or cls.all(sheet=sheet)
        #next_row_number = len(records) + 2 # plus headers plus one

        # auto-increment integer identifier:
        if any(records):
            existing_ids = [r.id for r in records]
            next_id = max(existing_ids) + 1
        else:
            next_id = 1

        rows = []
        for attrs in new_records:
            attrs["id"] = next_id
            now = cls.service.generate_timestamp()
            attrs["created_at"] = now
            #attrs["updated_at"] = now

            inst = cls(attrs)
            rows.append(inst.row)
            next_id += 1

        #return sheet.insert_rows(rows, row=next_row_number)
        return sheet.append_rows(rows)

    @classmethod
    def create(cls, new_record:dict):
        """Appends new records (list of dictionaries) to the sheet.
            Adds auto-incrementing unique identifiers, and timestamp columns.
        """
        return cls.create_all([new_record])

    @classmethod
    def seed(cls):
        return cls.create_all(new_records=cls.SEEDS)
