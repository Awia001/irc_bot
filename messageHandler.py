class messageHandler:
	
	def parseMessage(self, message, irc):
		self.irc = irc
		if message.find("PING") != -1:
			self.irc.send("PONG %s\r\n" % message.split()[1])
	
		#Message handling!
		status = message.split(" ")[1]
		if status == "PRIVMSG":
			username = str(message.split(" ")[0].strip(":").split("!")[0])
			msg = message.split(":", 2)[2].strip("\r\n")
			location = message.split(" ")[2].strip(":")
			print(username + ": " + msg)
			if msg[0] == "!":
				parts = msg.split(" ")
				cmd = parts[0].strip("!")
				
				self.parseCommands(cmd, location, irc)
		
	def parseCommands(self, cmd, location, irc):
		print(cmd)
		#THIS IS WHERE THE COMMANDS START#
		if cmd == "hello":
			irc.send("PRIVMSG " + location +" Hello!\r\n")
		if cmd == "bye":
			irc.send("PRIVMSG " + location +" Bye!\r\n")
		else:
			pass