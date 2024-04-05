## Google Cloud Setup

We will use the Google Cloud platform for user login purposes, and to interface with Google Sheets and other Google services.

After creating a project, we will configure an OAuth Client to handle user logins, and a Service Account to programmatically interface with Google Sheets and other services on our behalf.

### Project Setup

Visit the [Google Cloud Console](https://console.cloud.google.com). Create a new project, and name it. After it is created, select it, for example using the project selection dropdown menu.

### OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id". Before moving forward, we will be prompted to set up a consent screen.

Click to "Configure Consent Screen". Choose "external" by default, or consider "internal" if using your university-issued address and only members of your organization will be using the app. Give your app a name (users might see this when they log in). Leave the domain info blank for now, and leave the defaults / skip lots of the setup for now. If/when you deploy your app to a production server, you can return to populating this info (or you will be using a different "production" Google API project).

Return to the Credentials page and actually creating the "OAuth Client Id". Choose a "Web application" type, give it a name, and set the following "Authorized Redirect URIs" (for now, while the project is still in development):

  + http://localhost:5000/auth/google/callback
  + http://127.0.0.1:5000/auth/google/callback

After the client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`, and set them as environment variables (see configuration section below).

### Service Account Credentials

To fetch data from the Google Sheets database (and use other Google APIs), the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account, and give it "Editor" role access to your Google API project.

Find the service account you just created in the "Service Accounts" section of the Credentials page, and click on it. For the selected service account, visit the "Keys" menu to create a new JSON credentials file. Then download the resulting JSON key file into the root directory of this repo, and rename it to "google-credentials.json".


### Enabling APIs

In the Google APIs project console, from the "Enabled APIs and Services" page, search for and enable the "Google Sheets API".

If you would like to use additional APIs in the future (for example Google Calendar API for a calendar integration), you will need to come back and enable them sepearately in the future.
