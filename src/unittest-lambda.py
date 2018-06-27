import json
import os
import unittest
from lambda_function.factory import EventFactory
from lambda_function.events_ec2 import *
from lambda_function.events_dynamodb import *
from lambda_function.events_s3 import *

DIRECTORY = 'event-samples'


class TestEventParsing(unittest.TestCase):

    def _get_event_data(self, event_file: str):
        with open(event_file, 'r') as file_handler:
            json_data = json.load(file_handler)
            event_object = EventFactory(json_data)
            self.assertTrue(event_object.tags)
            self.assertTrue(event_object.arn)

    def test_create_bucket(self):
        file_event = os.path.join(DIRECTORY, 's3_create_bucket.json')
        self._get_event_data(file_event)

    def test_create_table(self):
        file_event = os.path.join(DIRECTORY, 'dynamodb_create_table.json')
        self._get_event_data(file_event)

    def test_create_dhcp_options(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_dhcp_options.json')
        self._get_event_data(file_event)

    def test_create_network_acl(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_network_acl.json')
        self._get_event_data(file_event)

    def test_create_network_interface(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_network_interface.json')
        self._get_event_data(file_event)

    def test_create_image(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_image.json')
        self._get_event_data(file_event)

    def test_create_internet_gateway(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_internet_gateway.json')
        self._get_event_data(file_event)

    def test_create_security_group(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_security_group.json')
        self._get_event_data(file_event)

    def test_create_snapshot(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_snapshot.json')
        self._get_event_data(file_event)

    def test_create_subnet(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_subnet.json')
        self._get_event_data(file_event)

    def test_create_volume(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_volume.json')
        self._get_event_data(file_event)

    def test_create_vpc(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_vpc.json')
        self._get_event_data(file_event)

    def test_run_instances(self):
        file_event = os.path.join(DIRECTORY, 'ec2_run_instances.json')
        self._get_event_data(file_event)

    def test_start_instance(self):
        file_event = os.path.join(DIRECTORY, 'ec2_start_instance.json')
        self._get_event_data(file_event)


class TestFactory(unittest.TestCase):

    def _get_event_data(self, event_file: str):
        with open(event_file, 'r') as file_handler:
            json_data = json.load(file_handler)
            return EventFactory(json_data)

    def test_create_bucket(self):
        file_event = os.path.join(DIRECTORY, 's3_create_bucket.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, S3CreateBucket)

    def test_create_table(self):
        file_event = os.path.join(DIRECTORY, 'dynamodb_create_table.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, DynamoDBCreateTable)

    def test_create_dhcp_options(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_dhcp_options.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateDhcpOptions)

    def test_create_network_acl(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_network_acl.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateNetworkAcl)

    def test_create_network_interface(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_network_interface.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateNetworkInterface)

    def test_create_image(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_image.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateImage)

    def test_create_internet_gateway(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_internet_gateway.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateInternetGateway)

    def test_create_security_group(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_security_group.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateSecurityGroup)

    def test_create_snapshot(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_snapshot.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateSnapshot)

    def test_create_subnet(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_subnet.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateSubnet)

    def test_create_volume(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_volume.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateVolume)

    def test_create_vpc(self):
        file_event = os.path.join(DIRECTORY, 'ec2_create_vpc.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2CreateVpc)

    def test_run_instances(self):
        file_event = os.path.join(DIRECTORY, 'ec2_run_instances.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2RunInstances)

    def test_start_instances(self):
        file_event = os.path.join(DIRECTORY, 'ec2_start_instance.json')
        event_object = self._get_event_data(file_event)
        self.assertIsInstance(event_object, EC2StartInstances)


if __name__ == '__main__':
    unittest.main(verbosity=2)
