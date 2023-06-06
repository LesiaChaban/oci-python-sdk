# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCapacityReportShapeAvailabilityDetails(object):
    """
    Information about the shapes in a capacity report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCapacityReportShapeAvailabilityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fault_domain:
            The value to assign to the fault_domain property of this CreateCapacityReportShapeAvailabilityDetails.
        :type fault_domain: str

        :param instance_shape:
            The value to assign to the instance_shape property of this CreateCapacityReportShapeAvailabilityDetails.
        :type instance_shape: str

        :param instance_shape_config:
            The value to assign to the instance_shape_config property of this CreateCapacityReportShapeAvailabilityDetails.
        :type instance_shape_config: oci.core.models.CapacityReportInstanceShapeConfig

        """
        self.swagger_types = {
            'fault_domain': 'str',
            'instance_shape': 'str',
            'instance_shape_config': 'CapacityReportInstanceShapeConfig'
        }

        self.attribute_map = {
            'fault_domain': 'faultDomain',
            'instance_shape': 'instanceShape',
            'instance_shape_config': 'instanceShapeConfig'
        }

        self._fault_domain = None
        self._instance_shape = None
        self._instance_shape_config = None

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CreateCapacityReportShapeAvailabilityDetails.
        The fault domain for the capacity report.

        If you do not specify a fault domain, the capacity report includes information about all fault domains.


        :return: The fault_domain of this CreateCapacityReportShapeAvailabilityDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CreateCapacityReportShapeAvailabilityDetails.
        The fault domain for the capacity report.

        If you do not specify a fault domain, the capacity report includes information about all fault domains.


        :param fault_domain: The fault_domain of this CreateCapacityReportShapeAvailabilityDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def instance_shape(self):
        """
        **[Required]** Gets the instance_shape of this CreateCapacityReportShapeAvailabilityDetails.
        The shape that you want to request a capacity report for. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :return: The instance_shape of this CreateCapacityReportShapeAvailabilityDetails.
        :rtype: str
        """
        return self._instance_shape

    @instance_shape.setter
    def instance_shape(self, instance_shape):
        """
        Sets the instance_shape of this CreateCapacityReportShapeAvailabilityDetails.
        The shape that you want to request a capacity report for. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :param instance_shape: The instance_shape of this CreateCapacityReportShapeAvailabilityDetails.
        :type: str
        """
        self._instance_shape = instance_shape

    @property
    def instance_shape_config(self):
        """
        Gets the instance_shape_config of this CreateCapacityReportShapeAvailabilityDetails.

        :return: The instance_shape_config of this CreateCapacityReportShapeAvailabilityDetails.
        :rtype: oci.core.models.CapacityReportInstanceShapeConfig
        """
        return self._instance_shape_config

    @instance_shape_config.setter
    def instance_shape_config(self, instance_shape_config):
        """
        Sets the instance_shape_config of this CreateCapacityReportShapeAvailabilityDetails.

        :param instance_shape_config: The instance_shape_config of this CreateCapacityReportShapeAvailabilityDetails.
        :type: oci.core.models.CapacityReportInstanceShapeConfig
        """
        self._instance_shape_config = instance_shape_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
