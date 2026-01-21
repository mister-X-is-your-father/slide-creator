#!/usr/bin/env python3
"""
Google OAuth 2.0 authentication for Google Slides API
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/presentations']

def authenticate(credentials_file='credentials.json', token_dir='~/.slide-creator'):
    """
    Authenticate with Google OAuth 2.0

    Args:
        credentials_file: Path to credentials.json from Google Cloud Console
        token_dir: Directory to store token.pickle

    Returns:
        Google credentials object
    """
    creds = None
    token_dir = os.path.expanduser(token_dir)
    token_file = os.path.join(token_dir, 'token.pickle')

    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_file):
                raise FileNotFoundError(
                    f"❌ Error: {credentials_file} が見つかりません\n"
                    "Google Cloud Console から OAuth 2.0 クライアント ID をダウンロードしてください"
                )
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=8080, open_browser=False)

        os.makedirs(token_dir, exist_ok=True)
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
        os.chmod(token_file, 0o600)

    return creds
