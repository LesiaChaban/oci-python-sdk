# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NewsReport(object):
    """
    News report resource.
    """

    #: A constant which can be used with the news_frequency property of a NewsReport.
    #: This constant has a value of "WEEKLY"
    NEWS_FREQUENCY_WEEKLY = "WEEKLY"

    #: A constant which can be used with the news_frequency property of a NewsReport.
    #: This constant has a value of "DAILY"
    NEWS_FREQUENCY_DAILY = "DAILY"

    #: A constant which can be used with the news_frequency property of a NewsReport.
    #: This constant has a value of "HOURLY"
    NEWS_FREQUENCY_HOURLY = "HOURLY"

    #: A constant which can be used with the locale property of a NewsReport.
    #: This constant has a value of "EN"
    LOCALE_EN = "EN"

    #: A constant which can be used with the status property of a NewsReport.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a NewsReport.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a NewsReport.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a NewsReport.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    #: A constant which can be used with the day_of_week property of a NewsReport.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the match_rule property of a NewsReport.
    #: This constant has a value of "MATCH_ANY"
    MATCH_RULE_MATCH_ANY = "MATCH_ANY"

    #: A constant which can be used with the match_rule property of a NewsReport.
    #: This constant has a value of "MATCH_ALL"
    MATCH_RULE_MATCH_ALL = "MATCH_ALL"

    #: A constant which can be used with the match_rule property of a NewsReport.
    #: This constant has a value of "MATCH_NONE"
    MATCH_RULE_MATCH_NONE = "MATCH_NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new NewsReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param news_frequency:
            The value to assign to the news_frequency property of this NewsReport.
            Allowed values for this property are: "WEEKLY", "DAILY", "HOURLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type news_frequency: str

        :param content_types:
            The value to assign to the content_types property of this NewsReport.
        :type content_types: oci.opsi.models.NewsContentTypes

        :param locale:
            The value to assign to the locale property of this NewsReport.
            Allowed values for this property are: "EN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type locale: str

        :param id:
            The value to assign to the id property of this NewsReport.
        :type id: str

        :param description:
            The value to assign to the description property of this NewsReport.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NewsReport.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this NewsReport.
        :type name: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this NewsReport.
        :type ons_topic_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NewsReport.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NewsReport.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this NewsReport.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this NewsReport.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this NewsReport.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NewsReport.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NewsReport.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this NewsReport.
        :type lifecycle_details: str

        :param day_of_week:
            The value to assign to the day_of_week property of this NewsReport.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        :param are_child_compartments_included:
            The value to assign to the are_child_compartments_included property of this NewsReport.
        :type are_child_compartments_included: bool

        :param tag_filters:
            The value to assign to the tag_filters property of this NewsReport.
        :type tag_filters: list[str]

        :param match_rule:
            The value to assign to the match_rule property of this NewsReport.
            Allowed values for this property are: "MATCH_ANY", "MATCH_ALL", "MATCH_NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type match_rule: str

        """
        self.swagger_types = {
            'news_frequency': 'str',
            'content_types': 'NewsContentTypes',
            'locale': 'str',
            'id': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'ons_topic_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'day_of_week': 'str',
            'are_child_compartments_included': 'bool',
            'tag_filters': 'list[str]',
            'match_rule': 'str'
        }

        self.attribute_map = {
            'news_frequency': 'newsFrequency',
            'content_types': 'contentTypes',
            'locale': 'locale',
            'id': 'id',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'ons_topic_id': 'onsTopicId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'day_of_week': 'dayOfWeek',
            'are_child_compartments_included': 'areChildCompartmentsIncluded',
            'tag_filters': 'tagFilters',
            'match_rule': 'matchRule'
        }

        self._news_frequency = None
        self._content_types = None
        self._locale = None
        self._id = None
        self._description = None
        self._compartment_id = None
        self._name = None
        self._ons_topic_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._day_of_week = None
        self._are_child_compartments_included = None
        self._tag_filters = None
        self._match_rule = None

    @property
    def news_frequency(self):
        """
        **[Required]** Gets the news_frequency of this NewsReport.
        News report frequency.

        Allowed values for this property are: "WEEKLY", "DAILY", "HOURLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The news_frequency of this NewsReport.
        :rtype: str
        """
        return self._news_frequency

    @news_frequency.setter
    def news_frequency(self, news_frequency):
        """
        Sets the news_frequency of this NewsReport.
        News report frequency.


        :param news_frequency: The news_frequency of this NewsReport.
        :type: str
        """
        allowed_values = ["WEEKLY", "DAILY", "HOURLY"]
        if not value_allowed_none_or_none_sentinel(news_frequency, allowed_values):
            news_frequency = 'UNKNOWN_ENUM_VALUE'
        self._news_frequency = news_frequency

    @property
    def content_types(self):
        """
        **[Required]** Gets the content_types of this NewsReport.

        :return: The content_types of this NewsReport.
        :rtype: oci.opsi.models.NewsContentTypes
        """
        return self._content_types

    @content_types.setter
    def content_types(self, content_types):
        """
        Sets the content_types of this NewsReport.

        :param content_types: The content_types of this NewsReport.
        :type: oci.opsi.models.NewsContentTypes
        """
        self._content_types = content_types

    @property
    def locale(self):
        """
        Gets the locale of this NewsReport.
        Language of the news report.

        Allowed values for this property are: "EN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The locale of this NewsReport.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this NewsReport.
        Language of the news report.


        :param locale: The locale of this NewsReport.
        :type: str
        """
        allowed_values = ["EN"]
        if not value_allowed_none_or_none_sentinel(locale, allowed_values):
            locale = 'UNKNOWN_ENUM_VALUE'
        self._locale = locale

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NewsReport.
        The `OCID`__ of the news report resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this NewsReport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NewsReport.
        The `OCID`__ of the news report resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this NewsReport.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this NewsReport.
        The description of the news report.


        :return: The description of this NewsReport.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NewsReport.
        The description of the news report.


        :param description: The description of this NewsReport.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NewsReport.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this NewsReport.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NewsReport.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this NewsReport.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this NewsReport.
        The news report name.


        :return: The name of this NewsReport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NewsReport.
        The news report name.


        :param name: The name of this NewsReport.
        :type: str
        """
        self._name = name

    @property
    def ons_topic_id(self):
        """
        **[Required]** Gets the ons_topic_id of this NewsReport.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ons_topic_id of this NewsReport.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this NewsReport.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ons_topic_id: The ons_topic_id of this NewsReport.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this NewsReport.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this NewsReport.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this NewsReport.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this NewsReport.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this NewsReport.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this NewsReport.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this NewsReport.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this NewsReport.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this NewsReport.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this NewsReport.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this NewsReport.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this NewsReport.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def status(self):
        """
        Gets the status of this NewsReport.
        Indicates the status of a news report in Ops Insights.

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this NewsReport.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NewsReport.
        Indicates the status of a news report in Ops Insights.


        :param status: The status of this NewsReport.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        Gets the time_created of this NewsReport.
        The time the the news report was first enabled. An RFC3339 formatted datetime string.


        :return: The time_created of this NewsReport.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NewsReport.
        The time the the news report was first enabled. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this NewsReport.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this NewsReport.
        The time the news report was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this NewsReport.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this NewsReport.
        The time the news report was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this NewsReport.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this NewsReport.
        The current state of the news report.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NewsReport.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NewsReport.
        The current state of the news report.


        :param lifecycle_state: The lifecycle_state of this NewsReport.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this NewsReport.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this NewsReport.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this NewsReport.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this NewsReport.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this NewsReport.
        Day of the week in which the news report will be sent if the frequency is set to WEEKLY.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this NewsReport.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this NewsReport.
        Day of the week in which the news report will be sent if the frequency is set to WEEKLY.


        :param day_of_week: The day_of_week of this NewsReport.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    @property
    def are_child_compartments_included(self):
        """
        Gets the are_child_compartments_included of this NewsReport.
        A flag to consider the resources within a given compartment and all sub-compartments.


        :return: The are_child_compartments_included of this NewsReport.
        :rtype: bool
        """
        return self._are_child_compartments_included

    @are_child_compartments_included.setter
    def are_child_compartments_included(self, are_child_compartments_included):
        """
        Sets the are_child_compartments_included of this NewsReport.
        A flag to consider the resources within a given compartment and all sub-compartments.


        :param are_child_compartments_included: The are_child_compartments_included of this NewsReport.
        :type: bool
        """
        self._are_child_compartments_included = are_child_compartments_included

    @property
    def tag_filters(self):
        """
        Gets the tag_filters of this NewsReport.
        List of tag filters; each filter composed by a namespace, key, and value.
        Example for defined tags - '<TagNamespace>.<TagKey>=<TagValue>'.
        Example for freeform tags - '<TagKey>=<TagValue>'.


        :return: The tag_filters of this NewsReport.
        :rtype: list[str]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """
        Sets the tag_filters of this NewsReport.
        List of tag filters; each filter composed by a namespace, key, and value.
        Example for defined tags - '<TagNamespace>.<TagKey>=<TagValue>'.
        Example for freeform tags - '<TagKey>=<TagValue>'.


        :param tag_filters: The tag_filters of this NewsReport.
        :type: list[str]
        """
        self._tag_filters = tag_filters

    @property
    def match_rule(self):
        """
        Gets the match_rule of this NewsReport.
        Match rule used for tag filters.

        Allowed values for this property are: "MATCH_ANY", "MATCH_ALL", "MATCH_NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The match_rule of this NewsReport.
        :rtype: str
        """
        return self._match_rule

    @match_rule.setter
    def match_rule(self, match_rule):
        """
        Sets the match_rule of this NewsReport.
        Match rule used for tag filters.


        :param match_rule: The match_rule of this NewsReport.
        :type: str
        """
        allowed_values = ["MATCH_ANY", "MATCH_ALL", "MATCH_NONE"]
        if not value_allowed_none_or_none_sentinel(match_rule, allowed_values):
            match_rule = 'UNKNOWN_ENUM_VALUE'
        self._match_rule = match_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
