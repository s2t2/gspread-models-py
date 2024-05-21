
# GitHub Actions Setup

We are using GitHub Actions for a variety of purposes, including continuous integration.

## Setup

Make another version of the test sheet document, to be used specifically for the CI server. Add the CI test document identifier as a repository secret called `GOOGLE_SHEETS_TEST_DOCUMENT_ID`.

## Workflows

### 1. Continuous Integration

The ["python-app.yml"](https://github.com/s2t2/gspread-models-py/blob/main/.github/workflows/python-app.yml) configuration file specifies what steps should take place during the CI build, including running automated tests to ensure the code is working as desired.

It requires the `GOOGLE_API_CREDENTIALS` repository secret. In GitHub repository settings, find the secrets and variables menu for "actions", and add a "New repository secret" called `GOOGLE_API_CREDENTIALS`, and paste the JSON content from the "google-credentials.json" file. Make sure there isn't an extra space or new line at the end!

### 2. Package Release

The ["python-publish.yml"](https://github.com/s2t2/gspread-models-py/blob/main/.github/workflows/python-publish.yml) configuration file triggers an update of the PyPI package when a new GitHub release is published.

#### PyPI API Key

To set this up, you need to obtain a PyPI access token and set it as a repository secret called `PYPI_API_TOKEN`. See:
  + https://pypi.org/help/#apitoken
  + https://pypi.org/manage/account/

We want to give the token project-level access only, so first create a project:
  + https://pypi.org/manage/account/publishing

Then when you generate the token, give it access to this project only.

### 3. Docs Site Deployment


The ["docs-deploy.yml"](https://github.com/s2t2/gspread-models-py/blob/main/.github/workflows/docs-deploy.yml) configuration file triggers an update of the documentation site hosted on GitHub pages.

To make it work for the first time, configure github pages deploy from github actions in the repository settings.
