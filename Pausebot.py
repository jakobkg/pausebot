import os
from enum import IntEnum, unique
from datetime import datetime, time
from flask import Flask, jsonify, request
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
    Class for storing users, should contain the following:
    User's display name [String]
    Type of pause the user is taking [Pause]
    When the user's pause is over [datetime object?]
    """

    m_DisplayName: str
    m_PauseType: Pause
    m_PauseEnd: datetime


class Pausebot():
    """
    The bot! Should store:
    Pause queue [list of User]
    The Slack client? [WebClient]
    Methods for input from Slack as outlined below
    Methods for responding to Slack
    Methods for managing the pause queue
    """

    m_PauseQueue: User
    m_client: WebClient

    def __init__(self, client: WebClient) -> None:
        self.m_client = client
        self.m_PauseQueue = []

    def parse_command(self, request_dict):
        """
        Parse the Slack POST message of a triggered /slash command,
        and call the appropriate handling method
        """
        valid_channels = ['b2c_pt_pause']

        if request_dict['channel_name'] not in valid_channels:
            return (True, 'Feil kanal! Jeg svarer bare i #b2c_pt_pause')
        else:
            return (True, 'Hurra, dette er en gyldig kanal')


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


SLACK_BOT_KEY = None
SLACK_AUTH_KEY = None
DEBUG_FLAG = None

try:
    SLACK_BOT_KEY = os.environ['BOTKEY']
except KeyError:
    print('WARNING: Bot API key not found')
    SLACK_BOT_KEY = ""

try:
    SLACK_AUTH_KEY = os.environ['AUTHKEY']
except KeyError:
    print('WARNING: Slack AUTH key not found')
    SLACK_AUTH_KEY = ""

try:
    DEBUG_FLAG = os.environ['PAUSEBOT_DEBUG']
except KeyError:
    pass


bot = Pausebot(WebClient(token=SLACK_BOT_KEY))

flaskapp = Flask(__name__)


@flaskapp.route('/', methods=['POST'])
def pass_to_bot():
    slashcommand_dict = request.form
    if DEBUG_FLAG:
        print('==== SLACK POST REQUEST RECEIVED ===')
        print('Contents:')
        for item in slashcommand_dict.items():
            print(item)

    botresponse = bot.parse_command(slashcommand_dict)
    return jsonify(ok=botresponse[0], text=botresponse[1])


if __name__ == '__main__':
    flaskapp.run()
