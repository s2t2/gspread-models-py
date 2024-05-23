
# Authentication

In order to authenticate to Google APIs, you can use either a service account credentials JSON file, or a credentials object.

When creating a new instance of the `SpreadsheetService`, or binding the `BaseModel` directly, you can pass either a `credentials_filepath` parameter, or a `credentials` parameter, based on your choice.

**A) Credentials Filepath**

If using a service account credentials JSON file, pass the string filepath as the `credentials_filepath` parameter:


```py
BaseModel.bind(credentials_filepath="...", document_id="...")
```

For more details about setting up service account credentials, see the following guides:

  + [Google Cloud Setup Guide](./setup/google-cloud.md)
  + [Google Sheets Setup Guide](./setup/google-sheets.md)

**B) Credentials Object**

Otherwise if using a credentials object (google.auth.Credentials), pass it as the `credentials` parameter:


```py
BaseModel.bind(credentials="...", document_id="...")
```

See the [Demo Notebook](./notebooks/demo_v1_0_6.ipynb) for an example of authenticating in Google Colab using a credentials object.
