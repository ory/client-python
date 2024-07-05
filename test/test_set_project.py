# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.set_project import SetProject

class TestSetProject(unittest.TestCase):
    """SetProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetProject:
        """Test SetProject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetProject`
        """
        model = SetProject()
        if include_optional:
            return SetProject(
                cors_admin = ory_client.models.project_cors.projectCors(
                    enabled = True, 
                    origins = [
                        ''
                        ], ),
                cors_public = ory_client.models.project_cors.projectCors(
                    enabled = True, 
                    origins = [
                        ''
                        ], ),
                name = '',
                services = ory_client.models.project_services.projectServices(
                    identity = ory_client.models.project_service_identity.projectServiceIdentity(
                        config = ory_client.models.config.config(), ), 
                    oauth2 = ory_client.models.project_service_o_auth2.projectServiceOAuth2(
                        config = ory_client.models.config.config(), ), 
                    permission = ory_client.models.project_service_permission.projectServicePermission(
                        config = ory_client.models.config.config(), ), )
            )
        else:
            return SetProject(
                cors_admin = ory_client.models.project_cors.projectCors(
                    enabled = True, 
                    origins = [
                        ''
                        ], ),
                cors_public = ory_client.models.project_cors.projectCors(
                    enabled = True, 
                    origins = [
                        ''
                        ], ),
                name = '',
                services = ory_client.models.project_services.projectServices(
                    identity = ory_client.models.project_service_identity.projectServiceIdentity(
                        config = ory_client.models.config.config(), ), 
                    oauth2 = ory_client.models.project_service_o_auth2.projectServiceOAuth2(
                        config = ory_client.models.config.config(), ), 
                    permission = ory_client.models.project_service_permission.projectServicePermission(
                        config = ory_client.models.config.config(), ), ),
        )
        """

    def testSetProject(self):
        """Test SetProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
