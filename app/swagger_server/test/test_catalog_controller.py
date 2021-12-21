# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCatalogController(BaseTestCase):
    """CatalogController integration test stubs"""

    def test_catalog(self):
        """Test case for catalog

        Query the list of all the RDF graphs' names (URIs) and the response will be JSON format.
        """
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('query', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.2/catalog',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
