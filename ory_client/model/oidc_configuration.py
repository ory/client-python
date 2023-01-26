"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.7
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ory_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ory_client.exceptions import ApiAttributeError



class OidcConfiguration(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'authorization_endpoint': (str,),  # noqa: E501
            'id_token_signed_response_alg': ([str],),  # noqa: E501
            'id_token_signing_alg_values_supported': ([str],),  # noqa: E501
            'issuer': (str,),  # noqa: E501
            'jwks_uri': (str,),  # noqa: E501
            'response_types_supported': ([str],),  # noqa: E501
            'subject_types_supported': ([str],),  # noqa: E501
            'token_endpoint': (str,),  # noqa: E501
            'userinfo_signed_response_alg': ([str],),  # noqa: E501
            'backchannel_logout_session_supported': (bool,),  # noqa: E501
            'backchannel_logout_supported': (bool,),  # noqa: E501
            'claims_parameter_supported': (bool,),  # noqa: E501
            'claims_supported': ([str],),  # noqa: E501
            'code_challenge_methods_supported': ([str],),  # noqa: E501
            'end_session_endpoint': (str,),  # noqa: E501
            'frontchannel_logout_session_supported': (bool,),  # noqa: E501
            'frontchannel_logout_supported': (bool,),  # noqa: E501
            'grant_types_supported': ([str],),  # noqa: E501
            'registration_endpoint': (str,),  # noqa: E501
            'request_object_signing_alg_values_supported': ([str],),  # noqa: E501
            'request_parameter_supported': (bool,),  # noqa: E501
            'request_uri_parameter_supported': (bool,),  # noqa: E501
            'require_request_uri_registration': (bool,),  # noqa: E501
            'response_modes_supported': ([str],),  # noqa: E501
            'revocation_endpoint': (str,),  # noqa: E501
            'scopes_supported': ([str],),  # noqa: E501
            'token_endpoint_auth_methods_supported': ([str],),  # noqa: E501
            'userinfo_endpoint': (str,),  # noqa: E501
            'userinfo_signing_alg_values_supported': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'authorization_endpoint': 'authorization_endpoint',  # noqa: E501
        'id_token_signed_response_alg': 'id_token_signed_response_alg',  # noqa: E501
        'id_token_signing_alg_values_supported': 'id_token_signing_alg_values_supported',  # noqa: E501
        'issuer': 'issuer',  # noqa: E501
        'jwks_uri': 'jwks_uri',  # noqa: E501
        'response_types_supported': 'response_types_supported',  # noqa: E501
        'subject_types_supported': 'subject_types_supported',  # noqa: E501
        'token_endpoint': 'token_endpoint',  # noqa: E501
        'userinfo_signed_response_alg': 'userinfo_signed_response_alg',  # noqa: E501
        'backchannel_logout_session_supported': 'backchannel_logout_session_supported',  # noqa: E501
        'backchannel_logout_supported': 'backchannel_logout_supported',  # noqa: E501
        'claims_parameter_supported': 'claims_parameter_supported',  # noqa: E501
        'claims_supported': 'claims_supported',  # noqa: E501
        'code_challenge_methods_supported': 'code_challenge_methods_supported',  # noqa: E501
        'end_session_endpoint': 'end_session_endpoint',  # noqa: E501
        'frontchannel_logout_session_supported': 'frontchannel_logout_session_supported',  # noqa: E501
        'frontchannel_logout_supported': 'frontchannel_logout_supported',  # noqa: E501
        'grant_types_supported': 'grant_types_supported',  # noqa: E501
        'registration_endpoint': 'registration_endpoint',  # noqa: E501
        'request_object_signing_alg_values_supported': 'request_object_signing_alg_values_supported',  # noqa: E501
        'request_parameter_supported': 'request_parameter_supported',  # noqa: E501
        'request_uri_parameter_supported': 'request_uri_parameter_supported',  # noqa: E501
        'require_request_uri_registration': 'require_request_uri_registration',  # noqa: E501
        'response_modes_supported': 'response_modes_supported',  # noqa: E501
        'revocation_endpoint': 'revocation_endpoint',  # noqa: E501
        'scopes_supported': 'scopes_supported',  # noqa: E501
        'token_endpoint_auth_methods_supported': 'token_endpoint_auth_methods_supported',  # noqa: E501
        'userinfo_endpoint': 'userinfo_endpoint',  # noqa: E501
        'userinfo_signing_alg_values_supported': 'userinfo_signing_alg_values_supported',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, authorization_endpoint, id_token_signed_response_alg, id_token_signing_alg_values_supported, issuer, jwks_uri, response_types_supported, subject_types_supported, token_endpoint, userinfo_signed_response_alg, *args, **kwargs):  # noqa: E501
        """OidcConfiguration - a model defined in OpenAPI

        Args:
            authorization_endpoint (str): OAuth 2.0 Authorization Endpoint URL
            id_token_signed_response_alg ([str]): OpenID Connect Default ID Token Signing Algorithms  Algorithm used to sign OpenID Connect ID Tokens.
            id_token_signing_alg_values_supported ([str]): OpenID Connect Supported ID Token Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.
            issuer (str): OpenID Connect Issuer URL  An URL using the https scheme with no query or fragment component that the OP asserts as its IssuerURL Identifier. If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.
            jwks_uri (str): OpenID Connect Well-Known JSON Web Keys URL  URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.
            response_types_supported ([str]): OAuth 2.0 Supported Response Types  JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.
            subject_types_supported ([str]): OpenID Connect Supported Subject Types  JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.
            token_endpoint (str): OAuth 2.0 Token Endpoint URL
            userinfo_signed_response_alg ([str]): OpenID Connect User Userinfo Signing Algorithm  Algorithm used to sign OpenID Connect Userinfo Responses.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            backchannel_logout_session_supported (bool): OpenID Connect Back-Channel Logout Session Required  Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP. [optional]  # noqa: E501
            backchannel_logout_supported (bool): OpenID Connect Back-Channel Logout Supported  Boolean value specifying whether the OP supports back-channel logout, with true indicating support.. [optional]  # noqa: E501
            claims_parameter_supported (bool): OpenID Connect Claims Parameter Parameter Supported  Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support.. [optional]  # noqa: E501
            claims_supported ([str]): OpenID Connect Supported Claims  JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for. Note that for privacy or other reasons, this might not be an exhaustive list.. [optional]  # noqa: E501
            code_challenge_methods_supported ([str]): OAuth 2.0 PKCE Supported Code Challenge Methods  JSON array containing a list of Proof Key for Code Exchange (PKCE) [RFC7636] code challenge methods supported by this authorization server.. [optional]  # noqa: E501
            end_session_endpoint (str): OpenID Connect End-Session Endpoint  URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.. [optional]  # noqa: E501
            frontchannel_logout_session_supported (bool): OpenID Connect Front-Channel Logout Session Required  Boolean value specifying whether the OP can pass iss (issuer) and sid (session ID) query parameters to identify the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also included in ID Tokens issued by the OP.. [optional]  # noqa: E501
            frontchannel_logout_supported (bool): OpenID Connect Front-Channel Logout Supported  Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support.. [optional]  # noqa: E501
            grant_types_supported ([str]): OAuth 2.0 Supported Grant Types  JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.. [optional]  # noqa: E501
            registration_endpoint (str): OpenID Connect Dynamic Client Registration Endpoint URL. [optional]  # noqa: E501
            request_object_signing_alg_values_supported ([str]): OpenID Connect Supported Request Object Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for Request Objects, which are described in Section 6.1 of OpenID Connect Core 1.0 [OpenID.Core]. These algorithms are used both when the Request Object is passed by value (using the request parameter) and when it is passed by reference (using the request_uri parameter).. [optional]  # noqa: E501
            request_parameter_supported (bool): OpenID Connect Request Parameter Supported  Boolean value specifying whether the OP supports use of the request parameter, with true indicating support.. [optional]  # noqa: E501
            request_uri_parameter_supported (bool): OpenID Connect Request URI Parameter Supported  Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support.. [optional]  # noqa: E501
            require_request_uri_registration (bool): OpenID Connect Requires Request URI Registration  Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter.. [optional]  # noqa: E501
            response_modes_supported ([str]): OAuth 2.0 Supported Response Modes  JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports.. [optional]  # noqa: E501
            revocation_endpoint (str): OAuth 2.0 Token Revocation URL  URL of the authorization server's OAuth 2.0 revocation endpoint.. [optional]  # noqa: E501
            scopes_supported ([str]): OAuth 2.0 Supported Scope Values  JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports. The server MUST support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this parameter is used. [optional]  # noqa: E501
            token_endpoint_auth_methods_supported ([str]): OAuth 2.0 Supported Client Authentication Methods  JSON array containing a list of Client Authentication methods supported by this Token Endpoint. The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0. [optional]  # noqa: E501
            userinfo_endpoint (str): OpenID Connect Userinfo URL  URL of the OP's UserInfo Endpoint.. [optional]  # noqa: E501
            userinfo_signing_alg_values_supported ([str]): OpenID Connect Supported Userinfo Signing Algorithm  JSON array containing a list of the JWS [JWS] signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.authorization_endpoint = authorization_endpoint
        self.id_token_signed_response_alg = id_token_signed_response_alg
        self.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self.issuer = issuer
        self.jwks_uri = jwks_uri
        self.response_types_supported = response_types_supported
        self.subject_types_supported = subject_types_supported
        self.token_endpoint = token_endpoint
        self.userinfo_signed_response_alg = userinfo_signed_response_alg
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, authorization_endpoint, id_token_signed_response_alg, id_token_signing_alg_values_supported, issuer, jwks_uri, response_types_supported, subject_types_supported, token_endpoint, userinfo_signed_response_alg, *args, **kwargs):  # noqa: E501
        """OidcConfiguration - a model defined in OpenAPI

        Args:
            authorization_endpoint (str): OAuth 2.0 Authorization Endpoint URL
            id_token_signed_response_alg ([str]): OpenID Connect Default ID Token Signing Algorithms  Algorithm used to sign OpenID Connect ID Tokens.
            id_token_signing_alg_values_supported ([str]): OpenID Connect Supported ID Token Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.
            issuer (str): OpenID Connect Issuer URL  An URL using the https scheme with no query or fragment component that the OP asserts as its IssuerURL Identifier. If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.
            jwks_uri (str): OpenID Connect Well-Known JSON Web Keys URL  URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.
            response_types_supported ([str]): OAuth 2.0 Supported Response Types  JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.
            subject_types_supported ([str]): OpenID Connect Supported Subject Types  JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.
            token_endpoint (str): OAuth 2.0 Token Endpoint URL
            userinfo_signed_response_alg ([str]): OpenID Connect User Userinfo Signing Algorithm  Algorithm used to sign OpenID Connect Userinfo Responses.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            backchannel_logout_session_supported (bool): OpenID Connect Back-Channel Logout Session Required  Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP. [optional]  # noqa: E501
            backchannel_logout_supported (bool): OpenID Connect Back-Channel Logout Supported  Boolean value specifying whether the OP supports back-channel logout, with true indicating support.. [optional]  # noqa: E501
            claims_parameter_supported (bool): OpenID Connect Claims Parameter Parameter Supported  Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support.. [optional]  # noqa: E501
            claims_supported ([str]): OpenID Connect Supported Claims  JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for. Note that for privacy or other reasons, this might not be an exhaustive list.. [optional]  # noqa: E501
            code_challenge_methods_supported ([str]): OAuth 2.0 PKCE Supported Code Challenge Methods  JSON array containing a list of Proof Key for Code Exchange (PKCE) [RFC7636] code challenge methods supported by this authorization server.. [optional]  # noqa: E501
            end_session_endpoint (str): OpenID Connect End-Session Endpoint  URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.. [optional]  # noqa: E501
            frontchannel_logout_session_supported (bool): OpenID Connect Front-Channel Logout Session Required  Boolean value specifying whether the OP can pass iss (issuer) and sid (session ID) query parameters to identify the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also included in ID Tokens issued by the OP.. [optional]  # noqa: E501
            frontchannel_logout_supported (bool): OpenID Connect Front-Channel Logout Supported  Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support.. [optional]  # noqa: E501
            grant_types_supported ([str]): OAuth 2.0 Supported Grant Types  JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.. [optional]  # noqa: E501
            registration_endpoint (str): OpenID Connect Dynamic Client Registration Endpoint URL. [optional]  # noqa: E501
            request_object_signing_alg_values_supported ([str]): OpenID Connect Supported Request Object Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for Request Objects, which are described in Section 6.1 of OpenID Connect Core 1.0 [OpenID.Core]. These algorithms are used both when the Request Object is passed by value (using the request parameter) and when it is passed by reference (using the request_uri parameter).. [optional]  # noqa: E501
            request_parameter_supported (bool): OpenID Connect Request Parameter Supported  Boolean value specifying whether the OP supports use of the request parameter, with true indicating support.. [optional]  # noqa: E501
            request_uri_parameter_supported (bool): OpenID Connect Request URI Parameter Supported  Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support.. [optional]  # noqa: E501
            require_request_uri_registration (bool): OpenID Connect Requires Request URI Registration  Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter.. [optional]  # noqa: E501
            response_modes_supported ([str]): OAuth 2.0 Supported Response Modes  JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports.. [optional]  # noqa: E501
            revocation_endpoint (str): OAuth 2.0 Token Revocation URL  URL of the authorization server's OAuth 2.0 revocation endpoint.. [optional]  # noqa: E501
            scopes_supported ([str]): OAuth 2.0 Supported Scope Values  JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports. The server MUST support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this parameter is used. [optional]  # noqa: E501
            token_endpoint_auth_methods_supported ([str]): OAuth 2.0 Supported Client Authentication Methods  JSON array containing a list of Client Authentication methods supported by this Token Endpoint. The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0. [optional]  # noqa: E501
            userinfo_endpoint (str): OpenID Connect Userinfo URL  URL of the OP's UserInfo Endpoint.. [optional]  # noqa: E501
            userinfo_signing_alg_values_supported ([str]): OpenID Connect Supported Userinfo Signing Algorithm  JSON array containing a list of the JWS [JWS] signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.authorization_endpoint = authorization_endpoint
        self.id_token_signed_response_alg = id_token_signed_response_alg
        self.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self.issuer = issuer
        self.jwks_uri = jwks_uri
        self.response_types_supported = response_types_supported
        self.subject_types_supported = subject_types_supported
        self.token_endpoint = token_endpoint
        self.userinfo_signed_response_alg = userinfo_signed_response_alg
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
