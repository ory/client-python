# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.15.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.frontend_api import FrontendApi


class TestFrontendApi(unittest.TestCase):
    """FrontendApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FrontendApi()

    def tearDown(self) -> None:
        pass

    def test_create_browser_login_flow(self) -> None:
        """Test case for create_browser_login_flow

        Create Login Flow for Browsers
        """
        pass

    def test_create_browser_logout_flow(self) -> None:
        """Test case for create_browser_logout_flow

        Create a Logout URL for Browsers
        """
        pass

    def test_create_browser_recovery_flow(self) -> None:
        """Test case for create_browser_recovery_flow

        Create Recovery Flow for Browsers
        """
        pass

    def test_create_browser_registration_flow(self) -> None:
        """Test case for create_browser_registration_flow

        Create Registration Flow for Browsers
        """
        pass

    def test_create_browser_settings_flow(self) -> None:
        """Test case for create_browser_settings_flow

        Create Settings Flow for Browsers
        """
        pass

    def test_create_browser_verification_flow(self) -> None:
        """Test case for create_browser_verification_flow

        Create Verification Flow for Browser Clients
        """
        pass

    def test_create_native_login_flow(self) -> None:
        """Test case for create_native_login_flow

        Create Login Flow for Native Apps
        """
        pass

    def test_create_native_recovery_flow(self) -> None:
        """Test case for create_native_recovery_flow

        Create Recovery Flow for Native Apps
        """
        pass

    def test_create_native_registration_flow(self) -> None:
        """Test case for create_native_registration_flow

        Create Registration Flow for Native Apps
        """
        pass

    def test_create_native_settings_flow(self) -> None:
        """Test case for create_native_settings_flow

        Create Settings Flow for Native Apps
        """
        pass

    def test_create_native_verification_flow(self) -> None:
        """Test case for create_native_verification_flow

        Create Verification Flow for Native Apps
        """
        pass

    def test_disable_my_other_sessions(self) -> None:
        """Test case for disable_my_other_sessions

        Disable my other sessions
        """
        pass

    def test_disable_my_session(self) -> None:
        """Test case for disable_my_session

        Disable one of my sessions
        """
        pass

    def test_exchange_session_token(self) -> None:
        """Test case for exchange_session_token

        Exchange Session Token
        """
        pass

    def test_get_flow_error(self) -> None:
        """Test case for get_flow_error

        Get User-Flow Errors
        """
        pass

    def test_get_login_flow(self) -> None:
        """Test case for get_login_flow

        Get Login Flow
        """
        pass

    def test_get_recovery_flow(self) -> None:
        """Test case for get_recovery_flow

        Get Recovery Flow
        """
        pass

    def test_get_registration_flow(self) -> None:
        """Test case for get_registration_flow

        Get Registration Flow
        """
        pass

    def test_get_settings_flow(self) -> None:
        """Test case for get_settings_flow

        Get Settings Flow
        """
        pass

    def test_get_verification_flow(self) -> None:
        """Test case for get_verification_flow

        Get Verification Flow
        """
        pass

    def test_get_web_authn_java_script(self) -> None:
        """Test case for get_web_authn_java_script

        Get WebAuthn JavaScript
        """
        pass

    def test_list_my_sessions(self) -> None:
        """Test case for list_my_sessions

        Get My Active Sessions
        """
        pass

    def test_perform_native_logout(self) -> None:
        """Test case for perform_native_logout

        Perform Logout for Native Apps
        """
        pass

    def test_to_session(self) -> None:
        """Test case for to_session

        Check Who the Current HTTP Session Belongs To
        """
        pass

    def test_update_login_flow(self) -> None:
        """Test case for update_login_flow

        Submit a Login Flow
        """
        pass

    def test_update_logout_flow(self) -> None:
        """Test case for update_logout_flow

        Update Logout Flow
        """
        pass

    def test_update_recovery_flow(self) -> None:
        """Test case for update_recovery_flow

        Update Recovery Flow
        """
        pass

    def test_update_registration_flow(self) -> None:
        """Test case for update_registration_flow

        Update Registration Flow
        """
        pass

    def test_update_settings_flow(self) -> None:
        """Test case for update_settings_flow

        Complete Settings Flow
        """
        pass

    def test_update_verification_flow(self) -> None:
        """Test case for update_verification_flow

        Complete Verification Flow
        """
        pass


if __name__ == '__main__':
    unittest.main()
