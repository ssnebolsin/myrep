import os

# Workspace Id in which the report is present
WORKSPACE_ID = 'cf15ff47-51df-47e3-ad21-6c5bbbb10c44'  #'7120f1ef-0fa8-4c5c-8a82-726a5923f294'
# Report Id for which Embed token needs to be generated
REPORT_ID = '329ee455-7c04-495c-a659-ca600f6d7ac4'  #'9c2a9cc9-0a0d-4095-a397-3223f9fb04fe' #'5d253c93-7cc3-4582-81a1-6031dad5141d'  # '1991081e-1e80-4005-9667-a4ccd477599b'

# Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
TENANT_ID = '041d21aa-b4ab-4ad1-891d-62207b3367ef'   #'9064dc66-330c-438e-aee3-1c9e605cc16d'

# Client Id (Application Id) of the AAD app
CLIENT_ID = 'ad0b2cd4-e976-4185-86f2-c7474a908528'  #'41470ce2-a5f8-4f20-82d0-e0f833297500'

# Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
# CLIENT_SECRET = os.environ["PBI_CLIENT_SECRET"]

# Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

# URL used for initiating authorization request
AUTHORITY = 'https://login.microsoftonline.com/organizations'

PAGE_NAME="ReportSection147c67b072172a437364"

REPORT_MAP = {
    "transport": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "d6ca6e10-9672-4864-8578-1ccda4a81d1b",
        "default_page_name": "ReportSection147c67b072172a437364"
    },
    "agro": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "329ee455-7c04-495c-a659-ca600f6d7ac4",
        "default_page_name": "ReportSection10db073908cebe1810ca"
    },
    "customerProfile": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "329ee455-7c04-495c-a659-ca600f6d7ac4",
        "default_page_name": "ReportSection"
    },
    "bank": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "329ee455-7c04-495c-a659-ca600f6d7ac4",
        "default_page_name": "ReportSectionf0ddb5614bc79e7785cf"
    },
    "sales": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "329ee455-7c04-495c-a659-ca600f6d7ac4",
        "default_page_name": "ReportSection92ca7de0704b1047010d"
    },
    "media": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "329ee455-7c04-495c-a659-ca600f6d7ac4",
        "default_page_name": "ReportSection98a34ed47cd40b3d0067"
    },
    "ats": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "97a4d913-ecc4-47ec-8395-8480b5147d9a",
        "default_page_name": "ReportSection6fab7f0cc354b07623e5"
    },
    "public_transport": {
        "workspace_id": "cf15ff47-51df-47e3-ad21-6c5bbbb10c44",
        "report_id": "6aa894e5-cbc0-4f7d-aa05-7353a8b0f122",
        "default_page_name": "ReportSection02288c58587aeaf4bd85"
    }
}
