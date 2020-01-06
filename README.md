# ASL Telegram Notify Bot
Telegram notification bot for connections/disconnections to Allstarlink Node. Note that this is just a notifier bot and is not interactive.

---
## Table of Contents
- [Description](https://github.com/n8acl/asltelegramnotify#Description)
- [Installation/Setup](https://github.com/n8acl/asltelegramnotify#Installation/Setup)
- [Change Log](https://github.com/n8acl/asltelegramnotify#changelog)

---

## Description
[Allstarlink](https://www.allstarlink.org/) (ASL) is a VOIP Ham Radio Application that allows the linking of repeaters and radios and is based on the Asterisk PBX Telephony System.

ASL has a built in ability to run a script on the connection or disconnection of one node to another node. Many node owners use this functionality as a notification method to know when someone connects/disconnects to thier system. This is done via either email or text message, depending on how the owner has the script setup.

This script will notify a node owner via Telegram when there is a connection or disconnection to one of the nodes on their system.

This bot will only send to the chat ID that is entered into the config.py file. So even if this bot is part of a channel/group with other users, only the chat ID of the person that is configured will get it. That is not to say that you could not use the chat ID of a channel or group, but if you want to use an existing bot that you own and don't want it going to everyone, if you put your personal ID in, it will only come to you.

Since ASL only runs on Linux, the instructions here are based on that.

### Credits

The original bot script this is based off is a gist by Github user Lucaspg96. You can check out his original gist by [clicking here](https://gist.github.com/lucaspg96/284c9dbe01d05d0563fde8fbb00db220). I modified it slighty to fit my needs and am sharing that modification here.

___

## Disclaimer
Know that you modify your ASL installation at your own risk. If you break your ASL system, I am not responsible, so make sure to read and make the best decisions for you.

---

## Installation/Setup
First make sure your system is up to date
```bash
sudo apt-get update && sudo apt-get -y upgrade
```

Next you will need to install Python3 and pip3 on your system if they are not already.
```bash
sudo apt-get install python3 python3-pip
```

Next you will need to install the [python-telegram-bot](https://python-telegram-bot.org/) python wrapper library if they aren't already:
```bash
pip3 install python-telegram-bot --upgrade
```
### API Keys Needed
You will need to get API keys from the following:
1. You will need to first either create a Telegram bot or use an existing one you own. If this is your first bot, you can use the [steps here](https://core.telegram.org/bots#6-botfather) and talk to @BotFather to create your bot. 
2. You will also need your Telegram chat id. This can be obtained once your bot is up and running by sending a message to your bot and using the Telegram API by going to this url: [https://api.telegram.org/bot'API-access-token'/getUpdates?offset=0](https://api.telegram.org/bot<API-access-token>/getUpdates?offset=0) replacing 'API-access-token' with your bot access token you obtained in the previous step, sans the single quotes. You will see some json and you will be able to find your ID there in the From stanza.
    * Note that Influx DB provides some examples of what to look for for the above 2 steps as well. You can go to their page by [clicking here](https://docs.influxdata.com/kapacitor/v1.5/event_handlers/telegram/).

### Getting the Script
I recommend downloading just the 3 python files. You can clone the repo, but note that it will overwrite the config.py file each time you update. Updates are easier just downloading the files you need.

Make sure to place them in a folder that you remember. I usually use something like /scripts to keep all my small scripts in. You may want to create a scripts/asltelegramnotify folder to keep all related files in.

Note that you will need to put these files on your ASL node server for them to function properly.

### Configure the Script
Once you have your API Keys, you will need to enter them into the script to make it all work. 

You will need to open the config.py file in your favorite text/Python editor and edit the top portion of the file where it has the keys variables. It looks like this:
```python
# Configure Telegram Keys

my_token = 'YOUR_TELEGRAM_BOT_KEY_TOKEN_HERE' #token that can be generated talking with @BotFather on telegram for your bot
my_chat_id = 'YOUR_CHAT_ID_HERE' # chat_id must be a number!

```

You can test the scripts by using the following command:

```bash
python3 </full/path/to>/asltelegramnotify/conn_bot.py 12345 54321
python3 </full/path/to>/asltelegramnotify/disconn_bot.py 12345 54321
```

You should get a connected and disconnected message from your bot on Telegram.

### Configure Allstarlink
Once you have created your bot (if you are not using an existing one you own already), have the files in place and have updated your tokens in the config.py file, you will now need to configure Allstarlink to use these scripts to notify you.

SSH into your Allstar Node Server (if you are not already) and then you will need to edit the rpt.conf file in the /etc/asterisk folder.

```bash
sudo nano /etc/asterisk/rpt.conf
```

When the editor opens, you will need to find the lines in the node stanza that reference:

* connpgm = 
* discpgm = 

These will have a path after them for an example. This where you will put the following:

```bash
connpgm = python3 </full/path/to>/asltelegramnotify/conn_bot.py
discpgm = python3 </full/path/to>/asltelegramnotify/disconn_bot.py
```

To test these scripts, you can connect to another ASL system and you should get a notification from your bot on Telegram that the node has connected. If you disconnect, you should get a message that your node has disconnected.

These 2 functions automatically send two arguements to your scripts: 
* your node number 
* their Node number

The alert to Telegram is formated as "Node THEIR_NODE connected to YOUR_NODE".

So if their node is 1999 and your node is 12345, you will get a notification similiar to the following example.

Example:
```bash
ALLSTAR ALERT: Node 1999 connected to 12345
```

---

## Change Log
* 01/05/2020 - Initial release 1.0 
