from blob_authentication import Auth


def download_to_file(container, blob, file):
    blob = blob_service_client.get_blob_client(container, blob)
    with open(file, "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)


# Instantiate a BlobServiceClient for storage account identified by
#  OAUTH_STORAGE_ACCOUNT_NAME environment variable in Azure Government cloud
auth = Auth()
blob_service_client = auth.auth_default_azure_credential()

# Download blob in container to file
download_to_file(
    container="dataverse-vappveoprod-unq22755fdd77ae47fe8f9536f82c0f0",
    blob="model.json",
    file="model.json")

download_to_file(
    container="dataverse-vappveoprod-unq22755fdd77ae47fe8f9536f82c0f0",
    blob="/conversationtranscript/2022.csv",
    file="conversation_transcript.csv")
