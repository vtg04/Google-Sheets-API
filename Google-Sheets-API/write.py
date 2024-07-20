#Authentication
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

# Writing Data
SPREADSHEET_ID = 'your-spreadsheet-id'
RANGE_NAME = 'Sheet1!A1:D10'

values = [
    ["Item", "Cost", "Stock"],
    ["Apple", "1.00", "100"],
    ["Banana", "0.50", "150"],
]

body = {
    'values': values
}

result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
    valueInputOption='RAW', body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))