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

def send():
	if sc.rtm_connect(with_team_state=False):
		print "starting...."
		sc.api_call(
		"chat.postMessage",
		channel = CHANNEL_NAME,
		text    = "Du mouvement..."
		)

while True:
    try:
        if grovepi.digitalRead(pir_sensor):
            send()
        time.sleep(.2)

    except IOError:
        print "Error"
