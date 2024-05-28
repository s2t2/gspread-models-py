
#from gspread_models import VERSION
#
#def test_package_version():
#    assert isinstance(VERSION, str)



def test_direct_imports():
    from gspread_models import BaseModel, SpreadsheetService, DateParser
    assert True
