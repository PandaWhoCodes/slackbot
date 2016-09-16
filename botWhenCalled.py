import indicoio
from slackclient import SlackClient
import time
BOT_NAME = 'BOT NAME'
indicoio.config.api_key = 'API KEY FOR INDICO'
slack_client = SlackClient('xoxb-KEY ')
BOT_ID='U2C6022NA'
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND='senti'
def handle_command(command, channel):

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
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
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
