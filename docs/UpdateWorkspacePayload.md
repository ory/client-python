# UpdateWorkspacePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workspace. | 

## Example

```python
from ory_client.models.update_workspace_payload import UpdateWorkspacePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspacePayload from a JSON string
update_workspace_payload_instance = UpdateWorkspacePayload.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspacePayload.to_json())

# convert the object into a dict
update_workspace_payload_dict = update_workspace_payload_instance.to_dict()
# create an instance of UpdateWorkspacePayload from a dict
update_workspace_payload_form_dict = update_workspace_payload.from_dict(update_workspace_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


