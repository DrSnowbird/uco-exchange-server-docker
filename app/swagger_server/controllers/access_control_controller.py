import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
from swagger_server.models.results import Results  # noqa: E501
from swagger_server import util


def access_create(access_token, user_id, graph_uri, access_control, body=None, organization_id=None, reference=None):  # noqa: E501
    """upload and create a new RDF graph upload RDF graph data source

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri: 
    :type graph_uri: str
    :param access_control: the access control record (object)
    :type access_control: str
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


def access_delete(access_token, user_id, graph_uri, body=None, organization_id=None, reference=None):  # noqa: E501
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


def access_query(access_token, user_id, graph_uri_list, body=None, organization_id=None, reference=None):  # noqa: E501
    """Either SPARQL v1.1. RDF (Federated) Query or GraphQL (Federated) Query from multiple data sources

     # noqa: E501

    :param access_token: Authorization access token string
    :type access_token: dict | bytes
    :param user_id: the ID of the organization of the client application
    :type user_id: str
    :param graph_uri_list: 
    :type graph_uri_list: dict | bytes
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
        graph_uri_list = GraphListType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def access_update(access_token, user_id, graph_uri, body=None, organization_id=None, reference=None):  # noqa: E501
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
