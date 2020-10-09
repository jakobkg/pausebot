# pausebot
A Slack bot that let's you signify to your colleagues that you're taking a 15 or 30 minute break 

## TODO
- [x] Basic responses and announcement of breaks
- [ ] Generalize code to work in any Slack workspace, not just our specific one
- [ ] Cleanups/consistent naming conventions for methods and variables
- [ ] Queue system
* - [ ] Methods for adding and removing people from the queue
* - [ ] Timers for knowing when to step through the queue
* - [ ] Sending users late responses via the temporary response hooks provided by Slack
* - [ ] Management functions like whether multiple people can take breaks at the same time
* - [ ] Allow users to swap their queue positions in case someone won't be able to take their break on time