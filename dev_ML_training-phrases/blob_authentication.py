"""
FILE: blob_authentication.py
DESCRIPTION:
    Authenticates a client via Default Azure Credential.
    The returned signature can be used with the credential parameter of any
     BlobServiceClient, ContainerClient, BlobClient.
    Also configures credentials to access resources in Azure Government cloud
     instead of default Azure AD endpoint for Azure Public Cloud.
USAGE:
    Set the following environment variables with your own values before using:
     1) OAUTH_STORAGE_ACCOUNT_NAME - the oauth storage account name.
"""

import os


class Auth(object):

    oauth_url = "https://{}.blob.core.usgovcloudapi.net".format(
        os.getenv("OAUTH_STORAGE_ACCOUNT_NAME")
    )

    def auth_default_azure_credential(self):
        # [START create_blob_service_client_oauth_default_credential]
        # Get a credential for authentication
        # Default Azure Credentials attempt a chained set of authentication
        # methods, per documentation here:
        # https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity
        # The docs above specify all mechanisms which the defaultCredential
        # internally support.
        from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
        default_credential = DefaultAzureCredential(
            authority=AzureAuthorityHosts.AZURE_GOVERNMENT)

        # Instantiate a BlobServiceClient using a token credential
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient(
            account_url=self.oauth_url,
            credential=default_credential
        )
        # [END create_blob_service_client_oauth_default_credential]

        return blob_service_client
