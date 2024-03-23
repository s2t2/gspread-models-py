
from gspread_models import VERSION

def test_package_version():
    assert isinstance(VERSION, str)
