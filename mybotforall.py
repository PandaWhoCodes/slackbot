import indicoio
from slackclient import SlackClient
import time
BOT_NAME = 'pyslack'
indicoio.config.api_key = 'INDICO KEY'
slack_client = SlackClient('xoxb-SOMETHING SOMETHING ')
BOT_ID='YOU GET AFTER RUNNING THE CODE IN README'
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND='senti' #You can have many more. This is just an example 
def handle_command(command, channel): 
    #Command has all the inouts in the particular slack channel
    lol=indicoio.sentiment(command)
    if lol>0.5:
        response = "positive"
    else:
        response =" negative"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):

    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and output['user']!='MY SLACK BOT ID':#We dont want the slack bot to keep replying to its own messages now do we 
                # return text after the @ mention, whitespace removed
                if  AT_BOT in output['text']:
                    return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']

                else:
                    return output['text'].strip().lower(), \
                           output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
