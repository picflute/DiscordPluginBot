# DiscordPluginBot
This is a very simple bot for the chat service Discord with plugin functionality over MySQL

## Dependencies
- discord.py (https://github.com/Rapptz/discord.py)
- MySQLdb

## What you also need
- A server with running MySQL on it
- Access to that server
- An account on Discord
- Some knowledge on Python to write extended plugins

## What you could need
- A server, where the script runs from

## Usage
  First of all, either clone, or download the bot.py file.
  After that, edit it and enter your Discord and MySQL credentials, as well as a name for your bot

  If you did that successfully, you can now go on and start adding plugins!

## How do I add a plugin?
You want to get either MySQL Workbench or PHPmyAdmin to insert a new plugin, because Python takes spaces and nls very seriously.

You don't have to fill in id, but all of the other fields. They should be self explanatory.

## What is this action thingy?
This thing decides, what format of plugin you want to use. If you want to create a plugin which just responds to a simple command, like /help or /staff, you want to use 'Text', because then you can enter normal text in the output field

If you want to use the full power of Python in your commands, you can select 'Python'

## NOTE:
Your plugin must contain a `dothis(message):` method!!!
To send a message to your clients from a plugin, you use
```python
dothis(message):
    client.send_message(message.channel, "Whatever you want to send")
```
