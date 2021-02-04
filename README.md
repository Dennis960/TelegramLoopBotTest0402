# TelegramLoopBotTest0402

This script runs a python loop that waits until the telegram bot got a new message.
It will echo back the message to the user who sent it.
After running it for ~11 hours on a Raspberry pi 2B the echo doesn't work. The process doesn't stop but it doesn't make any more http requests as well.

Setup:
pip install requests (version 2.22.0)
Go to telegram, find botFather, /newBot, give it a name and receive the <Token>
put the Token into the loop.py script
run the script (on a raspberry pi) and wait a few hours.

If anybody knows why the process stops or what is happening, please tell me :)
