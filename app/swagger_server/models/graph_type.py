# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.organization_type import OrganizationType  # noqa: F401,E501
from swagger_server.models.user_type import UserType  # noqa: F401,E501
from swagger_server import util


class GraphType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, organization_uuid: str='abcdabcd-1234-1234-1234-abcdefabcdef', graph_uri: str='<http://uco.example.org/bookstore>', sharable: bool=False, owner: UserType=None, organization: OrganizationType=None, date_created: datetime=None, date_expired: datetime=None):  # noqa: E501
        """GraphType - a model defined in Swagger

        :param organization_uuid: The organization_uuid of this GraphType.  # noqa: E501
        :type organization_uuid: str
        :param graph_uri: The graph_uri of this GraphType.  # noqa: E501
        :type graph_uri: str
        :param sharable: The sharable of this GraphType.  # noqa: E501
        :type sharable: bool
        :param owner: The owner of this GraphType.  # noqa: E501
        :type owner: UserType
        :param organization: The organization of this GraphType.  # noqa: E501
        :type organization: OrganizationType
        :param date_created: The date_created of this GraphType.  # noqa: E501
        :type date_created: datetime
        :param date_expired: The date_expired of this GraphType.  # noqa: E501
        :type date_expired: datetime
        """
        self.swagger_types = {
            'organization_uuid': str,
            'graph_uri': str,
            'sharable': bool,
            'owner': UserType,
            'organization': OrganizationType,
            'date_created': datetime,
            'date_expired': datetime
        }

        self.attribute_map = {
            'organization_uuid': 'organizationUUID',
            'graph_uri': 'graphURI',
            'sharable': 'sharable',
            'owner': 'owner',
            'organization': 'organization',
            'date_created': 'dateCreated',
            'date_expired': 'dateExpired'
        }
        self._organization_uuid = organization_uuid
        self._graph_uri = graph_uri
        self._sharable = sharable
        self._owner = owner
        self._organization = organization
        self._date_created = date_created
        self._date_expired = date_expired

    @classmethod
    def from_dict(cls, dikt) -> 'GraphType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GraphType of this GraphType.  # noqa: E501
        :rtype: GraphType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def organization_uuid(self) -> str:
        """Gets the organization_uuid of this GraphType.

        the UUID (v4.0) of an organization to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :return: The organization_uuid of this GraphType.
        :rtype: str
        """
        return self._organization_uuid

    @organization_uuid.setter
    def organization_uuid(self, organization_uuid: str):
        """Sets the organization_uuid of this GraphType.

        the UUID (v4.0) of an organization to be generated by the RDF Graph Exchange Server.  # noqa: E501

        :param organization_uuid: The organization_uuid of this GraphType.
        :type organization_uuid: str
        """

        self._organization_uuid = organization_uuid

    @property
    def graph_uri(self) -> str:
        """Gets the graph_uri of this GraphType.

        the URI of the RDF Graph data sources  # noqa: E501

        :return: The graph_uri of this GraphType.
        :rtype: str
        """
        return self._graph_uri

    @graph_uri.setter
    def graph_uri(self, graph_uri: str):
        """Sets the graph_uri of this GraphType.

        the URI of the RDF Graph data sources  # noqa: E501

        :param graph_uri: The graph_uri of this GraphType.
        :type graph_uri: str
        """
        if graph_uri is None:
            raise ValueError("Invalid value for `graph_uri`, must not be `None`")  # noqa: E501

        self._graph_uri = graph_uri

    @property
    def sharable(self) -> bool:
        """Gets the sharable of this GraphType.

        whether to allow the RDF graph to be shared other than the OWNER (the user who uploaded/created the RDF Graph)  # noqa: E501

        :return: The sharable of this GraphType.
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable: bool):
        """Sets the sharable of this GraphType.

        whether to allow the RDF graph to be shared other than the OWNER (the user who uploaded/created the RDF Graph)  # noqa: E501

        :param sharable: The sharable of this GraphType.
        :type sharable: bool
        """

        self._sharable = sharable

    @property
    def owner(self) -> UserType:
        """Gets the owner of this GraphType.


        :return: The owner of this GraphType.
        :rtype: UserType
        """
        return self._owner

    @owner.setter
    def owner(self, owner: UserType):
        """Sets the owner of this GraphType.


        :param owner: The owner of this GraphType.
        :type owner: UserType
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def organization(self) -> OrganizationType:
        """Gets the organization of this GraphType.


        :return: The organization of this GraphType.
        :rtype: OrganizationType
        """
        return self._organization

    @organization.setter
    def organization(self, organization: OrganizationType):
        """Sets the organization of this GraphType.


        :param organization: The organization of this GraphType.
        :type organization: OrganizationType
        """

        self._organization = organization

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this GraphType.

        date the RDF graph being uploaded/created by the user. Note this will auto-filled by the RDF Graph Exchange Server if not provided  # noqa: E501

        :return: The date_created of this GraphType.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime):
        """Sets the date_created of this GraphType.

        date the RDF graph being uploaded/created by the user. Note this will auto-filled by the RDF Graph Exchange Server if not provided  # noqa: E501

        :param date_created: The date_created of this GraphType.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_expired(self) -> datetime:
        """Gets the date_expired of this GraphType.

        date the RDF graph will be expired and removed automatically or not available for sharing. But, the owner can still access with RUD (Query, Update, Delete) operations. Note this will auto-default with, e.g., 90 days to expire, if not provided by the user.  # noqa: E501

        :return: The date_expired of this GraphType.
        :rtype: datetime
        """
        return self._date_expired

    @date_expired.setter
    def date_expired(self, date_expired: datetime):
        """Sets the date_expired of this GraphType.

        date the RDF graph will be expired and removed automatically or not available for sharing. But, the owner can still access with RUD (Query, Update, Delete) operations. Note this will auto-default with, e.g., 90 days to expire, if not provided by the user.  # noqa: E501

        :param date_expired: The date_expired of this GraphType.
        :type date_expired: datetime
        """

        self._date_expired = date_expired