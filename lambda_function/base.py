# coding: utf-8

"""
This Python module contains all the abstract classes used for event parsing.
"""

import abc


class EventError(Exception):
    """ Generic exception for error handling """
    pass


class BaseEvent(object, metaclass=abc.ABCMeta):
    """ Abstract Event base class """

    def __init__(self, event: dict):

        # Security check - We only handle CloudTrail Event
        if 'AWS API Call via CloudTrail' not in event['detail-type']:
            raise EventError(f'Event was not sent by CloudTrail. Skip it. '
                             f'Detail-type: {event["detail-type"]}')

        self._event = event  # Store the original event
        self._arn = []  # Will contain the ARNs extract from event
        self._tags = {}  # Will contain all the final tags to apply

        # Variables used to build ARNs
        self._arn_parts = {'partition': 'aws',
                           'region': event['region'],
                           'account': event['account']}

        self._arn_templates = {
            't1': 'arn:{partition}:{service}:{region}:{account}:{resource}',
            't2': 'arn:{partition}:{service}:{region}:{account}:{resourcetype}/{resource}',
            't3': 'arn:{partition}:{service}:{region}:{account}:{resourcetype}:{resource}',
            't4': 'arn:{partition}:{service}:{region}::{resourcetype}/{resource}'
        }

        # Will be initialized with the child-classes
        self._event_type = ''

    def __repr__(self):
        return f'{self.__class__.__name__}({self._event["time"]})'

    def __str__(self):
        return str(self._arn_parts)

    @property
    def arn(self) -> list:
        """
        Return the list of ARNs concern by the event
        :return: (list) ARNs
        """
        return self._arn

    @property
    def tags(self) -> dict:
        """
        Set of tags
        :return: (dict) Tags
        """
        self._tags[self._event_type+'By'] = self._event['detail']['userIdentity']['arn']
        self._tags[self._event_type+'At'] = self._event['time']
        self._tags[self._event_type+'From'] = self._event['detail']['sourceIPAddress']
        self._tags[self._event_type+'ID'] = self._event['detail']['eventID']
        return self._tags


class CreateEvent(BaseEvent, metaclass=abc.ABCMeta):
    """ Abstract class used for events that's create new objects """
    def __init__(self, event: dict):
        super(CreateEvent, self).__init__(event)
        self._event_type = 'Create'


class UpdateEvent(BaseEvent, metaclass=abc.ABCMeta):
    """ Abstract class used for events that's update existing objects """
    def __init__(self, event: dict):
        super(UpdateEvent, self).__init__(event)
        self._event_type = 'Update'
