
# Contributor's Guide

Contributions are welcome. Follow this guide if you would like to get setup as a project contributor or maintainer.

## Setup

### Services Setup

Follow the [Google Cloud Setup Guide](./setup/google-cloud.md) to setup a Google Cloud project with service account that has access to the Google Sheets API. Obtain a service account credentials JSON file, move it into the root directory of this repository, and rename it as "google-credentials.json" specifically.

Follow the [Google Sheets Setup Guide](./setup/google-sheets.md) to setup a Google Sheet document, update your document's sharing settings to share editor access with your service account, and note the identifier of this document (i.e. the `GOOGLE_SHEETS_DOCUMENT_ID`). Repeat this step to create a test document, and obtain its document identifier (i.e. `GOOGLE_SHEETS_TEST_DOCUMENT_ID`).

### Repo Setup

Clone the repository, and navigate to the root directory from the command line.

Setup and activate a new Anaconda virtual environment:

```sh
conda create -n gspread-models-env python=3.10
conda activate gspread-models-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

Create local ".env" file to configure environment variables:

```sh
# This is the ".env" file...

GOOGLE_SHEETS_DOCUMENT_ID="..."

GOOGLE_SHEETS_TEST_DOCUMENT_ID="..."
```

## Testing

Running tests locally:

```sh
pytest
```

For testing on CI (skips some requests):

```sh
CI=true pytest
```

## Pre-Release Testing


Installing from GitHub source:

```sh
pip install git+https://github.com/s2t2/gspread-models-py.git
```

Create a new notebook and install from GitHub source to verify everything works, before creating a release.

## Releasing

See the [GitHub Actions guide](./setup/github-actions.md) for information about the package deployment process.


## Documentation Site

Installing package requirements for documentation site:

```sh
pip install docs/requirements.txt
```

Checking links:

```sh
jupyter-book build docs/ --builder linkcheck
```

Building docs site (local preview):

```sh
jupyter-book build docs/ --builder html
```

Building pdf:

```sh
jupyter-book build docs/ --builder pdfhtml

jupyter-book build docs/ --builder pdflatex
```
