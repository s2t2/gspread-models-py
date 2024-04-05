
## Google Sheets Database Setup

Ensure you have followed the [Google Cloud Setup](/admin/GOOGLE_CLOUD.md) guide, specifically that you have enabled the "Google Sheets API", and have downloaded the service account JSON file into the root directory of this repository and renamed it as "google-credentials.json".

### Document Setup

Create a new Google Sheet document. The app will need read and write access to this document.

Modify the document's sharing settings to grant "Edit" privileges to the "client email" address specified in the Google API credentials JSON file (e.g. "`<my-serice>`@`<my-project>`.iam.gserviceaccount.com").


### Model-specific Sheets Setup

On each sheet, add an initial row of header columns. The first column name should be `id`, followed by any model-specific column names, followed by `created_at`. The model interface will manage these additional metadata columns (`id`, and `created_at`) for you. The remaining model-specific columns should be listed as the `COLUMNS` in the corresponding model class (see README).
