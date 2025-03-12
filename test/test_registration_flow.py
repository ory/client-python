# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.18.5
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.registration_flow import RegistrationFlow

class TestRegistrationFlow(unittest.TestCase):
    """RegistrationFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegistrationFlow:
        """Test RegistrationFlow
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrationFlow`
        """
        model = RegistrationFlow()
        if include_optional:
            return RegistrationFlow(
                active = 'password',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                oauth2_login_challenge = '',
                oauth2_login_request = ory_client.models.contains_information_on_an_ongoing_login_request/.Contains information on an ongoing login request.(
                    challenge = '', 
                    client = ory_client.models.o_auth_2/0_client.OAuth 2.0 Client(
                        access_token_strategy = '', 
                        allowed_cors_origins = [
                            ''
                            ], 
                        audience = [
                            ''
                            ], 
                        authorization_code_grant_access_token_lifespan = '4ms', 
                        authorization_code_grant_id_token_lifespan = '4ms', 
                        authorization_code_grant_refresh_token_lifespan = '4ms', 
                        backchannel_logout_session_required = True, 
                        backchannel_logout_uri = '', 
                        client_credentials_grant_access_token_lifespan = '4ms', 
                        client_id = '', 
                        client_name = '', 
                        client_secret = '', 
                        client_secret_expires_at = 56, 
                        client_uri = '', 
                        contacts = , 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        frontchannel_logout_session_required = True, 
                        frontchannel_logout_uri = '', 
                        grant_types = , 
                        implicit_grant_access_token_lifespan = '4ms', 
                        implicit_grant_id_token_lifespan = '4ms', 
                        jwks = null, 
                        jwks_uri = '', 
                        jwt_bearer_grant_access_token_lifespan = '4ms', 
                        logo_uri = '', 
                        metadata = ory_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                        owner = '', 
                        policy_uri = '', 
                        post_logout_redirect_uris = , 
                        redirect_uris = , 
                        refresh_token_grant_access_token_lifespan = '4ms', 
                        refresh_token_grant_id_token_lifespan = '4ms', 
                        refresh_token_grant_refresh_token_lifespan = '4ms', 
                        registration_access_token = '', 
                        registration_client_uri = '', 
                        request_object_signing_alg = '', 
                        request_uris = , 
                        response_types = , 
                        scope = 'scope1 scope-2 scope.3 scope:4', 
                        sector_identifier_uri = '', 
                        skip_consent = True, 
                        skip_logout_consent = True, 
                        subject_type = '', 
                        token_endpoint_auth_method = 'client_secret_basic', 
                        token_endpoint_auth_signing_alg = '', 
                        tos_uri = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        userinfo_signed_response_alg = '', ), 
                    oidc_context = ory_client.models.contains_optional_information_about_the_open_id_connect_request/.Contains optional information about the OpenID Connect request.(
                        acr_values = [
                            ''
                            ], 
                        display = '', 
                        id_token_hint_claims = {
                            'key' : null
                            }, 
                        login_hint = '', 
                        ui_locales = [
                            ''
                            ], ), 
                    request_url = '', 
                    requested_access_token_audience = , 
                    requested_scope = , 
                    session_id = '', 
                    skip = True, 
                    subject = '', ),
                organization_id = '',
                request_url = '',
                return_to = '',
                session_token_exchange_code = '',
                state = None,
                transient_payload = None,
                type = '',
                ui = ory_client.models.ui_container.uiContainer(
                    action = '', 
                    messages = [
                        ory_client.models.ui_text.uiText(
                            context = ory_client.models.context.context(), 
                            id = 56, 
                            text = '', 
                            type = 'info', )
                        ], 
                    method = '', 
                    nodes = [
                        ory_client.models.node_represents_a_flow's_nodes.Node represents a flow's nodes(
                            attributes = null, 
                            group = 'default', 
                            messages = [
                                ory_client.models.ui_text.uiText(
                                    context = ory_client.models.context.context(), 
                                    id = 56, 
                                    text = '', 
                                    type = 'info', )
                                ], 
                            meta = ory_client.models.a_node's_meta_information.A Node's Meta Information(
                                label = , ), 
                            type = 'text', )
                        ], )
            )
        else:
            return RegistrationFlow(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request_url = '',
                state = None,
                type = '',
                ui = ory_client.models.ui_container.uiContainer(
                    action = '', 
                    messages = [
                        ory_client.models.ui_text.uiText(
                            context = ory_client.models.context.context(), 
                            id = 56, 
                            text = '', 
                            type = 'info', )
                        ], 
                    method = '', 
                    nodes = [
                        ory_client.models.node_represents_a_flow's_nodes.Node represents a flow's nodes(
                            attributes = null, 
                            group = 'default', 
                            messages = [
                                ory_client.models.ui_text.uiText(
                                    context = ory_client.models.context.context(), 
                                    id = 56, 
                                    text = '', 
                                    type = 'info', )
                                ], 
                            meta = ory_client.models.a_node's_meta_information.A Node's Meta Information(
                                label = , ), 
                            type = 'text', )
                        ], ),
        )
        """

    def testRegistrationFlow(self):
        """Test RegistrationFlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
