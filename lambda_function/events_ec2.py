# coding: utf-8

""" Event parsing for EC2 """


from lambda_function.base import CreateEvent, UpdateEvent


class EC2CreateInternetGateway(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateInternetGateway, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['internetGateway']\
                                           ['internetGatewayId']
        self._arn.append(self._arn_templates['t1'].format(**self._arn_parts))


class EC2CreateSnapshot(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateSnapshot, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'snapshot'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['snapshotId']
        self._arn.append(self._arn_templates['t4'].format(**self._arn_parts))


class EC2CreateSubnet(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateSubnet, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'subnet'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['subnet']\
                                           ['subnetId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateVolume(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateVolume, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['volumeId']
        self._arn.append(self._arn_templates['t1'].format(**self._arn_parts))


class EC2RunInstances(CreateEvent):
    def __init__(self, event: dict):
        super(EC2RunInstances, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'instance'

        for item in event['detail']['responseElements']['instancesSet']['items']:
            self._arn_parts['resource'] = item['instanceId']
            self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2StartInstances(UpdateEvent):
    def __init__(self, event: dict):
        super(EC2StartInstances, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'instance'

        for item in event['detail']['requestParameters']['instancesSet']['items']:
            self._arn_parts['resource'] = item['instanceId']
            self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))
