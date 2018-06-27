# coding: utf-8

"""
Event parsing for S3
Each class describe a specific S3 event with it's own data and finally
build an ARN or a list of ARNs.
"""


from lambda_function.base import CreateEvent


class S3CreateBucket(CreateEvent):
    def __init__(self, event: dict):
        super(S3CreateBucket, self).__init__(event)
        self._arn_parts['service'] = 's3'
        self._arn_parts['region'] = ''  # S3 do not need region name
        self._arn_parts['resource'] = event['detail']['requestParameters']['bucketName']
        self._arn.append(self._arn_templates['t5'].format(**self._arn_parts))
