import os

# AAD App Details
CLIENT_ID = "ad0b2cd4-e976-4185-86f2-c7474a908528" # Application (client) ID of app registration
CLIENT_SECRET = os.environ["AAD_CLIENT_SECRET"]

# Single-tenant accounts supported only
AUTHORITY = "https://login.microsoftonline.com/041d21aa-b4ab-4ad1-891d-62207b3367ef"

# Redirect URI should be the same between this and AAD App Registration
REDIRECT_PATH = "/auth"

# Privileges scope
SCOPE = []

# Token cache storage
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = "/tmp"