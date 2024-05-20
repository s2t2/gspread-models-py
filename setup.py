# setup.py

from setuptools import setup

from gspread_models import VERSION

# FYI: PyPI doesn't display the links in this markdown
# https://stackoverflow.com/a/26737672/670433
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gspread_models",
    version=VERSION,
    author="Michael Rossetti",
    author_email="datacreativellc@gmail.com",
    description="An Object Relational Mapper (ORM) for the Google Sheets API. Provides a straightforward and intuitive model-based query interface, making it easy to interact with Google Sheets as if it were more like a database. Offers a fast and flexible way to get up and running with a Google Sheets database, for rapid prototyping and development in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/gspread-models-py",
    keywords="google sheets gspread models orm spreadsheet google-sheets google-sheets-api gspread-models gspread_models",
    install_requires=["python-dotenv", "gspread>=6.0.2"],  # install_requires
    packages=["gspread_models"], # find_packages()
)
