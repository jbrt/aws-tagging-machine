# coding: utf-8

"""
Event parsing for SQS
Each class describe a specific SQS event with it's own data and finally
build an ARN or a list of ARNs.
"""


from lambda_function.base import CreateEvent


class SQSCreateQueue(CreateEvent):
    def __init__(self, event: dict):
        super(SQSCreateQueue, self).__init__(event)
        self._arn_parts['service'] = 'sqs'
        self._arn_parts['resource'] = event['detail']['requestParameters']['queueName']
        self._arn.append(self._arn_templates['t1'].format(**self._arn_parts))
