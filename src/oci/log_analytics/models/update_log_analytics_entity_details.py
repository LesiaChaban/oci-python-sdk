# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLogAnalyticsEntityDetails(object):
    """
    Details of log analytics entity to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLogAnalyticsEntityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateLogAnalyticsEntityDetails.
        :type name: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this UpdateLogAnalyticsEntityDetails.
        :type management_agent_id: str

        :param timezone_region:
            The value to assign to the timezone_region property of this UpdateLogAnalyticsEntityDetails.
        :type timezone_region: str

        :param hostname:
            The value to assign to the hostname property of this UpdateLogAnalyticsEntityDetails.
        :type hostname: str

        :param properties:
            The value to assign to the properties property of this UpdateLogAnalyticsEntityDetails.
        :type properties: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLogAnalyticsEntityDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLogAnalyticsEntityDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'management_agent_id': 'str',
            'timezone_region': 'str',
            'hostname': 'str',
            'properties': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'management_agent_id': 'managementAgentId',
            'timezone_region': 'timezoneRegion',
            'hostname': 'hostname',
            'properties': 'properties',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._management_agent_id = None
        self._timezone_region = None
        self._hostname = None
        self._properties = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        Gets the name of this UpdateLogAnalyticsEntityDetails.
        Log analytics entity name.


        :return: The name of this UpdateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateLogAnalyticsEntityDetails.
        Log analytics entity name.


        :param name: The name of this UpdateLogAnalyticsEntityDetails.
        :type: str
        """
        self._name = name

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this UpdateLogAnalyticsEntityDetails.
        The OCID of the Management Agent.


        :return: The management_agent_id of this UpdateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this UpdateLogAnalyticsEntityDetails.
        The OCID of the Management Agent.


        :param management_agent_id: The management_agent_id of this UpdateLogAnalyticsEntityDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def timezone_region(self):
        """
        Gets the timezone_region of this UpdateLogAnalyticsEntityDetails.
        The timezone region of the log analytics entity.


        :return: The timezone_region of this UpdateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._timezone_region

    @timezone_region.setter
    def timezone_region(self, timezone_region):
        """
        Sets the timezone_region of this UpdateLogAnalyticsEntityDetails.
        The timezone region of the log analytics entity.


        :param timezone_region: The timezone_region of this UpdateLogAnalyticsEntityDetails.
        :type: str
        """
        self._timezone_region = timezone_region

    @property
    def hostname(self):
        """
        Gets the hostname of this UpdateLogAnalyticsEntityDetails.
        The hostname where the entity represented here is actually present. This would be the output one would get if
        they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
        management agents host since logs may be collected remotely.


        :return: The hostname of this UpdateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this UpdateLogAnalyticsEntityDetails.
        The hostname where the entity represented here is actually present. This would be the output one would get if
        they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
        management agents host since logs may be collected remotely.


        :param hostname: The hostname of this UpdateLogAnalyticsEntityDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def properties(self):
        """
        Gets the properties of this UpdateLogAnalyticsEntityDetails.
        The name/value pairs for parameter values to be used in file patterns specified in log sources.


        :return: The properties of this UpdateLogAnalyticsEntityDetails.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateLogAnalyticsEntityDetails.
        The name/value pairs for parameter values to be used in file patterns specified in log sources.


        :param properties: The properties of this UpdateLogAnalyticsEntityDetails.
        :type: dict(str, str)
        """
        self._properties = properties

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateLogAnalyticsEntityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateLogAnalyticsEntityDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateLogAnalyticsEntityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateLogAnalyticsEntityDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateLogAnalyticsEntityDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateLogAnalyticsEntityDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateLogAnalyticsEntityDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateLogAnalyticsEntityDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
