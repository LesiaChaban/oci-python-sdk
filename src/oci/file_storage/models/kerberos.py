# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Kerberos(object):
    """
    Allows administrator to configure a mount target to interact with the administrator's Kerberos infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Kerberos object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kerberos_realm:
            The value to assign to the kerberos_realm property of this Kerberos.
        :type kerberos_realm: str

        :param key_tab_secret_id:
            The value to assign to the key_tab_secret_id property of this Kerberos.
        :type key_tab_secret_id: str

        :param current_key_tab_secret_version:
            The value to assign to the current_key_tab_secret_version property of this Kerberos.
        :type current_key_tab_secret_version: int

        :param backup_key_tab_secret_version:
            The value to assign to the backup_key_tab_secret_version property of this Kerberos.
        :type backup_key_tab_secret_version: int

        :param is_kerberos_enabled:
            The value to assign to the is_kerberos_enabled property of this Kerberos.
        :type is_kerberos_enabled: bool

        """
        self.swagger_types = {
            'kerberos_realm': 'str',
            'key_tab_secret_id': 'str',
            'current_key_tab_secret_version': 'int',
            'backup_key_tab_secret_version': 'int',
            'is_kerberos_enabled': 'bool'
        }

        self.attribute_map = {
            'kerberos_realm': 'kerberosRealm',
            'key_tab_secret_id': 'keyTabSecretId',
            'current_key_tab_secret_version': 'currentKeyTabSecretVersion',
            'backup_key_tab_secret_version': 'backupKeyTabSecretVersion',
            'is_kerberos_enabled': 'isKerberosEnabled'
        }

        self._kerberos_realm = None
        self._key_tab_secret_id = None
        self._current_key_tab_secret_version = None
        self._backup_key_tab_secret_version = None
        self._is_kerberos_enabled = None

    @property
    def kerberos_realm(self):
        """
        **[Required]** Gets the kerberos_realm of this Kerberos.
        The Kerberos realm that the mount target will join.


        :return: The kerberos_realm of this Kerberos.
        :rtype: str
        """
        return self._kerberos_realm

    @kerberos_realm.setter
    def kerberos_realm(self, kerberos_realm):
        """
        Sets the kerberos_realm of this Kerberos.
        The Kerberos realm that the mount target will join.


        :param kerberos_realm: The kerberos_realm of this Kerberos.
        :type: str
        """
        self._kerberos_realm = kerberos_realm

    @property
    def key_tab_secret_id(self):
        """
        Gets the key_tab_secret_id of this Kerberos.
        The `OCID`__ of the keytab secret in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_tab_secret_id of this Kerberos.
        :rtype: str
        """
        return self._key_tab_secret_id

    @key_tab_secret_id.setter
    def key_tab_secret_id(self, key_tab_secret_id):
        """
        Sets the key_tab_secret_id of this Kerberos.
        The `OCID`__ of the keytab secret in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_tab_secret_id: The key_tab_secret_id of this Kerberos.
        :type: str
        """
        self._key_tab_secret_id = key_tab_secret_id

    @property
    def current_key_tab_secret_version(self):
        """
        Gets the current_key_tab_secret_version of this Kerberos.
        Version of the keytab secret in the Vault to use.


        :return: The current_key_tab_secret_version of this Kerberos.
        :rtype: int
        """
        return self._current_key_tab_secret_version

    @current_key_tab_secret_version.setter
    def current_key_tab_secret_version(self, current_key_tab_secret_version):
        """
        Sets the current_key_tab_secret_version of this Kerberos.
        Version of the keytab secret in the Vault to use.


        :param current_key_tab_secret_version: The current_key_tab_secret_version of this Kerberos.
        :type: int
        """
        self._current_key_tab_secret_version = current_key_tab_secret_version

    @property
    def backup_key_tab_secret_version(self):
        """
        Gets the backup_key_tab_secret_version of this Kerberos.
        Version of the keytab secert in the Vault to use as a backup.


        :return: The backup_key_tab_secret_version of this Kerberos.
        :rtype: int
        """
        return self._backup_key_tab_secret_version

    @backup_key_tab_secret_version.setter
    def backup_key_tab_secret_version(self, backup_key_tab_secret_version):
        """
        Sets the backup_key_tab_secret_version of this Kerberos.
        Version of the keytab secert in the Vault to use as a backup.


        :param backup_key_tab_secret_version: The backup_key_tab_secret_version of this Kerberos.
        :type: int
        """
        self._backup_key_tab_secret_version = backup_key_tab_secret_version

    @property
    def is_kerberos_enabled(self):
        """
        Gets the is_kerberos_enabled of this Kerberos.
        Specifies whether to enable or disable Kerberos.


        :return: The is_kerberos_enabled of this Kerberos.
        :rtype: bool
        """
        return self._is_kerberos_enabled

    @is_kerberos_enabled.setter
    def is_kerberos_enabled(self, is_kerberos_enabled):
        """
        Sets the is_kerberos_enabled of this Kerberos.
        Specifies whether to enable or disable Kerberos.


        :param is_kerberos_enabled: The is_kerberos_enabled of this Kerberos.
        :type: bool
        """
        self._is_kerberos_enabled = is_kerberos_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
