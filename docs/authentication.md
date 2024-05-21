
# Authentication

When creating a new instance of the `SpreadsheetService`, in order to authenticate to Google APIs, you can use either a service account credentials JSON file, or a credentials object.

**A) Credentials Filepath**

If using a service account credentials JSON file, pass the string filepath as the `credentials_filepath` parameter:

```py
SpreadsheetService(credentials_filepath="...", document_id="...")
```

For more details about setting up service account credentials, see the following guides:

  + [Google Cloud Setup Guide](./setup/google-cloud.md)
  + [Google Sheets Setup Guide](./setup/google-sheets.md)

**B) Credentials Object**

Otherwise if using a credentials object (google.auth.Credentials), pass it as the `credentials` parameter:

```py
SpreadsheetService(credentials="...", document_id="...")
```

See the [Demo Notebook](https://colab.research.google.com/drive/19hMHayokPtpJkLgCsWXZLV3FsGF7gvU6?usp=sharing) for an example of authenticating in Google Colab using a credentials object.
