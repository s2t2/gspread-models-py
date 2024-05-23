# Google Cloud Setup

## Project Setup

Visit the [Google Cloud Console](https://console.cloud.google.com). Create a new project, and name it. After it is created, select it, for example using the project selection dropdown menu.

## Enabling APIs

In the Google APIs project console, from the "Enabled APIs and Services" page, search for and enable the "Google Sheets API".

## Service Account Credentials

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account, and give it "Editor" role access to your Google API project.

Find the service account you just created in the "Service Accounts" section of the Credentials page, and click on it. For the selected service account, visit the "Keys" menu to create a new JSON credentials file. Then download the resulting JSON key file. Note the path to the local file you downloaded, and use this `credentials_filepath` when initializing the `SpreadsheetService` or binding the `BaseModel`.
