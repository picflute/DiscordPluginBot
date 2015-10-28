#!/usr/bin/python
import discord
import MySQLdb as mdb
import sys
import cmd


#Please enter your bot data
email = ''
passwd_discord = ''
nick = ''

#MySQL data
db_server = 'localhost'
db_user = ''
db_pass = ''
db_name = 'amplugins'



client = discord.Client()
client.login(email, passwd_discord)

def main():
	reload_bot()
    client.run()

def reload_bot():
	global name
	global aliases
	global desc
	global output
	global action
	name = []
	aliases = []
	desc = []
	output = []
	action = []
	count = 0
	try:
		con = mdb.connect(db_server, db_user, db_pass, db_name)
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS `plugins` (`id` int(11) NOT NULL,`name` varchar(120) NOT NULL,`author` text NOT NULL,`aliases` text NOT NULL,`description` text NOT NULL,`action` set('Python','Text') NOT NULL DEFAULT 'Text',`output` text NOT NULL,`enabled` tinyint(1) NOT NULL DEFAULT '1') ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1")
		cur.execute("SELECT * FROM plugins WHERE enabled = TRUE")
		for i in range(cur.rowcount):
			row = cur.fetchone()
			print "Plugin enabled: " + row[1] + " by " + row[2]
			name.append(row[1])
			aliases.append(row[3])
			desc.append(row[4])
			action.append(row[5])
			output.append(row[6])
			count = count + 1
		return count
	except mdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return count
	finally:
		if con:
			con.close()

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
def on_message(message):
    if message.content.startswith('/commands') or message.content.startswith('/help'):
    	cntr = 0
    	msg = "Available commands:\n"
        for cmd in aliases:
        	msg = msg + cmd + "\t\t\t\t\t" + desc[cntr] + "\n"
        	cntr = cntr + 1
        client.send_message(message.channel, msg)
    elif(message.content.startswith('/reload')):
    	count = str(reload_bot())
    	client.send_message(message.channel, nick + " was reloaded!\nSuccessfully loaded plugins: " + count)
    elif(message.content.split()[0] in aliases):
    	index = aliases.index(message.content.split()[0])
    	if(action[index] == 'Text'):
    		client.send_message(message.channel, output[index])
    	elif(action[index] == 'Python'):
    		exec(output[index], globals())
    		dothis(message)
    elif(message.content.startswith('/')):
    	client.send_message(message.channel, "Unknown command! Please enter /help or /command")

if __name__ == '__main__':
        main()
