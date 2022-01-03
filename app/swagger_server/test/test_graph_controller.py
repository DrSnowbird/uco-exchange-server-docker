# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.models.rdf_data_format_type import RDFDataFormatType  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGraphController(BaseTestCase):
    """GraphController integration test stubs"""

    def test_catalog(self):
        """Test case for catalog

        Query the list of all the RDF graphs' names (URIs) and the response will be JSON format.
        """
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('query', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/catalog',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_convert_graph(self):
        """Test case for convert_graph

        convert RDF graph data source in-between RDF Format
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('rdf_source_format', RDFDataFormatType()),
                        ('rdf_output_format', RDFDataFormatType()),
                        ('source_graph_name', ''),
                        ('output_graph_name', ''),
                        ('query', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/convert',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_graph(self):
        """Test case for delete_graph

        Delete RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_query_graph(self):
        """Test case for query_graph

        Either SPARQL v1.1. RDF (Federated) Query or GraphQL (Federated) Query from multiple data sources
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_list', GraphListType()),
                        ('organization_id', 'organizationID-unknown'),
                        ('query_type', 'query_type_example'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/query',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shacl_generate(self):
        """Test case for shacl_generate

        Build SHACL shapes from an ontology document, supported formats: Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('rdf_source_format', RDFDataFormatType()),
                        ('shacl_output_format', RDFDataFormatType()),
                        ('source_graph_name', ''),
                        ('output_graph_name', '')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/shacl-generate',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_graph(self):
        """Test case for update_graph

        update RDF graph data source
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a')]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/update',
            method='POST',
            data=json.dumps(body),
            content_type='application/text',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_graph(self):
        """Test case for validate_graph

        validate RDF graph data source for compliance
        """
        body = 'body_example'
        query_string = [('access_token', AccessToken()),
                        ('user_id', 'userUUID-unknown'),
                        ('graph_uri', '<http://uco.example.org/bookstore>'),
                        ('organization_id', 'organizationID-unknown'),
                        ('reference', 'n/a'),
                        ('standard_uri', 'unknown'),
                        ('rdf_format', RDFDataFormatType())]
        response = self.client.open(
            '/RS-API/RDF-Graph-Exchange/0.1.3/api/graph/validate',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
