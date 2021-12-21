# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatusController(BaseTestCase):
    """StatusController integration test stubs"""

    def test_status(self):
        """Test case for status

        Server heartbeat operation
        """
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.2/status',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
