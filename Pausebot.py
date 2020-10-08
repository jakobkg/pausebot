import os
import pytz
from enum import IntEnum, unique
from datetime import datetime, timedelta
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
    User's Slack ID [String]
    Type of pause the user is taking [Pause]
    When the user's pause is over [datetime object?]
    """

    m_DisplayName: str
    m_UserID: str
    m_PauseType: Pause
    m_PauseEnd: datetime

    def __init__(self, id: str, pause: Pause, pauseEnd: datetime) -> None:
        self.m_UserID = id
        self.m_PauseType = pause
        self.m_PauseEnd = pauseEnd

    def getPauseEnd(self):
        """
        Returns the datetime object of the end of the user's pause [datetime object]
        """

        return self.m_PauseEnd

    def getPauseType(self):
        """
        Returns the type of pause the user is taking [Pause]
        """

        return self.m_PauseType

    def getUserID(self) -> str:
        """
        Return the user ID if this Slack user
        """
        return self.m_UserID

    def tagUser(self) -> str:
        """
        Insert this into a message to tag the user in the message on Slack
        """
        return '<@' + self.m_UserID + '>'

class Pausebot():
    """
    The bot! Should store:
    Pause queue [list of User]
    The Slack client? [WebClient]
    Methods for parsing and processing input from Slack
    Methods for responding to Slack
    Methods for managing the pause queue
    """

    m_PauseQueue: User
    m_client: WebClient

    def __init__(self, client: WebClient) -> None:
        self.m_client = client
        self.m_PauseQueue = []

    def parse_command(self, requestDict: dict) -> str:
        """
        Parse the Slack POST message of a triggered /slash command,
        and call the appropriate handling method
        """

        validChannels = ['b2c_pt_pause', 'pausebot_testkanal', 'privategroup'] if DEBUG_FLAG else ['b2c_pt_pause']

        if requestDict['channel_name'] not in validChannels:
            return 'Feil kanal! Jeg svarer bare i #b2c_pt_pause'

        pause = Pause.Lunch if requestDict['command'] == '/lunsj' else Pause.Break
        pauseEnd = datetime.now(pytz.timezone('Europe/Oslo')) + timedelta(minutes=pause)

        initiator = User(id=requestDict['user_id'], pause=pause, pauseEnd=pauseEnd)

        self.m_client.chat_postMessage(channel=requestDict['channel_id'], text=self.__acknowledge_pause(initiator))

        return self.__acknowledge_pause(initiator)

    def __acknowledge_pause(self, user: User) -> str:
        """
        Send a response to let the user know that their pause has been registered
        """

        pauseString = 'pause' if user.getPauseType().name == 'Break' else 'lunsj'
        pauseEndString = user.getPauseEnd().strftime('%H:%M')

        return 'Ok, ' + user.tagUser() + ' har ' + pauseString + ' til ' + pauseEndString

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

flaskApp = Flask(__name__)


@flaskApp.route('/', methods=['POST'])
def pass_to_bot():
    slashcommandDict = request.form
    if DEBUG_FLAG:
        print('==== SLACK POST REQUEST RECEIVED ===')
        print('Contents:')
        for item in slashcommandDict.items():
            print(item)

    botResponse = bot.parse_command(slashcommandDict)
    return jsonify(ok=True, text=botResponse)


if __name__ == '__main__':
    flaskApp.run()
