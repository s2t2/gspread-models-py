
#from abc import abstractmethod
from typing import List, Dict
from functools import lru_cache #,cached_property
from datetime import datetime

from gspread import Worksheet #, Spreadsheet
#from gspread_models.service import SpreadsheetService


class BaseModel:

    SHEET_NAME = None # abstract constant (str) to be set in child class

    COLUMNS = [] # abstract constant to be set in child class

    SEEDS = [] # abstract constant to be set in child class

    service = None # SpreadsheetService()

    def __init__(self, attrs:Dict):
        """
        Need to set service afterwards to bind the base model (and models which inherit from it) to a given sheet.

            service = SpreadsheetService() # opportunity to pass custom credentials and designate the sheet
            BaseModel.service = service
        """
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

    #
    # INSTANCE METHODS
    #

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

    #
    # CLASS METHODS
    #

    @classmethod
    def set_document_id(cls, document_id):
        cls.service.document_id = document_id

    @classmethod
    def get_sheet(cls) -> Worksheet:
       print(f"GET SHEET ('{cls.SHEET_NAME}')...")
       return cls.service.get_sheet(sheet_name=cls.SHEET_NAME)

    # using @property + @lru_cache because @cached_property throws:
    # ... TypeError: Cannot use cached_property instance without calling __set_name__ on it.
    @classmethod
    @property
    @lru_cache(maxsize=None)
    def sheet(cls) -> Worksheet:
        """Caches the sheet to avoid unnecessary API requests."""
        return cls.get_sheet()

    # ... API

    @classmethod
    def find(cls, by_id):
        """Fetches a record by its unique identifier."""
        records = cls.sheet.get_all_records()
        for record in records:
            if record.get("id") == by_id:
                return cls(record)
        return None

    @classmethod
    def all(cls):
        """Fetches all records from a given sheet."""
        records = cls.sheet.get_all_records()
        return [cls(record) for record in records]

    @classmethod
    def destroy_all(cls):
        """Removes all records from a given sheet, except the header row."""
        records = cls.sheet.get_all_records()
        # start on the second row, and delete one more than the number of records (to account for header row)
        return cls.sheet.delete_rows(start_index=2, end_index=len(records)+1)

    @classmethod
    def where(cls, **kwargs):
        """Filter records which match all provided values."""
        records = cls.sheet.get_all_records()
        objs = []
        for attrs in records:
            obj = cls(attrs)

            match_all = all(getattr(obj, k) == v for k, v in kwargs.items())

            if match_all:
                objs.append(obj)

        return objs

    @classmethod
    def create_all(cls, new_records:List[Dict], records=[]):
        """Appends new records (list of dictionaries) to the sheet.
            Adds auto-incrementing unique identifiers, and timestamp columns.
        """
        records = records or cls.all()

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

            inst = cls(attrs)
            rows.append(inst.row)
            next_id += 1

        return cls.sheet.append_rows(rows)

    @classmethod
    def create(cls, new_record:dict):
        """Appends new records (list of dictionaries) to the sheet.
            Adds auto-incrementing unique identifiers, and timestamp columns.
        """
        return cls.create_all([new_record])

    @classmethod
    def seed(cls):
        return cls.create_all(new_records=cls.SEEDS)
