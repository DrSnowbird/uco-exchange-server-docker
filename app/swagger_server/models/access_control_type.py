# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.graph_access_group_type import GraphAccessGroupType  # noqa: F401,E501
from swagger_server import util


class AccessControlType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_uuid: str='None', graph_uuid: str='None', access_right: GraphAccessGroupType=None):  # noqa: E501
        """AccessControlType - a model defined in Swagger

        :param user_uuid: The user_uuid of this AccessControlType.  # noqa: E501
        :type user_uuid: str
        :param graph_uuid: The graph_uuid of this AccessControlType.  # noqa: E501
        :type graph_uuid: str
        :param access_right: The access_right of this AccessControlType.  # noqa: E501
        :type access_right: GraphAccessGroupType
        """
        self.swagger_types = {
            'user_uuid': str,
            'graph_uuid': str,
            'access_right': GraphAccessGroupType
        }

        self.attribute_map = {
            'user_uuid': 'userUUID',
            'graph_uuid': 'graphUUID',
            'access_right': 'accessRight'
        }
        self._user_uuid = user_uuid
        self._graph_uuid = graph_uuid
        self._access_right = access_right

    @classmethod
    def from_dict(cls, dikt) -> 'AccessControlType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessControlType of this AccessControlType.  # noqa: E501
        :rtype: AccessControlType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_uuid(self) -> str:
        """Gets the user_uuid of this AccessControlType.

        the UUID (v4.0) of an organization to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :return: The user_uuid of this AccessControlType.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid: str):
        """Sets the user_uuid of this AccessControlType.

        the UUID (v4.0) of an organization to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :param user_uuid: The user_uuid of this AccessControlType.
        :type user_uuid: str
        """
        if user_uuid is None:
            raise ValueError("Invalid value for `user_uuid`, must not be `None`")  # noqa: E501

        self._user_uuid = user_uuid

    @property
    def graph_uuid(self) -> str:
        """Gets the graph_uuid of this AccessControlType.

        the UUID (v4.0) of an RDF Graph to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :return: The graph_uuid of this AccessControlType.
        :rtype: str
        """
        return self._graph_uuid

    @graph_uuid.setter
    def graph_uuid(self, graph_uuid: str):
        """Sets the graph_uuid of this AccessControlType.

        the UUID (v4.0) of an RDF Graph to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :param graph_uuid: The graph_uuid of this AccessControlType.
        :type graph_uuid: str
        """

        self._graph_uuid = graph_uuid

    @property
    def access_right(self) -> GraphAccessGroupType:
        """Gets the access_right of this AccessControlType.


        :return: The access_right of this AccessControlType.
        :rtype: GraphAccessGroupType
        """
        return self._access_right

    @access_right.setter
    def access_right(self, access_right: GraphAccessGroupType):
        """Sets the access_right of this AccessControlType.


        :param access_right: The access_right of this AccessControlType.
        :type access_right: GraphAccessGroupType
        """

        self._access_right = access_right
