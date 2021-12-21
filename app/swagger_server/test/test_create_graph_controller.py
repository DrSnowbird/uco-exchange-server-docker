# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreateGraphController(BaseTestCase):
    """CreateGraphController integration test stubs"""

    def test_create_graph(self):
        """Test case for create_graph

        upload and create a new RDF graph upload RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('rdf_format', 'JSON-LD'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.2/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()