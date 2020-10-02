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
    
    m_DisplayName : str
    m_PauseType : Pause
    m_PauseEnd : datetime.datetime
    

class Pausebot():
    """
    The bot! Should store:
    Pause queue [list of User]
    Methods for input from Slack as outlined below
    Methods for responding to Slack
    Methods for managing the pause queue
    """

    m_PauseQueue : User
    m_client : WebClient

    def __init__(self, client : WebClient) -> None:
        self.m_client = client
        self.m_PauseQueue = []


    def parse_command(self, command_json):
        """
        Parse the Slack JSON message of a triggered /slash command, and call the appropriate handling method
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


SLACK_BOT_KEY : str
SLACK_AUTH_KEY : str

try:
    with open('slack_bot_key') as f:
        SLACK_BOT_KEY = f.readline()
except FileNotFoundError:
    print('Bot key file not found!')
    quit()

try:
    with open('slack_auth_key') as f:
        SLACK_AUTH_KEY = f.readline()
except FileNotFoundError:
    print('Auth key file not found!')
    quit()

bot = Pausebot(WebClient(token=SLACK_BOT_KEY))

flaskapp = Flask(__name__)

@flaskapp.route('/', method=['POST'])
def pass_to_bot():
    bot.parse_command(request.json)


if __name__ == '__main__':
    flaskapp.run()