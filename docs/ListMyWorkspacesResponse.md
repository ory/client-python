# ListMyWorkspacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**next_page_token** | **str** |  | 
**workspaces** | [**List[WorkspaceMeta]**](WorkspaceMeta.md) |  | 

## Example

```python
from ory_client.models.list_my_workspaces_response import ListMyWorkspacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMyWorkspacesResponse from a JSON string
list_my_workspaces_response_instance = ListMyWorkspacesResponse.from_json(json)
# print the JSON string representation of the object
print(ListMyWorkspacesResponse.to_json())

# convert the object into a dict
list_my_workspaces_response_dict = list_my_workspaces_response_instance.to_dict()
# create an instance of ListMyWorkspacesResponse from a dict
list_my_workspaces_response_form_dict = list_my_workspaces_response.from_dict(list_my_workspaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


