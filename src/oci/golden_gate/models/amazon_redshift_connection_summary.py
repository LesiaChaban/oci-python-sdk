# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AmazonRedshiftConnectionSummary(ConnectionSummary):
    """
    Summary of the Amazon Redshift Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AmazonRedshiftConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.AmazonRedshiftConnectionSummary.connection_type` attribute
        of this class is ``AMAZON_REDSHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this AmazonRedshiftConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this AmazonRedshiftConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AmazonRedshiftConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AmazonRedshiftConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AmazonRedshiftConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AmazonRedshiftConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AmazonRedshiftConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AmazonRedshiftConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AmazonRedshiftConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AmazonRedshiftConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AmazonRedshiftConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AmazonRedshiftConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this AmazonRedshiftConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this AmazonRedshiftConnectionSummary.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this AmazonRedshiftConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this AmazonRedshiftConnectionSummary.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this AmazonRedshiftConnectionSummary.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this AmazonRedshiftConnectionSummary.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param locks:
            The value to assign to the locks property of this AmazonRedshiftConnectionSummary.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this AmazonRedshiftConnectionSummary.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this AmazonRedshiftConnectionSummary.
        :type technology_type: str

        :param connection_url:
            The value to assign to the connection_url property of this AmazonRedshiftConnectionSummary.
        :type connection_url: str

        :param username:
            The value to assign to the username property of this AmazonRedshiftConnectionSummary.
        :type username: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this AmazonRedshiftConnectionSummary.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'locks': 'list[ResourceLock]',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'connection_url': 'str',
            'username': 'str',
            'password_secret_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'locks': 'locks',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'connection_url': 'connectionUrl',
            'username': 'username',
            'password_secret_id': 'passwordSecretId'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._locks = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._connection_url = None
        self._username = None
        self._password_secret_id = None
        self._connection_type = 'AMAZON_REDSHIFT'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this AmazonRedshiftConnectionSummary.
        The Amazon Redshift technology type.


        :return: The technology_type of this AmazonRedshiftConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this AmazonRedshiftConnectionSummary.
        The Amazon Redshift technology type.


        :param technology_type: The technology_type of this AmazonRedshiftConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def connection_url(self):
        """
        **[Required]** Gets the connection_url of this AmazonRedshiftConnectionSummary.
        Connection URL.
        e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'


        :return: The connection_url of this AmazonRedshiftConnectionSummary.
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """
        Sets the connection_url of this AmazonRedshiftConnectionSummary.
        Connection URL.
        e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'


        :param connection_url: The connection_url of this AmazonRedshiftConnectionSummary.
        :type: str
        """
        self._connection_url = connection_url

    @property
    def username(self):
        """
        **[Required]** Gets the username of this AmazonRedshiftConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :return: The username of this AmazonRedshiftConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this AmazonRedshiftConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :param username: The username of this AmazonRedshiftConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this AmazonRedshiftConnectionSummary.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this AmazonRedshiftConnectionSummary.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this AmazonRedshiftConnectionSummary.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this AmazonRedshiftConnectionSummary.
        :type: str
        """
        self._password_secret_id = password_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
