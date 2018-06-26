# coding: utf-8

"""
Event parsing for EC2
Each class describe a specific EC2 event with it's own data and finally
build an ARN or a list of ARNs.
"""


from lambda_function.base import CreateEvent, UpdateEvent


class EC2CreateDhcpOptions(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateDhcpOptions, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'dhcp-options'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['dhcpOptions']\
                                           ['dhcpOptionsId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateInternetGateway(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateInternetGateway, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'internet-gateway'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['internetGateway']\
                                           ['internetGatewayId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateNetworkAcl(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateNetworkAcl, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'network-acl'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['networkAcl']\
                                           ['networkAclId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateRouteTable(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateRouteTable, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'route-table'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['routeTable']\
                                           ['routeTableId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateSecurityGroup(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateSecurityGroup, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'security-group'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['groupId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateSnapshot(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateSnapshot, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'snapshot'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['snapshotId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


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
        self._arn_parts['resourcetype'] = 'volume'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['volumeId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


class EC2CreateVpc(CreateEvent):
    def __init__(self, event: dict):
        super(EC2CreateVpc, self).__init__(event)
        self._arn_parts['service'] = 'ec2'
        self._arn_parts['resourcetype'] = 'vpc'
        self._arn_parts['resource'] = event['detail']\
                                           ['responseElements']\
                                           ['vpc']\
                                           ['vpcId']
        self._arn.append(self._arn_templates['t2'].format(**self._arn_parts))


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
