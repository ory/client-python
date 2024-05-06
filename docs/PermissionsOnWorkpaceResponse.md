# PermissionsOnWorkpaceResponse

Get Permissions on Project Request Parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from ory_client.models.permissions_on_workpace_response import PermissionsOnWorkpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsOnWorkpaceResponse from a JSON string
permissions_on_workpace_response_instance = PermissionsOnWorkpaceResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionsOnWorkpaceResponse.to_json())

# convert the object into a dict
permissions_on_workpace_response_dict = permissions_on_workpace_response_instance.to_dict()
# create an instance of PermissionsOnWorkpaceResponse from a dict
permissions_on_workpace_response_form_dict = permissions_on_workpace_response.from_dict(permissions_on_workpace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


