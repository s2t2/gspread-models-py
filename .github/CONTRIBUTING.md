
# Contributor's Guide

## Setup

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
GOOGLE_SHEETS_DOCUMENT_ID="..."

GOOGLE_SHEETS_TEST_DOCUMENT_ID="..."
```

## Usage

## Testing

Running tests locally:

```sh
pytest
```

For testing on CI (skips some requests):

```sh
CI=true pytest
```
