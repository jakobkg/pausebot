from enum import IntEnum, unique
from slack import WebClient
from slack.errors import SlackApiError


@unique
class Pause(IntEnum):
    """
    An enum for pause types
    """
    Break = 15
    Lunch = 30


class User():
    """
    Abstract class for storing users, should contain the following:
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

def add_to_list(user, pause, pauselist):
    """
    Update the list of users who are currently taking a pause
    """
    pass

def remove_from_list(user, pauselist):
    """
    Remove a user from the list once their pause has ended
    """
    pass

def respond_pauselist(pauselist):
    """
    Respond to the /list command with the list of users currently taking a pause and the end time of their respective pausees
    """
    pass