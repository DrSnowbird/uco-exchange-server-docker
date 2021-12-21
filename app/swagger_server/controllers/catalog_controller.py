import connexion
import six

from swagger_server.models.access_token import AccessToken  # noqa: E501
from swagger_server.models.errors import Errors  # noqa: E501
from swagger_server.models.graph_list_type import GraphListType  # noqa: E501
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
