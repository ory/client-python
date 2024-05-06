# WorkspaceMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**subscription_id** | **str** |  | [optional] 
**subscription_plan** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from ory_client.models.workspace_meta import WorkspaceMeta

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMeta from a JSON string
workspace_meta_instance = WorkspaceMeta.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMeta.to_json())

# convert the object into a dict
workspace_meta_dict = workspace_meta_instance.to_dict()
# create an instance of WorkspaceMeta from a dict
workspace_meta_form_dict = workspace_meta.from_dict(workspace_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


