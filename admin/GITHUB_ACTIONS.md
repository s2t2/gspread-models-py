
# Continuous Integration with GitHub Actions

We are using GitHub Actions to handle Continuous Integration for this Python Application.

## Setup

Make another version of the test sheet document, to be used specifically for the CI server. Add the CI test document identifier as a repository secret called `GOOGLE_SHEETS_TEST_DOCUMENT_ID`.

## Builds

### Python Application

The "python-app.yml" [configuration file](/.github/workflows/python-app.yml) specifies what steps should take place during the CI build.

In GitHub repository settings, find the secrets and variables menu for "actions", and add a "New repository secret" called `GOOGLE_API_CREDENTIALS`, and paste the JSON content from the "google-credentials.json" file. Make sure there isn't an extra space or new line at the end!
