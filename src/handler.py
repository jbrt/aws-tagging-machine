# coding: utf-8

""" Main module """

import boto3
from lambda_function.factory import EventFactory
from lambda_function.base import EventError


def auto_tagging(event, context):
    """
    Launch the auto-tagging machine
    :param event: (dict) event receive from Lambda/CloudTrail
    :param context: (dict) context of the Lambda function
    :return: (dict) result of the tagging operation
    """

    # With Lambda all stdout messages will be logged to CloudWatch Log.
    # Use a logger here is useless ;)
    print(f'Begin tagging operation with: {event}')

    try:
        # First, let's analyse this event and extract ARN & tag information
        event_handler = EventFactory(event)

        # Then, tag the resource
        client = boto3.client('resourcegroupstaggingapi')
        response = client.tag_resources(ResourceARNList=event_handler.arn,
                                        Tags=event_handler.tags)

    except EventError as error:
        print(error)

    else:
        print(f'Successfully tag the resource: {event_handler}')
        print(f'Tags applied: {event_handler.tags}')
        return response
