# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceTypeSummary(object):
    """
    The summary of monitored resource type.
    """

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "SM_MGMT_AGENT_MONITORED"
    SOURCE_TYPE_SM_MGMT_AGENT_MONITORED = "SM_MGMT_AGENT_MONITORED"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "SM_REPO_ONLY"
    SOURCE_TYPE_SM_REPO_ONLY = "SM_REPO_ONLY"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "OCI_NATIVE"
    SOURCE_TYPE_OCI_NATIVE = "OCI_NATIVE"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "PROMETHEUS"
    SOURCE_TYPE_PROMETHEUS = "PROMETHEUS"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "TELEGRAF"
    SOURCE_TYPE_TELEGRAF = "TELEGRAF"

    #: A constant which can be used with the source_type property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "COLLECTD"
    SOURCE_TYPE_COLLECTD = "COLLECTD"

    #: A constant which can be used with the resource_category property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "APPLICATION"
    RESOURCE_CATEGORY_APPLICATION = "APPLICATION"

    #: A constant which can be used with the resource_category property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "DATABASE"
    RESOURCE_CATEGORY_DATABASE = "DATABASE"

    #: A constant which can be used with the resource_category property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "MIDDLEWARE"
    RESOURCE_CATEGORY_MIDDLEWARE = "MIDDLEWARE"

    #: A constant which can be used with the resource_category property of a MonitoredResourceTypeSummary.
    #: This constant has a value of "UNKNOWN"
    RESOURCE_CATEGORY_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MonitoredResourceTypeSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this MonitoredResourceTypeSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this MonitoredResourceTypeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MonitoredResourceTypeSummary.
        :type description: str

        :param metric_namespace:
            The value to assign to the metric_namespace property of this MonitoredResourceTypeSummary.
        :type metric_namespace: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredResourceTypeSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredResourceTypeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param source_type:
            The value to assign to the source_type property of this MonitoredResourceTypeSummary.
            Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param resource_category:
            The value to assign to the resource_category property of this MonitoredResourceTypeSummary.
            Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_category: str

        :param metadata:
            The value to assign to the metadata property of this MonitoredResourceTypeSummary.
        :type metadata: oci.stack_monitoring.models.ResourceTypeMetadataDetails

        :param additional_namespace_map:
            The value to assign to the additional_namespace_map property of this MonitoredResourceTypeSummary.
        :type additional_namespace_map: dict(str, str)

        :param time_created:
            The value to assign to the time_created property of this MonitoredResourceTypeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoredResourceTypeSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResourceTypeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResourceTypeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResourceTypeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'metric_namespace': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'source_type': 'str',
            'resource_category': 'str',
            'metadata': 'ResourceTypeMetadataDetails',
            'additional_namespace_map': 'dict(str, str)',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'metric_namespace': 'metricNamespace',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'source_type': 'sourceType',
            'resource_category': 'resourceCategory',
            'metadata': 'metadata',
            'additional_namespace_map': 'additionalNamespaceMap',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._metric_namespace = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._source_type = None
        self._resource_category = None
        self._metadata = None
        self._additional_namespace_map = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MonitoredResourceTypeSummary.
        Monitored resource type identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MonitoredResourceTypeSummary.
        Monitored resource type identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MonitoredResourceTypeSummary.
        A unique monitored resource type name. The name must be unique across tenancy.
        Name can not be changed.


        :return: The name of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResourceTypeSummary.
        A unique monitored resource type name. The name must be unique across tenancy.
        Name can not be changed.


        :param name: The name of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this MonitoredResourceTypeSummary.
        Monitored resource type display name.


        :return: The display_name of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoredResourceTypeSummary.
        Monitored resource type display name.


        :param display_name: The display_name of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this MonitoredResourceTypeSummary.
        A friendly description.


        :return: The description of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MonitoredResourceTypeSummary.
        A friendly description.


        :param description: The description of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._description = description

    @property
    def metric_namespace(self):
        """
        Gets the metric_namespace of this MonitoredResourceTypeSummary.
        Metric namespace for resource type.


        :return: The metric_namespace of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        """
        Sets the metric_namespace of this MonitoredResourceTypeSummary.
        Metric namespace for resource type.


        :param metric_namespace: The metric_namespace of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._metric_namespace = metric_namespace

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredResourceTypeSummary.
        The `OCID`__ of the tenancy containing the resource type.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredResourceTypeSummary.
        The `OCID`__ of the tenancy containing the resource type.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredResourceTypeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredResourceTypeSummary.
        Lifecycle state of the monitored resource type.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredResourceTypeSummary.
        Lifecycle state of the monitored resource type.


        :param lifecycle_state: The lifecycle_state of this MonitoredResourceTypeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def source_type(self):
        """
        Gets the source_type of this MonitoredResourceTypeSummary.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.

        Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this MonitoredResourceTypeSummary.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.


        :param source_type: The source_type of this MonitoredResourceTypeSummary.
        :type: str
        """
        allowed_values = ["SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def resource_category(self):
        """
        Gets the resource_category of this MonitoredResourceTypeSummary.
        Resource Category to indicate the kind of resource type.

        Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_category of this MonitoredResourceTypeSummary.
        :rtype: str
        """
        return self._resource_category

    @resource_category.setter
    def resource_category(self, resource_category):
        """
        Sets the resource_category of this MonitoredResourceTypeSummary.
        Resource Category to indicate the kind of resource type.


        :param resource_category: The resource_category of this MonitoredResourceTypeSummary.
        :type: str
        """
        allowed_values = ["APPLICATION", "DATABASE", "MIDDLEWARE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(resource_category, allowed_values):
            resource_category = 'UNKNOWN_ENUM_VALUE'
        self._resource_category = resource_category

    @property
    def metadata(self):
        """
        Gets the metadata of this MonitoredResourceTypeSummary.

        :return: The metadata of this MonitoredResourceTypeSummary.
        :rtype: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MonitoredResourceTypeSummary.

        :param metadata: The metadata of this MonitoredResourceTypeSummary.
        :type: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        self._metadata = metadata

    @property
    def additional_namespace_map(self):
        """
        Gets the additional_namespace_map of this MonitoredResourceTypeSummary.
        Key/Value pair for additional namespaces used by stack monitoring services for SYSTEM (SMB) resource types.


        :return: The additional_namespace_map of this MonitoredResourceTypeSummary.
        :rtype: dict(str, str)
        """
        return self._additional_namespace_map

    @additional_namespace_map.setter
    def additional_namespace_map(self, additional_namespace_map):
        """
        Sets the additional_namespace_map of this MonitoredResourceTypeSummary.
        Key/Value pair for additional namespaces used by stack monitoring services for SYSTEM (SMB) resource types.


        :param additional_namespace_map: The additional_namespace_map of this MonitoredResourceTypeSummary.
        :type: dict(str, str)
        """
        self._additional_namespace_map = additional_namespace_map

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredResourceTypeSummary.
        The date and time when the monitored resource type was created, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MonitoredResourceTypeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredResourceTypeSummary.
        The date and time when the monitored resource type was created, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MonitoredResourceTypeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MonitoredResourceTypeSummary.
        The date and time when the monitored resource was updated, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this MonitoredResourceTypeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoredResourceTypeSummary.
        The date and time when the monitored resource was updated, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this MonitoredResourceTypeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResourceTypeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResourceTypeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResourceTypeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResourceTypeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResourceTypeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResourceTypeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResourceTypeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResourceTypeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResourceTypeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResourceTypeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResourceTypeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResourceTypeSummary.
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
