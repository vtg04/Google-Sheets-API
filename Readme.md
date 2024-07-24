# Google Sheets API Automation

This project demonstrates how to use the Google Sheets API to automate reading and writing data in a Google Sheet using Python.

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Google-Sheets-API.git
```

### Navigate to the Project Directory

```bash
cd Google-Sheets-API
```

### Install Required Libraries

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Set Environment Variable
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account key:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-file.json
```

## Usage

### Read Data from Google Sheets
Run the Python script read.py to read data from your Google Sheet:

```bash
python read.py
```

### Write Data to Google Sheets
Run the script to write data:

```bash
python write.py
```
