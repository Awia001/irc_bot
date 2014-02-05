import socket

class connection:
	
	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def connect(self, server, port, nick):
		self.irc.connect((server, port))
		
		self.irc.send("USER test test test test\r\n")
		self.irc.send("NICK %s\r\n" % nick)
		
	def getBuffer(self):
		return self.irc.recv(510)
	
	def joinChannel(self, chan):
		self.irc.send("JOIN %s\r\n" % chan)
	
	def send(self, message):
		self.irc.send(message)