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
    description="Model based ORM interface into Google Sheets. Read and write data to and from Google Sheets using a high-level class-based interface. This package is built on top of the awesome `gspread` package.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/gspread-models-py",
    keywords="google sheets gspread models orm spreadsheet google-sheets google-sheets-api gspread-models gspread_models",
    install_requires=["python-dotenv", "gspread>=6.0.2"],  # install_requires
    packages=["gspread_models"], # find_packages()
)
