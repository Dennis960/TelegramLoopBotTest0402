# The script works fine for multiple hours
# /home/pi/loop.py
# python 3.7.3 (default, Jul 25 2020)
# Raspbian GNU/Linux 10 (buster)
import time
import urllib
import json
import requests #Version 2.22.0

TOKEN = '<Token>' #this should be the token specified by telegram after you created a bot with /newBot at the botFather and gave it a name
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    """Gets the content of the Url in utf-8 format"""
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
def get_json_from_url(url):
    """Returns the repsonse of the url get request in a json format."""
    content = get_url(url)
    js = json.loads(content)
    return js
def get_updates(offset=None):
    """Gets all messages that haven't been processed yet."""
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js
def get_last_update_id(updates):
    """Gets the id of the last message."""
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo(text, chat_id):
    """Sends a message to the given chat"""
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
def check_messages_loop():
    """Constantly checks for new messages for the telegram bot."""
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                for update in updates["result"]:
                    echo(update["message"]["text"], update["message"]["chat"]["id"])
            time.sleep(0.5)
        except Exception as e:
            print(e)
check_messages_loop()
