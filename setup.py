# setup.py

from setuptools import setup #, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gspread_models",
    version="1.0",
    author="Michael Rossetti",
    author_email="datacreativellc@gmail.com",
    description="Model based ORM interface into Google Sheets, using the gspread package.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/gspread-models-py",
    keywords="google sheets gspread models orm spreadsheet",
    packages=["gspread_models"] # find_packages()
)
