from enum import IntEnum, unique
from flask import Flask
from slack import WebClient
from slack.errors import SlackApiError


class Pausebot():
    """
    The bot! Should store:
    Pause queue [list of User]
    Current user taking a pause (Maybe just the top element of the pause queue?) [User]
    Methods for input from Slack as outlined below
    Methods for responding to Slack
    Methods for managing the pause queue
    """
    pass

@unique
class Pause(IntEnum):
    """
    An enum for pause types
    """
    Break = 15
    Lunch = 30


class User():
    """
    Class for storing users, should contain the following:
    User's display name [String]
    Type of pause the user is taking [Pause]
    When the user's pause is over [datetime object?]
    """
    pass


def parse_incoming(message):
    """
    Parse incoming message from Slack
    Expected input is the json from the slash command in Slack
    Output is the display name of the user triggering the command and the type of pause the user is taking (15 minute break or 30 minute lunch)
    """
    pass

def acknowledge_pause(user, pause):
    """
    Send a response to let the user know that their pause has been registered
    """
    pass

def add_to_queue(user, pause, pauselist):
    """
    Update the queue of users who are waitinbg for their pause
    """
    pass

def remove_from_queue(user, pauselist):
    """
    Remove a user from the list once their pause has ended
    """
    pass

def respond_pausequeue(pauselist):
    """
    Respond to the queue command with the list of users waiting for their pause
    """
    pass