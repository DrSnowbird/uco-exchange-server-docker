# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccessControlController(BaseTestCase):
    """AccessControlController integration test stubs"""

    def test_access_create(self):
        """Test case for access_create

        upload and create a new RDF graph upload RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('access_control', 'JSON-LD'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/access-control/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_access_delete(self):
        """Test case for access_delete

        Delete RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/access-control/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_access_query(self):
        """Test case for access_query

        Either SPARQL v1.1. RDF (Federated) Query or GraphQL (Federated) Query from multiple data sources
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri_list', GraphListType()),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/access-control/query',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_access_update(self):
        """Test case for access_update

        update RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/access-control/update',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
