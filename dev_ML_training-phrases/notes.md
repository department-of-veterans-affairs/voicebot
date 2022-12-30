# VA GitHub repos
## Chatbot
[github repo](https://github.com/department-of-veterans-affairs/va-virtual-agent)
## Chat Transcript Analysis
[github repo](https://github.ec.va.gov/ECSO/mct_text_analytics)

# Azure Documentation
[Azure/Learn/Documentation](https://learn.microsoft.com/en-us/azure/)

# Azure SDK for Python
[azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python)

[samples](https://github.com/Azure-Samples)

[azure-identity](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python)

[azure-storage-blob](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.14.1/sdk/identity/azure-identity#credential-classes)

[azure-storage-blob authentication samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/storage/azure-storage-blob/samples/blob_samples_authentication.py)

[environment-variables](https://github.com/Azure/azure-sdk-for-python/tree/azure-storage-blob_12.14.1/sdk/identity/azure-identity#environment-variables)

# Azure Government

```python
import os
from msrestazure.azure_cloud import AZURE_GOVERNMENT as CLOUD
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential, AzureAuthorityHosts

# Assumes the subscription ID and tenant ID to use are in the AZURE_SUBSCRIPTION_ID and
# AZURE_TENANT_ID environment variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]

# When using sovereign domains (that is, any cloud other than AZURE_PUBLIC_CLOUD),
# you must use an authority with DefaultAzureCredential.
credential = DefaultAzureCredential(authority=AzureAuthorityHosts.AZURE_GOVERNMENT)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])

subscription_client = SubscriptionClient(
    credential,
    base_url=CLOUD.endpoints.resource_manager,
    credential_scopes=[CLOUD.endpoints.resource_manager + "/.default"])
``` 

## Azure Government - see also:
[Hybrid Identity](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/reference-connect-government-cloud)

[Trusted Internet Connections](https://learn.microsoft.com/en-us/azure/azure-government/compliance/compliance-tic)

# DataBricks
[Developer tools and guidance](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/)

[integrate IDE with dbx](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/index-ide)

[azure-databricks-mlops-using-mlflow](https://learn.microsoft.com/en-us/samples/azure-samples/azure-databricks-mlops-mlflow/azure-databricks-mlops-using-mlflow/)

[Sign in using a service principal](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/)

# Language Models
[Transformers](https://github.com/huggingface/transformers)

# VA ECSO
[Azure Configuration & Deployment Settings](https://dvagov.sharepoint.com/sites/OITECSO/Shared%20Documents/Cloud%20101/CSP%20TSS%20Service%20Guides%20User%20Acceptance/VAEC_Azure_Baseline_Config_Mgmt_Plan.pdf)

