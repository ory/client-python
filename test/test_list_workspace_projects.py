# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.list_workspace_projects import ListWorkspaceProjects

class TestListWorkspaceProjects(unittest.TestCase):
    """ListWorkspaceProjects unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListWorkspaceProjects:
        """Test ListWorkspaceProjects
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWorkspaceProjects`
        """
        model = ListWorkspaceProjects()
        if include_optional:
            return ListWorkspaceProjects(
                has_next_page = True,
                next_page = '',
                projects = [
                    ory_client.models.project_metadata.projectMetadata(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        environment = 'prod', 
                        home_region = 'eu-central', 
                        hosts = [
                            ''
                            ], 
                        id = '', 
                        name = '', 
                        slug = '', 
                        state = 'running', 
                        subscription_id = '', 
                        subscription_plan = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        workspace = ory_client.models.workspace.workspace(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            name = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        workspace_id = '', )
                    ]
            )
        else:
            return ListWorkspaceProjects(
                has_next_page = True,
                next_page = '',
                projects = [
                    ory_client.models.project_metadata.projectMetadata(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        environment = 'prod', 
                        home_region = 'eu-central', 
                        hosts = [
                            ''
                            ], 
                        id = '', 
                        name = '', 
                        slug = '', 
                        state = 'running', 
                        subscription_id = '', 
                        subscription_plan = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        workspace = ory_client.models.workspace.workspace(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            name = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        workspace_id = '', )
                    ],
        )
        """

    def testListWorkspaceProjects(self):
        """Test ListWorkspaceProjects"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
