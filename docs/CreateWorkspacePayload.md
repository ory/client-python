# CreateWorkspacePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workspace | 

## Example

```python
from ory_client.models.create_workspace_payload import CreateWorkspacePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspacePayload from a JSON string
create_workspace_payload_instance = CreateWorkspacePayload.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspacePayload.to_json())

# convert the object into a dict
create_workspace_payload_dict = create_workspace_payload_instance.to_dict()
# create an instance of CreateWorkspacePayload from a dict
create_workspace_payload_form_dict = create_workspace_payload.from_dict(create_workspace_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


