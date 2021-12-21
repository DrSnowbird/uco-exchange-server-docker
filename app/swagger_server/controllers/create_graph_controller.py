import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server import util


def create_graph(access_token, user_id, graph_uri, rdf_format, body=None, organization_id=None, reference=None):  # noqa: E501
    """upload and create a new RDF graph upload RDF graph data source

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param rdf_format: the semantic graph format types, e.g., JSON-LD, RDF/XML, N3, Turtle. Note that parsing JSON-LD mostly is much more time-consuming and expensive in computing than other formats. This API supports other data formats, e.g., N3, RDF/XML, and TURTLE
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
