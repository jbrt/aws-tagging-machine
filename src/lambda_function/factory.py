# coding: utf-8

"""
This module contains a factory used to simplify the creation
of event objects.
"""

from lambda_function.base import EventError
from lambda_function.events_ec2 import *
from lambda_function.events_dynamodb import *
from lambda_function.events_s3 import *


class EventFactory(object):
    """ This class build and return the right event object """

    def __new__(cls, event: dict):

        cls._events = {'CreateBucket': S3CreateBucket,
                       'CreateDhcpOptions': EC2CreateDhcpOptions,
                       'CreateNetworkAcl': EC2CreateNetworkAcl,
                       'CreateNetworkInterface': EC2CreateNetworkInterface,
                       'CreateImage': EC2CreateImage,
                       'CreateInternetGateway': EC2CreateInternetGateway,
                       'CreateRouteTable': EC2CreateRouteTable,
                       'CreateSecurityGroup': EC2CreateSecurityGroup,
                       'CreateSnapshot': EC2CreateSnapshot,
                       'CreateSubnet': EC2CreateSubnet,
                       'CreateTable': DynamoDBCreateTable,
                       'CreateVolume': EC2CreateVolume,
                       'CreateVpc': EC2CreateVpc,
                       'RunInstances': EC2RunInstances,
                       'StartInstances': EC2StartInstances}

        try:
            event_name = event['detail']['eventName']

        except KeyError:
            raise EventError(f"Can't retrieve event name. "
                             f"Malformed event ? Event: {event}")

        if event_name not in cls._events:
            raise EventError(f'{event_name} not yet handle by that tool')

        return cls._events[event_name](event)
