# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingAnalyticsTargetDetails(TargetDetails):
    """
    The log group used for the Logging Analytics target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingAnalyticsTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.LoggingAnalyticsTargetDetails.kind` attribute
        of this class is ``loggingAnalytics`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this LoggingAnalyticsTargetDetails.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"
        :type kind: str

        :param log_group_id:
            The value to assign to the log_group_id property of this LoggingAnalyticsTargetDetails.
        :type log_group_id: str

        """
        self.swagger_types = {
            'kind': 'str',
            'log_group_id': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'log_group_id': 'logGroupId'
        }

        self._kind = None
        self._log_group_id = None
        self._kind = 'loggingAnalytics'

    @property
    def log_group_id(self):
        """
        **[Required]** Gets the log_group_id of this LoggingAnalyticsTargetDetails.
        The `OCID`__ of the Logging Analytics log group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The log_group_id of this LoggingAnalyticsTargetDetails.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this LoggingAnalyticsTargetDetails.
        The `OCID`__ of the Logging Analytics log group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param log_group_id: The log_group_id of this LoggingAnalyticsTargetDetails.
        :type: str
        """
        self._log_group_id = log_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
