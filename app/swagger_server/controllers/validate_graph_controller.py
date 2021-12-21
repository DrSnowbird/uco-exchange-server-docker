import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.rdf_data_format_type import RDFDataFormatType  # noqa: E501
from swagger_server import util


def validate_graph(access_token, user_id, graph_uri, rdf_format, body=None, organization_id=None, reference=None, standard_uri=None):  # noqa: E501
    """validate RDF graph data source for compliance

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param rdf_format: the client applications&#x27; type of this batch of RDF data to be uploaded and validated for compliance, e.g., JSON-LD, RDF/XML, N3, Turtle. Note that parsing JSON-LD mostly is much more time-consuming and expensive in computing than other formats. This API supports other data formats, e.g., N3, RDF/XML, and TURTLE
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
