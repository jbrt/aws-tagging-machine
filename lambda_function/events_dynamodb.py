# coding: utf-8

""" Event parsing for DynamoDB """

from lambda_function.base import CreateEvent, UpdateEvent


class DynamoDBCreateTable(CreateEvent):
    def __init__(self, event: dict):
        super(DynamoDBCreateTable, self).__init__(event)

        # Unlike a service like EC2, DynamoDB build it's own ARN
        # We do not need to use the dedicated method to build it.
        arn = event['detail']['responseElements']['tableDescription']['tableArn']
        self._arn.append(arn)
