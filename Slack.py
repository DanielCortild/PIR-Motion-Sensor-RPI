from slackclient import SlackClient
import time
import os
import psutil
import grovepi

slack_token = os.environ.get('SLACK_BOT_TOKEN')
BOT_TOKEN = slack_token
sc = SlackClient(slack_token)
CHANNEL_NAME = "pir_motion"

if sc.rtm_connect(with_team_state=False):
	print "starting...."
	sc.api_call(
	"chat.postMessage",
	channel = CHANNEL_NAME,
	text    ="Bon on allume"
	)
