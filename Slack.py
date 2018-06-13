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

mouv = 0

while True:
    try:
        if grovepi.digitalRead(pir_sensor):
            mouv = mouv+1
        else:
            if mouv > 0:
				mouv = mouv-1

        if mouv == 10:
			print("Mouvmement")
			send()
			mouv=0
			time.sleep(30)

        time.sleep(.2)


    except IOError:
        print "Error"
