# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseKeyHistoryEntry(object):
    """
    The Autonomous Database `Vault`__ service key management history entry.

    __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseKeyHistoryEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousDatabaseKeyHistoryEntry.
        :type id: str

        :param vault_id:
            The value to assign to the vault_id property of this AutonomousDatabaseKeyHistoryEntry.
        :type vault_id: str

        :param time_activated:
            The value to assign to the time_activated property of this AutonomousDatabaseKeyHistoryEntry.
        :type time_activated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'vault_id': 'str',
            'time_activated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'vault_id': 'vaultId',
            'time_activated': 'timeActivated'
        }

        self._id = None
        self._vault_id = None
        self._time_activated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDatabaseKeyHistoryEntry.
        The id of the Autonomous Database `Vault`__ service key management history entry.

        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The id of this AutonomousDatabaseKeyHistoryEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDatabaseKeyHistoryEntry.
        The id of the Autonomous Database `Vault`__ service key management history entry.

        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param id: The id of this AutonomousDatabaseKeyHistoryEntry.
        :type: str
        """
        self._id = id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this AutonomousDatabaseKeyHistoryEntry.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this AutonomousDatabaseKeyHistoryEntry.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this AutonomousDatabaseKeyHistoryEntry.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this AutonomousDatabaseKeyHistoryEntry.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def time_activated(self):
        """
        Gets the time_activated of this AutonomousDatabaseKeyHistoryEntry.
        The date and time the kms key activated.


        :return: The time_activated of this AutonomousDatabaseKeyHistoryEntry.
        :rtype: datetime
        """
        return self._time_activated

    @time_activated.setter
    def time_activated(self, time_activated):
        """
        Sets the time_activated of this AutonomousDatabaseKeyHistoryEntry.
        The date and time the kms key activated.


        :param time_activated: The time_activated of this AutonomousDatabaseKeyHistoryEntry.
        :type: datetime
        """
        self._time_activated = time_activated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
