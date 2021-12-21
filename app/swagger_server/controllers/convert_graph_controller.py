import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.rdf_data_format_type import RDFDataFormatType  # noqa: E501
from swagger_server import util


def convert_graph(access_token, user_id, rdf_source_format, rdf_output_format, source_graph_name, output_graph_name, query, body=None):  # noqa: E501
    """convert RDF graph data source in-between RDF Format

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param rdf_source_format: the source dataset data format type, e.g., JSON-LD, RDF/XML, N3, Turtle.
    :type rdf_source_format: dict | bytes
    :param rdf_output_format: the output dataset data format type, e.g., JSON-LD, RDF/XML, N3, Turtle.
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
