
## Google Sheets Database Setup

Ensure you have followed the [Google Cloud Setup](/docs/GOOGLE_CLOUD.md) guide, specifically that you have enabled the "Google Sheets API", and have downloaded the service account JSON file into the root directory of this repository and renamed it as "google-credentials.json".

### Document Setup

Create a new Google Sheet document.

The app will need read and write access to your document.

Modify the document's sharing settings to grant "Edit" privileges to the "client email" address specified in the Google API service account credentials JSON file (e.g. "`<my-serice>`@`<my-project>`.iam.gserviceaccount.com").
