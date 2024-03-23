
# Continuous Integration with GitHub Actions

We are using GitHub Actions to handle Continuous Integration for this Python Application.

The "python-app.yml" [configuration file](/.github/workflows/python-app.yml) specifies what steps should take place during the CI build.



In GitHub repository settings, find the secrets and variables menu for "actions", and add a "New repository secret" called `GOOGLE_API_CREDENTIALS`, and paste the JSON content from the "google-credentials.json" file. Make sure there isn't an extra space or new line at the end!

Also add a repository secret called `GOOGLE_SHEETS_TEST_DOCUMENT_ID` and set it (see README).
