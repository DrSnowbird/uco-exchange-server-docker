# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGraphqlController(BaseTestCase):
    """GraphqlController integration test stubs"""

    def test_graphql(self):
        """Test case for graphql

        GraphQL REST API
        """
        body = Object()
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_list', GraphListType()),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/graphql',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_graphql_schema_from_rdf(self):
        """Test case for graphql_schema_from_rdf

        generate GraphQL Schema (https://graphql.org/learn/schema/) using input RDF Ontology
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('source_graph_name', ''),
                        ('output_graph_name', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/graphql/schema/from-rdf',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_graphql_schema_from_rdf_uri(self):
        """Test case for graphql_schema_from_rdf_uri

        generate GraphQL Schema (https://graphql.org/learn/schema/) using input RDF Ontology in remote URI
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('source_graph_name', ''),
                        ('source_uri', ''),
                        ('output_graph_name', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/graphql/schema/from-rdf-uri',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
