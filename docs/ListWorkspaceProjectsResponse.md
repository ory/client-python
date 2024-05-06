# ListWorkspaceProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**next_page** | **str** |  | 
**projects** | [**List[ProjectMetadata]**](ProjectMetadata.md) |  | 

## Example

```python
from ory_client.models.list_workspace_projects_response import ListWorkspaceProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspaceProjectsResponse from a JSON string
list_workspace_projects_response_instance = ListWorkspaceProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ListWorkspaceProjectsResponse.to_json())

# convert the object into a dict
list_workspace_projects_response_dict = list_workspace_projects_response_instance.to_dict()
# create an instance of ListWorkspaceProjectsResponse from a dict
list_workspace_projects_response_form_dict = list_workspace_projects_response.from_dict(list_workspace_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


