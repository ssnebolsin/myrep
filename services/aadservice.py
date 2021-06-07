# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from flask import current_app as app
import msal
import pbie_config


class AadService:

    @staticmethod
    def get_access_token():
        """Generates and returns Access token"""
        response = None
        try:
            authority = pbie_config.AUTHORITY.replace('organizations', pbie_config.TENANT_ID)
            clientapp = msal.ConfidentialClientApplication(pbie_config.CLIENT_ID, client_credential=pbie_config.CLIENT_SECRET, authority=authority)
            response = clientapp.acquire_token_for_client(scopes=pbie_config.SCOPE)
            return response['access_token']
        except Exception as ex:
            raise Exception('Error retrieving Access token\n' + str(ex))
