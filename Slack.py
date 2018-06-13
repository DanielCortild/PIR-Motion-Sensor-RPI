from slackclient import SlackClient
import time
import os
import psutil
import grovepi

slack_token = os.environ.get('SLACK_BOT_TOKEN')
BOT_TOKEN = slack_token
sc = SlackClient(slack_token)
CHANNEL_NAME = "pir_motion"
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

if sc.rtm_connect(with_team_state=False):
	print "starting...."
	sc.api_call(
	"chat.postMessage",
	channel = CHANNEL_NAME,
	text    ="Bon on allume"
	)

while True:
    try:
        # Sense motion, usually human, within the target range
        if grovepi.digitalRead(pir_sensor):
            print 'Motion Detected'
        else:
            print '-'

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.2)

    except IOError:
        print "Error"
