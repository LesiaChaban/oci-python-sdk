# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableRegionSummary(object):
    """
    The summary of region availability for a subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableRegionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_name:
            The value to assign to the region_name property of this AvailableRegionSummary.
        :type region_name: str

        :param system_tags:
            The value to assign to the system_tags property of this AvailableRegionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'region_name': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'region_name': 'regionName',
            'system_tags': 'systemTags'
        }

        self._region_name = None
        self._system_tags = None

    @property
    def region_name(self):
        """
        **[Required]** Gets the region_name of this AvailableRegionSummary.
        Region availability for the subscription.


        :return: The region_name of this AvailableRegionSummary.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this AvailableRegionSummary.
        Region availability for the subscription.


        :param region_name: The region_name of this AvailableRegionSummary.
        :type: str
        """
        self._region_name = region_name

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AvailableRegionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AvailableRegionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AvailableRegionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AvailableRegionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
