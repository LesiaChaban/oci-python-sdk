# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoringTemplate(object):
    """
    Detailed information of the Monitoring Template
    """

    #: A constant which can be used with the status property of a MonitoringTemplate.
    #: This constant has a value of "NOT_APPLIED"
    STATUS_NOT_APPLIED = "NOT_APPLIED"

    #: A constant which can be used with the status property of a MonitoringTemplate.
    #: This constant has a value of "APPLIED"
    STATUS_APPLIED = "APPLIED"

    #: A constant which can be used with the status property of a MonitoringTemplate.
    #: This constant has a value of "PARTIAL_APPLIED"
    STATUS_PARTIAL_APPLIED = "PARTIAL_APPLIED"

    #: A constant which can be used with the lifecycle_state property of a MonitoringTemplate.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoringTemplate.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoringTemplate.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoringTemplate.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoringTemplate.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the message_format property of a MonitoringTemplate.
    #: This constant has a value of "RAW"
    MESSAGE_FORMAT_RAW = "RAW"

    #: A constant which can be used with the message_format property of a MonitoringTemplate.
    #: This constant has a value of "PRETTY_JSON"
    MESSAGE_FORMAT_PRETTY_JSON = "PRETTY_JSON"

    #: A constant which can be used with the message_format property of a MonitoringTemplate.
    #: This constant has a value of "ONS_OPTIMIZED"
    MESSAGE_FORMAT_ONS_OPTIMIZED = "ONS_OPTIMIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoringTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MonitoringTemplate.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MonitoringTemplate.
        :type display_name: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MonitoringTemplate.
        :type tenant_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoringTemplate.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this MonitoringTemplate.
        :type description: str

        :param status:
            The value to assign to the status property of this MonitoringTemplate.
            Allowed values for this property are: "NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoringTemplate.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param destinations:
            The value to assign to the destinations property of this MonitoringTemplate.
        :type destinations: list[str]

        :param is_alarms_enabled:
            The value to assign to the is_alarms_enabled property of this MonitoringTemplate.
        :type is_alarms_enabled: bool

        :param is_split_notification_enabled:
            The value to assign to the is_split_notification_enabled property of this MonitoringTemplate.
        :type is_split_notification_enabled: bool

        :param members:
            The value to assign to the members property of this MonitoringTemplate.
        :type members: list[oci.stack_monitoring.models.MemberReference]

        :param repeat_notification_duration:
            The value to assign to the repeat_notification_duration property of this MonitoringTemplate.
        :type repeat_notification_duration: str

        :param message_format:
            The value to assign to the message_format property of this MonitoringTemplate.
            Allowed values for this property are: "RAW", "PRETTY_JSON", "ONS_OPTIMIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type message_format: str

        :param total_alarm_conditions:
            The value to assign to the total_alarm_conditions property of this MonitoringTemplate.
        :type total_alarm_conditions: float

        :param total_applied_alarm_conditions:
            The value to assign to the total_applied_alarm_conditions property of this MonitoringTemplate.
        :type total_applied_alarm_conditions: float

        :param time_created:
            The value to assign to the time_created property of this MonitoringTemplate.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoringTemplate.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoringTemplate.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoringTemplate.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoringTemplate.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'tenant_id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'destinations': 'list[str]',
            'is_alarms_enabled': 'bool',
            'is_split_notification_enabled': 'bool',
            'members': 'list[MemberReference]',
            'repeat_notification_duration': 'str',
            'message_format': 'str',
            'total_alarm_conditions': 'float',
            'total_applied_alarm_conditions': 'float',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'tenant_id': 'tenantId',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'destinations': 'destinations',
            'is_alarms_enabled': 'isAlarmsEnabled',
            'is_split_notification_enabled': 'isSplitNotificationEnabled',
            'members': 'members',
            'repeat_notification_duration': 'repeatNotificationDuration',
            'message_format': 'messageFormat',
            'total_alarm_conditions': 'totalAlarmConditions',
            'total_applied_alarm_conditions': 'totalAppliedAlarmConditions',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._tenant_id = None
        self._compartment_id = None
        self._description = None
        self._status = None
        self._lifecycle_state = None
        self._destinations = None
        self._is_alarms_enabled = None
        self._is_split_notification_enabled = None
        self._members = None
        self._repeat_notification_duration = None
        self._message_format = None
        self._total_alarm_conditions = None
        self._total_applied_alarm_conditions = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MonitoringTemplate.
        The `OCID`__ of the monitoringTemplate

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MonitoringTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MonitoringTemplate.
        The `OCID`__ of the monitoringTemplate

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MonitoringTemplate.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MonitoringTemplate.
        A user-friendly name for the monitoring template. It should be unique, and it's mutable in nature. Avoid entering confidential information.


        :return: The display_name of this MonitoringTemplate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoringTemplate.
        A user-friendly name for the monitoring template. It should be unique, and it's mutable in nature. Avoid entering confidential information.


        :param display_name: The display_name of this MonitoringTemplate.
        :type: str
        """
        self._display_name = display_name

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MonitoringTemplate.
        Tenant Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this MonitoringTemplate.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MonitoringTemplate.
        Tenant Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this MonitoringTemplate.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoringTemplate.
        The OCID of the compartment containing the monitoringTemplate.


        :return: The compartment_id of this MonitoringTemplate.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoringTemplate.
        The OCID of the compartment containing the monitoringTemplate.


        :param compartment_id: The compartment_id of this MonitoringTemplate.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this MonitoringTemplate.
        A user-friendly description for the monitoring template. It does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The description of this MonitoringTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MonitoringTemplate.
        A user-friendly description for the monitoring template. It does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param description: The description of this MonitoringTemplate.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """
        **[Required]** Gets the status of this MonitoringTemplate.
        The current status of the monitoring template i.e. whether it is Applied or NotApplied.

        Allowed values for this property are: "NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this MonitoringTemplate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MonitoringTemplate.
        The current status of the monitoring template i.e. whether it is Applied or NotApplied.


        :param status: The status of this MonitoringTemplate.
        :type: str
        """
        allowed_values = ["NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MonitoringTemplate.
        The current lifecycle state of the monitoring template.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoringTemplate.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoringTemplate.
        The current lifecycle state of the monitoring template.


        :param lifecycle_state: The lifecycle_state of this MonitoringTemplate.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def destinations(self):
        """
        **[Required]** Gets the destinations of this MonitoringTemplate.
        A list of destinations for alarm notifications. Each destination is represented by the OCID of a related resource.


        :return: The destinations of this MonitoringTemplate.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this MonitoringTemplate.
        A list of destinations for alarm notifications. Each destination is represented by the OCID of a related resource.


        :param destinations: The destinations of this MonitoringTemplate.
        :type: list[str]
        """
        self._destinations = destinations

    @property
    def is_alarms_enabled(self):
        """
        Gets the is_alarms_enabled of this MonitoringTemplate.
        Whether the alarm is enabled or disabled. Default value is enabled.


        :return: The is_alarms_enabled of this MonitoringTemplate.
        :rtype: bool
        """
        return self._is_alarms_enabled

    @is_alarms_enabled.setter
    def is_alarms_enabled(self, is_alarms_enabled):
        """
        Sets the is_alarms_enabled of this MonitoringTemplate.
        Whether the alarm is enabled or disabled. Default value is enabled.


        :param is_alarms_enabled: The is_alarms_enabled of this MonitoringTemplate.
        :type: bool
        """
        self._is_alarms_enabled = is_alarms_enabled

    @property
    def is_split_notification_enabled(self):
        """
        Gets the is_split_notification_enabled of this MonitoringTemplate.
        Whether the alarm notification is enabled or disabled, it will be Enabled by default.


        :return: The is_split_notification_enabled of this MonitoringTemplate.
        :rtype: bool
        """
        return self._is_split_notification_enabled

    @is_split_notification_enabled.setter
    def is_split_notification_enabled(self, is_split_notification_enabled):
        """
        Sets the is_split_notification_enabled of this MonitoringTemplate.
        Whether the alarm notification is enabled or disabled, it will be Enabled by default.


        :param is_split_notification_enabled: The is_split_notification_enabled of this MonitoringTemplate.
        :type: bool
        """
        self._is_split_notification_enabled = is_split_notification_enabled

    @property
    def members(self):
        """
        **[Required]** Gets the members of this MonitoringTemplate.
        List of members of this monitoring template.


        :return: The members of this MonitoringTemplate.
        :rtype: list[oci.stack_monitoring.models.MemberReference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this MonitoringTemplate.
        List of members of this monitoring template.


        :param members: The members of this MonitoringTemplate.
        :type: list[oci.stack_monitoring.models.MemberReference]
        """
        self._members = members

    @property
    def repeat_notification_duration(self):
        """
        Gets the repeat_notification_duration of this MonitoringTemplate.
        The frequency for re-submitting alarm notifications, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, PT4H indicates four hours. Minimum- PT1M. Maximum - P30D.


        :return: The repeat_notification_duration of this MonitoringTemplate.
        :rtype: str
        """
        return self._repeat_notification_duration

    @repeat_notification_duration.setter
    def repeat_notification_duration(self, repeat_notification_duration):
        """
        Sets the repeat_notification_duration of this MonitoringTemplate.
        The frequency for re-submitting alarm notifications, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, PT4H indicates four hours. Minimum- PT1M. Maximum - P30D.


        :param repeat_notification_duration: The repeat_notification_duration of this MonitoringTemplate.
        :type: str
        """
        self._repeat_notification_duration = repeat_notification_duration

    @property
    def message_format(self):
        """
        Gets the message_format of this MonitoringTemplate.
        The format to use for alarm notifications.

        Allowed values for this property are: "RAW", "PRETTY_JSON", "ONS_OPTIMIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The message_format of this MonitoringTemplate.
        :rtype: str
        """
        return self._message_format

    @message_format.setter
    def message_format(self, message_format):
        """
        Sets the message_format of this MonitoringTemplate.
        The format to use for alarm notifications.


        :param message_format: The message_format of this MonitoringTemplate.
        :type: str
        """
        allowed_values = ["RAW", "PRETTY_JSON", "ONS_OPTIMIZED"]
        if not value_allowed_none_or_none_sentinel(message_format, allowed_values):
            message_format = 'UNKNOWN_ENUM_VALUE'
        self._message_format = message_format

    @property
    def total_alarm_conditions(self):
        """
        **[Required]** Gets the total_alarm_conditions of this MonitoringTemplate.
        Total Alarm Conditions


        :return: The total_alarm_conditions of this MonitoringTemplate.
        :rtype: float
        """
        return self._total_alarm_conditions

    @total_alarm_conditions.setter
    def total_alarm_conditions(self, total_alarm_conditions):
        """
        Sets the total_alarm_conditions of this MonitoringTemplate.
        Total Alarm Conditions


        :param total_alarm_conditions: The total_alarm_conditions of this MonitoringTemplate.
        :type: float
        """
        self._total_alarm_conditions = total_alarm_conditions

    @property
    def total_applied_alarm_conditions(self):
        """
        **[Required]** Gets the total_applied_alarm_conditions of this MonitoringTemplate.
        Total Applied Alarm Conditions


        :return: The total_applied_alarm_conditions of this MonitoringTemplate.
        :rtype: float
        """
        return self._total_applied_alarm_conditions

    @total_applied_alarm_conditions.setter
    def total_applied_alarm_conditions(self, total_applied_alarm_conditions):
        """
        Sets the total_applied_alarm_conditions of this MonitoringTemplate.
        Total Applied Alarm Conditions


        :param total_applied_alarm_conditions: The total_applied_alarm_conditions of this MonitoringTemplate.
        :type: float
        """
        self._total_applied_alarm_conditions = total_applied_alarm_conditions

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MonitoringTemplate.
        The date and time the monitoringTemplate was created. Format defined by RFC3339.


        :return: The time_created of this MonitoringTemplate.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoringTemplate.
        The date and time the monitoringTemplate was created. Format defined by RFC3339.


        :param time_created: The time_created of this MonitoringTemplate.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this MonitoringTemplate.
        The date and time the monitoringTemplate was last updated. Format defined by RFC3339.


        :return: The time_updated of this MonitoringTemplate.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoringTemplate.
        The date and time the monitoringTemplate was last updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this MonitoringTemplate.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoringTemplate.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoringTemplate.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoringTemplate.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoringTemplate.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoringTemplate.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoringTemplate.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoringTemplate.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoringTemplate.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoringTemplate.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoringTemplate.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoringTemplate.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoringTemplate.
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
