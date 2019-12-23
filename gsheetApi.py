import pandas as pd
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import requests
import accounts

def gsheet_build_service(token_refresh=True):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token and token_refresh:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    service = build('sheets', 'v4', credentials=credentials)
    return service


def play_with_gsheet(spreadsheetId=None, _range=None, dataframe=None, method='read', first_time=True, service=None):
    """
    method: {'read', 'write', 'clear', 'append'}
    """
    
    if first_time:
        service = gsheet_build_service()

    if method == 'read':
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=_range).execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        df = df.iloc[1:].rename(columns=df.iloc[0])
        return df
    
    if method == 'write':
        values = [dataframe.columns.values.astype(str).tolist()] + dataframe.astype(str).values.tolist()
        data = [
        {
            'range': _range,
            'values': values
        }
        ]
        body = {
            'valueInputOption':'RAW',
            'data':data
        }
        
        service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()
            
    if method == 'clear':
        body = {
            'ranges':_range
        }
        
        service.spreadsheets().values().batchClear(spreadsheetId=spreadsheetId, body=body).execute()
            
    if method == 'append' and len(dataframe) > 0:
        body = {
            'values': dataframe.astype(str).values.tolist()
        }
        
        service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=_range,
                                                        valueInputOption='RAW', insertDataOption='INSERT_ROWS',
                                                        body=body).execute()