# MigrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment of the project in the workspace. Can be one of \&quot;prod\&quot; or \&quot;dev\&quot;. Note that the number of projects in the \&quot;prod\&quot; environment is limited depending on the subscription. prod Production stage Staging dev Development | 
**project_subscription** | **str** | The action to take with the project subscription. Can be one of \&quot;migrate\&quot;, and \&quot;ignore\&quot;. \&quot;migrate\&quot; will migrate the project subscription to the workspace. \&quot;ignore\&quot; will ignore the project subscription. migrate ProjectSubscriptionActionMigrate  ProjectSubscriptionActionMigrate will migrate the project subscription to the  workspace. ignore ProjectSubscriptionActionIgnore  ProjectSubscriptionActionIgnore will ignore the project subscription. | 

## Example

```python
from ory_client.models.migration_options import MigrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationOptions from a JSON string
migration_options_instance = MigrationOptions.from_json(json)
# print the JSON string representation of the object
print(MigrationOptions.to_json())

# convert the object into a dict
migration_options_dict = migration_options_instance.to_dict()
# create an instance of MigrationOptions from a dict
migration_options_form_dict = migration_options.from_dict(migration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


