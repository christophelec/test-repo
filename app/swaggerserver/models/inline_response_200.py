# coding: utf-8

from __future__ import absolute_import
from swaggerserver.models.pet_tags import PetTags
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse200(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, category: PetTags=None, name: str=None, photo_urls: List[str]=None, tags: List[PetTags]=None, status: str=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param id: The id of this InlineResponse200.
        :type id: int
        :param category: The category of this InlineResponse200.
        :type category: PetTags
        :param name: The name of this InlineResponse200.
        :type name: str
        :param photo_urls: The photo_urls of this InlineResponse200.
        :type photo_urls: List[str]
        :param tags: The tags of this InlineResponse200.
        :type tags: List[PetTags]
        :param status: The status of this InlineResponse200.
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'category': PetTags,
            'name': str,
            'photo_urls': List[str],
            'tags': List[PetTags],
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'category': 'category',
            'name': 'name',
            'photo_urls': 'photoUrls',
            'tags': 'tags',
            'status': 'status'
        }

        self._id = id
        self._category = category
        self._name = name
        self._photo_urls = photo_urls
        self._tags = tags
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.
        :rtype: InlineResponse200
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this InlineResponse200.

        :return: The id of this InlineResponse200.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this InlineResponse200.

        :param id: The id of this InlineResponse200.
        :type id: int
        """

        self._id = id

    @property
    def category(self) -> PetTags:
        """
        Gets the category of this InlineResponse200.

        :return: The category of this InlineResponse200.
        :rtype: PetTags
        """
        return self._category

    @category.setter
    def category(self, category: PetTags):
        """
        Sets the category of this InlineResponse200.

        :param category: The category of this InlineResponse200.
        :type category: PetTags
        """

        self._category = category

    @property
    def name(self) -> str:
        """
        Gets the name of this InlineResponse200.

        :return: The name of this InlineResponse200.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this InlineResponse200.

        :param name: The name of this InlineResponse200.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def photo_urls(self) -> List[str]:
        """
        Gets the photo_urls of this InlineResponse200.

        :return: The photo_urls of this InlineResponse200.
        :rtype: List[str]
        """
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, photo_urls: List[str]):
        """
        Sets the photo_urls of this InlineResponse200.

        :param photo_urls: The photo_urls of this InlineResponse200.
        :type photo_urls: List[str]
        """
        if photo_urls is None:
            raise ValueError("Invalid value for `photo_urls`, must not be `None`")

        self._photo_urls = photo_urls

    @property
    def tags(self) -> List[PetTags]:
        """
        Gets the tags of this InlineResponse200.

        :return: The tags of this InlineResponse200.
        :rtype: List[PetTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[PetTags]):
        """
        Sets the tags of this InlineResponse200.

        :param tags: The tags of this InlineResponse200.
        :type tags: List[PetTags]
        """

        self._tags = tags

    @property
    def status(self) -> str:
        """
        Gets the status of this InlineResponse200.
        pet status in the store

        :return: The status of this InlineResponse200.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """
        Sets the status of this InlineResponse200.
        pet status in the store

        :param status: The status of this InlineResponse200.
        :type status: str
        """
        allowed_values = ["available", "pending", "sold"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
