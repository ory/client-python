"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.11
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ory_client.api_client import ApiClient, Endpoint as _Endpoint
from ory_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ory_client.model.check_opl_syntax_result import CheckOplSyntaxResult
from ory_client.model.create_relationship_body import CreateRelationshipBody
from ory_client.model.error_generic import ErrorGeneric
from ory_client.model.relationship import Relationship
from ory_client.model.relationship_namespaces import RelationshipNamespaces
from ory_client.model.relationship_patch import RelationshipPatch
from ory_client.model.relationships import Relationships


class RelationshipApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.check_opl_syntax_endpoint = _Endpoint(
            settings={
                'response_type': (CheckOplSyntaxResult,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/opl/syntax/check',
                'operation_id': 'check_opl_syntax',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (str,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'text/plain'
                ]
            },
            api_client=api_client
        )
        self.create_relationship_endpoint = _Endpoint(
            settings={
                'response_type': (Relationship,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'create_relationship',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_relationship_body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'create_relationship_body':
                        (CreateRelationshipBody,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_relationship_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_relationships_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'delete_relationships',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'object',
                    'relation',
                    'subject_id',
                    'subject_set_namespace',
                    'subject_set_object',
                    'subject_set_relation',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'object':
                        (str,),
                    'relation':
                        (str,),
                    'subject_id':
                        (str,),
                    'subject_set_namespace':
                        (str,),
                    'subject_set_object':
                        (str,),
                    'subject_set_relation':
                        (str,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'object': 'object',
                    'relation': 'relation',
                    'subject_id': 'subject_id',
                    'subject_set_namespace': 'subject_set.namespace',
                    'subject_set_object': 'subject_set.object',
                    'subject_set_relation': 'subject_set.relation',
                },
                'location_map': {
                    'namespace': 'query',
                    'object': 'query',
                    'relation': 'query',
                    'subject_id': 'query',
                    'subject_set_namespace': 'query',
                    'subject_set_object': 'query',
                    'subject_set_relation': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_relationships_endpoint = _Endpoint(
            settings={
                'response_type': (Relationships,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples',
                'operation_id': 'get_relationships',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page_token',
                    'page_size',
                    'namespace',
                    'object',
                    'relation',
                    'subject_id',
                    'subject_set_namespace',
                    'subject_set_object',
                    'subject_set_relation',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page_token':
                        (str,),
                    'page_size':
                        (int,),
                    'namespace':
                        (str,),
                    'object':
                        (str,),
                    'relation':
                        (str,),
                    'subject_id':
                        (str,),
                    'subject_set_namespace':
                        (str,),
                    'subject_set_object':
                        (str,),
                    'subject_set_relation':
                        (str,),
                },
                'attribute_map': {
                    'page_token': 'page_token',
                    'page_size': 'page_size',
                    'namespace': 'namespace',
                    'object': 'object',
                    'relation': 'relation',
                    'subject_id': 'subject_id',
                    'subject_set_namespace': 'subject_set.namespace',
                    'subject_set_object': 'subject_set.object',
                    'subject_set_relation': 'subject_set.relation',
                },
                'location_map': {
                    'page_token': 'query',
                    'page_size': 'query',
                    'namespace': 'query',
                    'object': 'query',
                    'relation': 'query',
                    'subject_id': 'query',
                    'subject_set_namespace': 'query',
                    'subject_set_object': 'query',
                    'subject_set_relation': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_relationship_namespaces_endpoint = _Endpoint(
            settings={
                'response_type': (RelationshipNamespaces,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/namespaces',
                'operation_id': 'list_relationship_namespaces',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.patch_relationships_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'patch_relationships',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'relationship_patch',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'relationship_patch':
                        ([RelationshipPatch],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'relationship_patch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def check_opl_syntax(
        self,
        **kwargs
    ):
        """Check the syntax of an OPL file  # noqa: E501

        The OPL file is expected in the body of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_opl_syntax(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CheckOplSyntaxResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.check_opl_syntax_endpoint.call_with_http_info(**kwargs)

    def create_relationship(
        self,
        **kwargs
    ):
        """Create a Relationship  # noqa: E501

        Use this endpoint to create a relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_relationship(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_relationship_body (CreateRelationshipBody): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Relationship
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.create_relationship_endpoint.call_with_http_info(**kwargs)

    def delete_relationships(
        self,
        **kwargs
    ):
        """Delete Relationships  # noqa: E501

        Use this endpoint to delete relationships  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_relationships(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            namespace (str): Namespace of the Relationship. [optional]
            object (str): Object of the Relationship. [optional]
            relation (str): Relation of the Relationship. [optional]
            subject_id (str): SubjectID of the Relationship. [optional]
            subject_set_namespace (str): Namespace of the Subject Set. [optional]
            subject_set_object (str): Object of the Subject Set. [optional]
            subject_set_relation (str): Relation of the Subject Set. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.delete_relationships_endpoint.call_with_http_info(**kwargs)

    def get_relationships(
        self,
        **kwargs
    ):
        """Query relationships  # noqa: E501

        Get all relationships that match the query. Only the namespace field is required.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_relationships(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page_token (str): [optional]
            page_size (int): [optional]
            namespace (str): Namespace of the Relationship. [optional]
            object (str): Object of the Relationship. [optional]
            relation (str): Relation of the Relationship. [optional]
            subject_id (str): SubjectID of the Relationship. [optional]
            subject_set_namespace (str): Namespace of the Subject Set. [optional]
            subject_set_object (str): Object of the Subject Set. [optional]
            subject_set_relation (str): Relation of the Subject Set. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Relationships
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_relationships_endpoint.call_with_http_info(**kwargs)

    def list_relationship_namespaces(
        self,
        **kwargs
    ):
        """Query namespaces  # noqa: E501

        Get all namespaces  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_relationship_namespaces(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            RelationshipNamespaces
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.list_relationship_namespaces_endpoint.call_with_http_info(**kwargs)

    def patch_relationships(
        self,
        **kwargs
    ):
        """Patch Multiple Relationships  # noqa: E501

        Use this endpoint to patch one or more relationships.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_relationships(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            relationship_patch ([RelationshipPatch]): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.patch_relationships_endpoint.call_with_http_info(**kwargs)

