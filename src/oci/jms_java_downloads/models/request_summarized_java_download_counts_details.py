# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestSummarizedJavaDownloadCountsDetails(object):
    """
    Attributes to summarize the Java download counts in a tenancy.
    """

    #: A constant which can be used with the group_as property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "JAVA_FAMILY"
    GROUP_AS_JAVA_FAMILY = "JAVA_FAMILY"

    #: A constant which can be used with the group_as property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "JAVA_RELEASE"
    GROUP_AS_JAVA_RELEASE = "JAVA_RELEASE"

    #: A constant which can be used with the group_as property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "PLATFORM"
    GROUP_AS_PLATFORM = "PLATFORM"

    #: A constant which can be used with the sort_by property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "FAMILY_VERSION"
    SORT_BY_FAMILY_VERSION = "FAMILY_VERSION"

    #: A constant which can be used with the sort_by property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "DOWNLOAD_COUNT"
    SORT_BY_DOWNLOAD_COUNT = "DOWNLOAD_COUNT"

    #: A constant which can be used with the sort_order property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a RequestSummarizedJavaDownloadCountsDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    def __init__(self, **kwargs):
        """
        Initializes a new RequestSummarizedJavaDownloadCountsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this RequestSummarizedJavaDownloadCountsDetails.
        :type compartment_id: str

        :param group_as:
            The value to assign to the group_as property of this RequestSummarizedJavaDownloadCountsDetails.
            Allowed values for this property are: "JAVA_FAMILY", "JAVA_RELEASE", "PLATFORM"
        :type group_as: str

        :param family_version:
            The value to assign to the family_version property of this RequestSummarizedJavaDownloadCountsDetails.
        :type family_version: str

        :param release_version:
            The value to assign to the release_version property of this RequestSummarizedJavaDownloadCountsDetails.
        :type release_version: str

        :param time_start:
            The value to assign to the time_start property of this RequestSummarizedJavaDownloadCountsDetails.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this RequestSummarizedJavaDownloadCountsDetails.
        :type time_end: datetime

        :param sort_by:
            The value to assign to the sort_by property of this RequestSummarizedJavaDownloadCountsDetails.
            Allowed values for this property are: "FAMILY_VERSION", "DOWNLOAD_COUNT"
        :type sort_by: str

        :param sort_order:
            The value to assign to the sort_order property of this RequestSummarizedJavaDownloadCountsDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        :param limit:
            The value to assign to the limit property of this RequestSummarizedJavaDownloadCountsDetails.
        :type limit: int

        :param page:
            The value to assign to the page property of this RequestSummarizedJavaDownloadCountsDetails.
        :type page: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'group_as': 'str',
            'family_version': 'str',
            'release_version': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'sort_by': 'str',
            'sort_order': 'str',
            'limit': 'int',
            'page': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'group_as': 'groupAs',
            'family_version': 'familyVersion',
            'release_version': 'releaseVersion',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'sort_by': 'sortBy',
            'sort_order': 'sortOrder',
            'limit': 'limit',
            'page': 'page'
        }

        self._compartment_id = None
        self._group_as = None
        self._family_version = None
        self._release_version = None
        self._time_start = None
        self._time_end = None
        self._sort_by = None
        self._sort_order = None
        self._limit = None
        self._page = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RequestSummarizedJavaDownloadCountsDetails.
        The compartment `OCID`__ here should be the tenancy OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RequestSummarizedJavaDownloadCountsDetails.
        The compartment `OCID`__ here should be the tenancy OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def group_as(self):
        """
        **[Required]** Gets the group_as of this RequestSummarizedJavaDownloadCountsDetails.
        The property that specifies the aggregation type for the download counts.

        Allowed values for this property are: "JAVA_FAMILY", "JAVA_RELEASE", "PLATFORM"


        :return: The group_as of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._group_as

    @group_as.setter
    def group_as(self, group_as):
        """
        Sets the group_as of this RequestSummarizedJavaDownloadCountsDetails.
        The property that specifies the aggregation type for the download counts.


        :param group_as: The group_as of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        allowed_values = ["JAVA_FAMILY", "JAVA_RELEASE", "PLATFORM"]
        if not value_allowed_none_or_none_sentinel(group_as, allowed_values):
            raise ValueError(
                f"Invalid value for `group_as`, must be None or one of {allowed_values}"
            )
        self._group_as = group_as

    @property
    def family_version(self):
        """
        Gets the family_version of this RequestSummarizedJavaDownloadCountsDetails.
        Unique Java family version identifier.


        :return: The family_version of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """
        Sets the family_version of this RequestSummarizedJavaDownloadCountsDetails.
        Unique Java family version identifier.


        :param family_version: The family_version of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        self._family_version = family_version

    @property
    def release_version(self):
        """
        Gets the release_version of this RequestSummarizedJavaDownloadCountsDetails.
        Unique Java release version identifier.


        :return: The release_version of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """
        Sets the release_version of this RequestSummarizedJavaDownloadCountsDetails.
        Unique Java release version identifier.


        :param release_version: The release_version of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        self._release_version = release_version

    @property
    def time_start(self):
        """
        Gets the time_start of this RequestSummarizedJavaDownloadCountsDetails.
        The start time from when download data has to be included (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_start of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this RequestSummarizedJavaDownloadCountsDetails.
        The start time from when download data has to be included (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_start: The time_start of this RequestSummarizedJavaDownloadCountsDetails.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this RequestSummarizedJavaDownloadCountsDetails.
        The end time until when the download data has to be included (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_end of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this RequestSummarizedJavaDownloadCountsDetails.
        The end time until when the download data has to be included (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_end: The time_end of this RequestSummarizedJavaDownloadCountsDetails.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def sort_by(self):
        """
        Gets the sort_by of this RequestSummarizedJavaDownloadCountsDetails.
        The property to be used for sorting the aggregated report.

        Allowed values for this property are: "FAMILY_VERSION", "DOWNLOAD_COUNT"


        :return: The sort_by of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this RequestSummarizedJavaDownloadCountsDetails.
        The property to be used for sorting the aggregated report.


        :param sort_by: The sort_by of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        allowed_values = ["FAMILY_VERSION", "DOWNLOAD_COUNT"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                f"Invalid value for `sort_by`, must be None or one of {allowed_values}"
            )
        self._sort_by = sort_by

    @property
    def sort_order(self):
        """
        Gets the sort_order of this RequestSummarizedJavaDownloadCountsDetails.
        The sort order for the aggregated report.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this RequestSummarizedJavaDownloadCountsDetails.
        The sort order for the aggregated report.


        :param sort_order: The sort_order of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(sort_order, allowed_values):
            raise ValueError(
                f"Invalid value for `sort_order`, must be None or one of {allowed_values}"
            )
        self._sort_order = sort_order

    @property
    def limit(self):
        """
        Gets the limit of this RequestSummarizedJavaDownloadCountsDetails.
        The maximum number of items to return.


        :return: The limit of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this RequestSummarizedJavaDownloadCountsDetails.
        The maximum number of items to return.


        :param limit: The limit of this RequestSummarizedJavaDownloadCountsDetails.
        :type: int
        """
        self._limit = limit

    @property
    def page(self):
        """
        Gets the page of this RequestSummarizedJavaDownloadCountsDetails.
        The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous call.


        :return: The page of this RequestSummarizedJavaDownloadCountsDetails.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this RequestSummarizedJavaDownloadCountsDetails.
        The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous call.


        :param page: The page of this RequestSummarizedJavaDownloadCountsDetails.
        :type: str
        """
        self._page = page

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
