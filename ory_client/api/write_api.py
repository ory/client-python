"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.183
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
from ory_client.model.generic_error import GenericError
from ory_client.model.patch_delta import PatchDelta
from ory_client.model.relation_query import RelationQuery


class WriteApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_relation_tuple_endpoint = _Endpoint(
            settings={
                'response_type': (RelationQuery,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'create_relation_tuple',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'relation_query',
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
                    'relation_query':
                        (RelationQuery,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'relation_query': 'body',
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
        self.delete_relation_tuples_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'delete_relation_tuples',
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
        self.patch_relation_tuples_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/admin/relation-tuples',
                'operation_id': 'patch_relation_tuples',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'patch_delta',
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
                    'patch_delta':
                        ([PatchDelta],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'patch_delta': 'body',
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

    def create_relation_tuple(
        self,
        **kwargs
    ):
        """Create a Relation Tuple  # noqa: E501

        Use this endpoint to create a relation tuple.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_relation_tuple(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            relation_query (RelationQuery): [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            RelationQuery
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
        return self.create_relation_tuple_endpoint.call_with_http_info(**kwargs)

    def delete_relation_tuples(
        self,
        **kwargs
    ):
        """Delete Relation Tuples  # noqa: E501

        Use this endpoint to delete relation tuples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_relation_tuples(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            namespace (str): Namespace of the Relation Tuple. [optional]
            object (str): Object of the Relation Tuple. [optional]
            relation (str): Relation of the Relation Tuple. [optional]
            subject_id (str): SubjectID of the Relation Tuple. [optional]
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
        return self.delete_relation_tuples_endpoint.call_with_http_info(**kwargs)

    def patch_relation_tuples(
        self,
        **kwargs
    ):
        """Patch Multiple Relation Tuples  # noqa: E501

        Use this endpoint to patch one or more relation tuples.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_relation_tuples(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            patch_delta ([PatchDelta]): [optional]
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
        return self.patch_relation_tuples_endpoint.call_with_http_info(**kwargs)

