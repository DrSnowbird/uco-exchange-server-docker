import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.models.rdf_data_format_type import RDFDataFormatType  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server import util


def catalog(access_token, user_id, query=None):  # noqa: E501
    """Query the list of all the RDF graphs&#x27; names (URIs) and the response will be JSON format.

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param query: Query GraphsSPARQL Query expression (max 1536). Note the common lowest limit for the entrie url is 2048 as the limit. The query SPARQL string must be url-encoded. The example below is not url-encoded to show the un-encoded SPARQL content.
    :type query: str

    :rtype: GraphListType
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def convert_graph(access_token, user_id, rdf_source_format, rdf_output_format, source_graph_name, output_graph_name, query, body=None):  # noqa: E501
    """convert RDF graph data source in-between RDF Format

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param rdf_source_format: the source dataset data format type, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type rdf_source_format: dict | bytes
    :param rdf_output_format: the output dataset data format type, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type rdf_output_format: dict | bytes
    :param source_graph_name: the sourece Graph Name for generating the converted RDF Graph. If null or emply, then the entire DEFAULT RDF tuples will be used to generate the target named-Graph as defined in &#x27;outputGraphname&#x27;. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF (default) graph.
    :type source_graph_name: str
    :param output_graph_name: the new Graph Name for rdfOutput. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF graph and &#x27;default&#x27; graph will be used. If both sourceGraphName and outputGraphName are null or empty, then the entire source default graph will be used as input for conversion and the output will have no named-graph.
    :type output_graph_name: str
    :param query: SPARQL Query expression (max 1536). Note the common lowest limit for the entrie url is 2048 as the limit. The query SPARQL string must be url-encoded. The example below is not url-encoded to show the un-encoded SPARQL content. If the query is provided with named-graph(s), then these named-graph will be used and ignore the &#x27;sourceGraphName&#x27; parameter
    :type query: str
    :param body: SPARQL v1.1 (see W3C SPARQL v1.1. Update Specification - https://www.w3.org/TR/sparql11-update/ ) as the specification syntax of the payload SPARQL Update statements.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        rdf_source_format = RDFDataFormatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        rdf_output_format = RDFDataFormatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_graph(access_token, user_id, graph_uri, rdf_format, body=None, organization_id=None, reference=None):  # noqa: E501
    """upload and create a new RDF graph upload RDF graph data source

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param rdf_format: the semantic graph format types, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX. Note that parsing JSON-LD mostly is much more time-consuming and expensive in computing than other formats. This API supports other data formats, e.g., N3, RDF/XML, and TURTLE
    :type rdf_format: str
    :param body: upload RDF data source
    :type body: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_graph(access_token, user_id, graph_uri, body=None, organization_id=None, reference=None):  # noqa: E501
    """Delete RDF graph data source

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param body: More specifics about what RDF data to delete using SPARQL &#x27;DELETE DATA&#x27; statement. Note the Client can only delete the original Graph data sources being uploaded by the same User ID and Graph name. These graphs uploaded by others will not be deleted by the request as the protection by the ownership of those other graphs.
    :type body: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def query_graph(access_token, user_id, body=None, graph_list=None, organization_id=None, query_type=None, reference=None):  # noqa: E501
    """Either SPARQL v1.1. RDF (Federated) Query or GraphQL (Federated) Query from multiple data sources

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param body: More specifics about what RDF data to delete using SPARQL &#x27;DELETE DATA&#x27; statement. Note the Client can only delete the original Graph data sources being uploaded by the same User ID and Graph name. These graphs uploaded by others will not be deleted by the request as the protection by the ownership of those other graphs.
    :type body: dict | bytes
    :param graph_list: Either SPARQL or GraphQL query is supported
    :type graph_list: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param query_type: Either SPARQL or GraphQL query is supported
    :type query_type: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        graph_list = GraphListType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def shacl_generate(access_token, user_id, rdf_source_format, shacl_output_format, source_graph_name, output_graph_name, body=None):  # noqa: E501
    """Build SHACL shapes from an ontology document, supported formats: Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param rdf_source_format: the source dataset data format type, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type rdf_source_format: dict | bytes
    :param shacl_output_format: the output dataset data format type, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type shacl_output_format: dict | bytes
    :param source_graph_name: the sourece Graph Name for generating the converted RDF Graph. If null or emply, then the entire DEFAULT RDF tuples will be used to generate the target named-Graph as defined in &#x27;outputGraphname&#x27;. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF (default) graph.
    :type source_graph_name: str
    :param output_graph_name: the new Graph Name for rdfOutput. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF graph and &#x27;default&#x27; graph will be used. If both sourceGraphName and outputGraphName are null or empty, then the entire source default graph will be used as input for conversion and the output will have no named-graph.
    :type output_graph_name: str
    :param body: SPARQL v1.1 (see W3C SPARQL v1.1. Update Specification - https://www.w3.org/TR/sparql11-update/ ) as the specification syntax of the payload SPARQL Update statements.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        rdf_source_format = RDFDataFormatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        shacl_output_format = RDFDataFormatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_graph(access_token, user_id, graph_uri, body=None, organization_id=None, reference=None):  # noqa: E501
    """update RDF graph data source

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param body: SPARQL v1.1 (see W3C SPARQL v1.1. Update Specification - https://www.w3.org/TR/sparql11-update/ ) as the specification syntax of the payload SPARQL Update statements.
    :type body: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str

    :rtype: Results
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def validate_graph(access_token, user_id, graph_uri, rdf_format, body=None, organization_id=None, reference=None, standard_uri=None):  # noqa: E501
    """validate RDF graph data source for compliance

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param rdf_format: the client applications&#x27; type of this batch of RDF data to be uploaded and validated for compliance, e.g., Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX. Note that parsing JSON-LD mostly is much more time-consuming and expensive in computing than other formats. This API supports other data formats, e.g., N3, RDF/XML, and TURTLE
    :type rdf_format: dict | bytes
    :param body: SPARQL v1.1 (see W3C SPARQL v1.1. Update Specification - https://www.w3.org/TR/sparql11-update/ ) as the specification syntax of the payload SPARQL Update statements.
    :type body: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str
    :param standard_uri: the client applications&#x27; compliance-standard URI for this batch of RDF data to be uploaded and validated for compliance. For example, the URI of UCO SHACL shape Turtle file.
    :type standard_uri: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        rdf_format = RDFDataFormatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
