# slackbot
A slack bot to do sentiment analysis on any group it is invited to. You can change it to work only when its name is mentioned and add more functionality.

# Getting Ready 
`pip install slackclient`

[Go to Slack API Page](https://api.slack.com/)

![alt text](https://www.fullstackpython.com/source/static/img/160604-simple-python-slack-bot/sign-in-slack.png)
![alt text](https://www.fullstackpython.com/source/static/img/160604-simple-python-slack-bot/custom-bot-users.png)
![alt text](https://www.fullstackpython.com/source/static/img/160604-simple-python-slack-bot/starterbot.jpg)

After all this get your API key 
Next you willl need to get your bot's ID 
for that RUN this simple code just once and copy your bot ID 

```import os
from slackclient import SlackClient


BOT_NAME = 'YOUR BOT NAME WHICH YOU GAVE EXAMPLE @SOMETHINGBOT'

slack_client ="YOUR API KEY"


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
```
        
##Replace all the defaults with your API's and ID's and test your bot



