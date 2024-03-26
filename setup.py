# setup.py

from setuptools import setup #, find_packages

from gspread_models import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

# https://stackoverflow.com/a/53069528/670433
#with open("requirements.txt", "r") as f:
#    install_requires = f.read().splitlines() #> ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]

setup(
    name="gspread_models",
    version=VERSION,
    author="Michael Rossetti",
    author_email="datacreativellc@gmail.com",
    description="Model based ORM interface into Google Sheets, using the gspread package.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/gspread-models-py",
    keywords="google sheets gspread models orm spreadsheet",
    install_requires=["python-dotenv", "gspread>=6.0.2"],  # install_requires
    packages=["gspread_models"], # find_packages()
)
