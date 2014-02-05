import connection, messageHandler

def fetchAndHandleLoop():
	while(1):
		messageHandler.parseMessage(irc.getBuffer(), irc)

irc = connection.connection()
messageHandler = messageHandler.messageHandler()

irc.connect("irc.w3.org", 6665, "testbot")
irc.joinChannel("#coolkids")

fetchAndHandleLoop()