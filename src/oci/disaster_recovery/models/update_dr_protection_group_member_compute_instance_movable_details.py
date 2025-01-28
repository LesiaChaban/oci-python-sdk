# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .update_dr_protection_group_member_details import UpdateDrProtectionGroupMemberDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrProtectionGroupMemberComputeInstanceMovableDetails(UpdateDrProtectionGroupMemberDetails):
    """
    Update properties for a movable compute instance member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrProtectionGroupMemberComputeInstanceMovableDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.member_type` attribute
        of this class is ``COMPUTE_INSTANCE_MOVABLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"
        :type member_type: str

        :param is_retain_fault_domain:
            The value to assign to the is_retain_fault_domain property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type is_retain_fault_domain: bool

        :param destination_capacity_reservation_id:
            The value to assign to the destination_capacity_reservation_id property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type destination_capacity_reservation_id: str

        :param vnic_mappings:
            The value to assign to the vnic_mappings property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type vnic_mappings: list[oci.disaster_recovery.models.ComputeInstanceMovableVnicMappingDetails]

        :param destination_compartment_id:
            The value to assign to the destination_compartment_id property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type destination_compartment_id: str

        :param destination_dedicated_vm_host_id:
            The value to assign to the destination_dedicated_vm_host_id property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type destination_dedicated_vm_host_id: str

        :param file_system_operations:
            The value to assign to the file_system_operations property of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type file_system_operations: list[oci.disaster_recovery.models.UpdateComputeInstanceMovableFileSystemOperationDetails]

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'is_retain_fault_domain': 'bool',
            'destination_capacity_reservation_id': 'str',
            'vnic_mappings': 'list[ComputeInstanceMovableVnicMappingDetails]',
            'destination_compartment_id': 'str',
            'destination_dedicated_vm_host_id': 'str',
            'file_system_operations': 'list[UpdateComputeInstanceMovableFileSystemOperationDetails]'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'is_retain_fault_domain': 'isRetainFaultDomain',
            'destination_capacity_reservation_id': 'destinationCapacityReservationId',
            'vnic_mappings': 'vnicMappings',
            'destination_compartment_id': 'destinationCompartmentId',
            'destination_dedicated_vm_host_id': 'destinationDedicatedVmHostId',
            'file_system_operations': 'fileSystemOperations'
        }

        self._member_id = None
        self._member_type = None
        self._is_retain_fault_domain = None
        self._destination_capacity_reservation_id = None
        self._vnic_mappings = None
        self._destination_compartment_id = None
        self._destination_dedicated_vm_host_id = None
        self._file_system_operations = None
        self._member_type = 'COMPUTE_INSTANCE_MOVABLE'

    @property
    def is_retain_fault_domain(self):
        """
        Gets the is_retain_fault_domain of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A flag indicating if the compute instance should be moved to the same fault domain in the destination region.
        The compute instance launch will fail if this flag is set to true and capacity is not available in the
        specified fault domain in the destination region.

        Example: `false`


        :return: The is_retain_fault_domain of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: bool
        """
        return self._is_retain_fault_domain

    @is_retain_fault_domain.setter
    def is_retain_fault_domain(self, is_retain_fault_domain):
        """
        Sets the is_retain_fault_domain of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A flag indicating if the compute instance should be moved to the same fault domain in the destination region.
        The compute instance launch will fail if this flag is set to true and capacity is not available in the
        specified fault domain in the destination region.

        Example: `false`


        :param is_retain_fault_domain: The is_retain_fault_domain of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: bool
        """
        self._is_retain_fault_domain = is_retain_fault_domain

    @property
    def destination_capacity_reservation_id(self):
        """
        Gets the destination_capacity_reservation_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a capacity reservation in the destination region which will be used to launch
        the compute instance.

        Example: `ocid1.capacityreservation.oc1..uniqueID`


        :return: The destination_capacity_reservation_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: str
        """
        return self._destination_capacity_reservation_id

    @destination_capacity_reservation_id.setter
    def destination_capacity_reservation_id(self, destination_capacity_reservation_id):
        """
        Sets the destination_capacity_reservation_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a capacity reservation in the destination region which will be used to launch
        the compute instance.

        Example: `ocid1.capacityreservation.oc1..uniqueID`


        :param destination_capacity_reservation_id: The destination_capacity_reservation_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: str
        """
        self._destination_capacity_reservation_id = destination_capacity_reservation_id

    @property
    def vnic_mappings(self):
        """
        Gets the vnic_mappings of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A list of compute instance VNIC mappings.


        :return: The vnic_mappings of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: list[oci.disaster_recovery.models.ComputeInstanceMovableVnicMappingDetails]
        """
        return self._vnic_mappings

    @vnic_mappings.setter
    def vnic_mappings(self, vnic_mappings):
        """
        Sets the vnic_mappings of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A list of compute instance VNIC mappings.


        :param vnic_mappings: The vnic_mappings of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: list[oci.disaster_recovery.models.ComputeInstanceMovableVnicMappingDetails]
        """
        self._vnic_mappings = vnic_mappings

    @property
    def destination_compartment_id(self):
        """
        Gets the destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a compartment in the destination region in which the compute instance
        should be launched.

        Example: `ocid1.compartment.oc1..uniqueID`


        :return: The destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: str
        """
        return self._destination_compartment_id

    @destination_compartment_id.setter
    def destination_compartment_id(self, destination_compartment_id):
        """
        Sets the destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a compartment in the destination region in which the compute instance
        should be launched.

        Example: `ocid1.compartment.oc1..uniqueID`


        :param destination_compartment_id: The destination_compartment_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: str
        """
        self._destination_compartment_id = destination_compartment_id

    @property
    def destination_dedicated_vm_host_id(self):
        """
        Gets the destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a dedicated VM host in the destination region where the compute instance
        should be launched.

        Example: `ocid1.dedicatedvmhost.oc1..uniqueID`


        :return: The destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: str
        """
        return self._destination_dedicated_vm_host_id

    @destination_dedicated_vm_host_id.setter
    def destination_dedicated_vm_host_id(self, destination_dedicated_vm_host_id):
        """
        Sets the destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        The OCID of a dedicated VM host in the destination region where the compute instance
        should be launched.

        Example: `ocid1.dedicatedvmhost.oc1..uniqueID`


        :param destination_dedicated_vm_host_id: The destination_dedicated_vm_host_id of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: str
        """
        self._destination_dedicated_vm_host_id = destination_dedicated_vm_host_id

    @property
    def file_system_operations(self):
        """
        Gets the file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A list of operations performed on file systems used by the compute instance.


        :return: The file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateComputeInstanceMovableFileSystemOperationDetails]
        """
        return self._file_system_operations

    @file_system_operations.setter
    def file_system_operations(self, file_system_operations):
        """
        Sets the file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        A list of operations performed on file systems used by the compute instance.


        :param file_system_operations: The file_system_operations of this UpdateDrProtectionGroupMemberComputeInstanceMovableDetails.
        :type: list[oci.disaster_recovery.models.UpdateComputeInstanceMovableFileSystemOperationDetails]
        """
        self._file_system_operations = file_system_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
