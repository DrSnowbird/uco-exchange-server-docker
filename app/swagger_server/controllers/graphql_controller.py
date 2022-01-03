import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server import util


def graphql(access_token, user_id, body=None, graph_list=None, organization_id=None, reference=None):  # noqa: E501
    """GraphQL REST API

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param body: GraphQL query.
    :type body: dict | bytes
    :param graph_list: Either SPARQL or GraphQL query is supported
    :type graph_list: dict | bytes
    :param organization_id: the organization of the client application
    :type organization_id: str
    :param reference: the client applications&#x27; reference to this batch of RDF data to be uploaded and it is not used by the Server.
    :type reference: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        graph_list = GraphListType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def graphql_schema_from_rdf(access_token, user_id, output_graph_name, body=None, source_graph_name=None):  # noqa: E501
    """generate GraphQL Schema (https://graphql.org/learn/schema/) using input RDF Ontology

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param output_graph_name: the new Graph Name for generating GraphQL schema. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF graph and &#x27;default&#x27; graph will be used. If both sourceGraphName and outputGraphName are null or empty, then the entire source default graph will be used as input for conversion and the output will have no named-graph.
    :type output_graph_name: str
    :param body: RDF ontology dataset in supported formats, e.g. Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type body: dict | bytes
    :param source_graph_name: the sourece Graph Name for generating the converted RDF Graph. If null or emply, then the entire DEFAULT RDF tuples will be used to generate the target named-Graph as defined in &#x27;outputGraphname&#x27;. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF (default) graph.
    :type source_graph_name: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def graphql_schema_from_rdf_uri(access_token, user_id, source_uri, body=None, source_graph_name=None, output_graph_name=None):  # noqa: E501
    """generate GraphQL Schema (https://graphql.org/learn/schema/) using input RDF Ontology in remote URI

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param source_uri: the source RDF dataset URI, e.g., https://student.university-rdf-example.org.
    :type source_uri: str
    :param body: RDF ontology dataset in supported formats, e.g. Turtle, RDF/XML, N-Triples, JSON-LD, RDF/JSON, TriG, N-Quads, TriX.
    :type body: dict | bytes
    :param source_graph_name: the sourece Graph Name for generating the converted RDF Graph. If null or emply, then the entire DEFAULT RDF tuples will be used to generate the target named-Graph as defined in &#x27;outputGraphname&#x27;. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF (default) graph.
    :type source_graph_name: str
    :param output_graph_name: the new Graph Name for generating GraphQL schema. If the &#x27;outputGraphName&#x27; is null or empty, then no named-Graph name will be used for the converted RDF graph and &#x27;default&#x27; graph will be used. If both sourceGraphName and outputGraphName are null or empty, then the entire source default graph will be used as input for conversion and the output will have no named-graph.
    :type output_graph_name: str

    :rtype: str
    """
    if connexion.request.is_json:
        access_token = AccessToken.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
