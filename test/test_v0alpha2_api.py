"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.1.0-alpha.4
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.v0alpha2_api import V0alpha2Api  # noqa: E501


class TestV0alpha2Api(unittest.TestCase):
    """V0alpha2Api unit test stubs"""

    def setUp(self):
        self.api = V0alpha2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_create_identity(self):
        """Test case for admin_create_identity

        Create an Identity  # noqa: E501
        """
        pass

    def test_admin_create_self_service_recovery_link(self):
        """Test case for admin_create_self_service_recovery_link

        Create a Recovery Link  # noqa: E501
        """
        pass

    def test_admin_delete_identity(self):
        """Test case for admin_delete_identity

        Delete an Identity  # noqa: E501
        """
        pass

    def test_admin_delete_identity_sessions(self):
        """Test case for admin_delete_identity_sessions

        Calling this endpoint irrecoverably and permanently deletes and invalidates all sessions that belong to the given Identity.  # noqa: E501
        """
        pass

    def test_admin_extend_session(self):
        """Test case for admin_extend_session

        Calling this endpoint extends the given session ID. If `session.earliest_possible_extend` is set it will only extend the session after the specified time has passed.  # noqa: E501
        """
        pass

    def test_admin_get_identity(self):
        """Test case for admin_get_identity

        Get an Identity  # noqa: E501
        """
        pass

    def test_admin_list_identities(self):
        """Test case for admin_list_identities

        List Identities  # noqa: E501
        """
        pass

    def test_admin_list_identity_sessions(self):
        """Test case for admin_list_identity_sessions

        This endpoint returns all sessions that belong to the given Identity.  # noqa: E501
        """
        pass

    def test_admin_update_identity(self):
        """Test case for admin_update_identity

        Update an Identity  # noqa: E501
        """
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a Project  # noqa: E501
        """
        pass

    def test_create_self_service_logout_flow_url_for_browsers(self):
        """Test case for create_self_service_logout_flow_url_for_browsers

        Create a Logout URL for Browsers  # noqa: E501
        """
        pass

    def test_get_json_schema(self):
        """Test case for get_json_schema

        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get a Project  # noqa: E501
        """
        pass

    def test_get_project_members(self):
        """Test case for get_project_members

        Get all members associated with this project.  # noqa: E501
        """
        pass

    def test_get_self_service_error(self):
        """Test case for get_self_service_error

        Get Self-Service Errors  # noqa: E501
        """
        pass

    def test_get_self_service_login_flow(self):
        """Test case for get_self_service_login_flow

        Get Login Flow  # noqa: E501
        """
        pass

    def test_get_self_service_recovery_flow(self):
        """Test case for get_self_service_recovery_flow

        Get Recovery Flow  # noqa: E501
        """
        pass

    def test_get_self_service_registration_flow(self):
        """Test case for get_self_service_registration_flow

        Get Registration Flow  # noqa: E501
        """
        pass

    def test_get_self_service_settings_flow(self):
        """Test case for get_self_service_settings_flow

        Get Settings Flow  # noqa: E501
        """
        pass

    def test_get_self_service_verification_flow(self):
        """Test case for get_self_service_verification_flow

        Get Verification Flow  # noqa: E501
        """
        pass

    def test_get_web_authn_java_script(self):
        """Test case for get_web_authn_java_script

        Get WebAuthn JavaScript  # noqa: E501
        """
        pass

    def test_initialize_self_service_login_flow_for_browsers(self):
        """Test case for initialize_self_service_login_flow_for_browsers

        Initialize Login Flow for Browsers  # noqa: E501
        """
        pass

    def test_initialize_self_service_login_flow_without_browser(self):
        """Test case for initialize_self_service_login_flow_without_browser

        Initialize Login Flow for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_initialize_self_service_recovery_flow_for_browsers(self):
        """Test case for initialize_self_service_recovery_flow_for_browsers

        Initialize Recovery Flow for Browsers  # noqa: E501
        """
        pass

    def test_initialize_self_service_recovery_flow_without_browser(self):
        """Test case for initialize_self_service_recovery_flow_without_browser

        Initialize Recovery Flow for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_initialize_self_service_registration_flow_for_browsers(self):
        """Test case for initialize_self_service_registration_flow_for_browsers

        Initialize Registration Flow for Browsers  # noqa: E501
        """
        pass

    def test_initialize_self_service_registration_flow_without_browser(self):
        """Test case for initialize_self_service_registration_flow_without_browser

        Initialize Registration Flow for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_initialize_self_service_settings_flow_for_browsers(self):
        """Test case for initialize_self_service_settings_flow_for_browsers

        Initialize Settings Flow for Browsers  # noqa: E501
        """
        pass

    def test_initialize_self_service_settings_flow_without_browser(self):
        """Test case for initialize_self_service_settings_flow_without_browser

        Initialize Settings Flow for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_initialize_self_service_verification_flow_for_browsers(self):
        """Test case for initialize_self_service_verification_flow_for_browsers

        Initialize Verification Flow for Browser Clients  # noqa: E501
        """
        pass

    def test_initialize_self_service_verification_flow_without_browser(self):
        """Test case for initialize_self_service_verification_flow_without_browser

        Initialize Verification Flow for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_list_identity_schemas(self):
        """Test case for list_identity_schemas

        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        List All Projects  # noqa: E501
        """
        pass

    def test_list_sessions(self):
        """Test case for list_sessions

        This endpoints returns all other active sessions that belong to the logged-in user. The current session can be retrieved by calling the `/sessions/whoami` endpoint.  # noqa: E501
        """
        pass

    def test_patch_project(self):
        """Test case for patch_project

        Patch an Ory Cloud Project Configuration  # noqa: E501
        """
        pass

    def test_purge_project(self):
        """Test case for purge_project

        Irrecoverably Purge a Project  # noqa: E501
        """
        pass

    def test_remove_project_member(self):
        """Test case for remove_project_member

        Remove a member associated with this project. This also sets their invite status to `REMOVED`.  # noqa: E501
        """
        pass

    def test_revoke_session(self):
        """Test case for revoke_session

        Calling this endpoint invalidates the specified session. The current session cannot be revoked. Session data are not deleted.  # noqa: E501
        """
        pass

    def test_revoke_sessions(self):
        """Test case for revoke_sessions

        Calling this endpoint invalidates all except the current session that belong to the logged-in user. Session data are not deleted.  # noqa: E501
        """
        pass

    def test_submit_self_service_login_flow(self):
        """Test case for submit_self_service_login_flow

        Submit a Login Flow  # noqa: E501
        """
        pass

    def test_submit_self_service_logout_flow(self):
        """Test case for submit_self_service_logout_flow

        Complete Self-Service Logout  # noqa: E501
        """
        pass

    def test_submit_self_service_logout_flow_without_browser(self):
        """Test case for submit_self_service_logout_flow_without_browser

        Perform Logout for APIs, Services, Apps, ...  # noqa: E501
        """
        pass

    def test_submit_self_service_recovery_flow(self):
        """Test case for submit_self_service_recovery_flow

        Complete Recovery Flow  # noqa: E501
        """
        pass

    def test_submit_self_service_registration_flow(self):
        """Test case for submit_self_service_registration_flow

        Submit a Registration Flow  # noqa: E501
        """
        pass

    def test_submit_self_service_settings_flow(self):
        """Test case for submit_self_service_settings_flow

        Complete Settings Flow  # noqa: E501
        """
        pass

    def test_submit_self_service_verification_flow(self):
        """Test case for submit_self_service_verification_flow

        Complete Verification Flow  # noqa: E501
        """
        pass

    def test_to_session(self):
        """Test case for to_session

        Check Who the Current HTTP Session Belongs To  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update an Ory Cloud Project Configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
