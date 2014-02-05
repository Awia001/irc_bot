import socket

SERVER = "irc.w3.org"
NICK = "AdamBot"
CHAN = "#coolkids", "#coolkidstest"
username = None
msg = None

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#irc.settimeout(2)
irc.connect((SERVER, 6665))

irc.send("USER test test test test\r\n")
irc.send("NICK " + NICK + "\r\n")
for chan in CHAN:
	irc.send("JOIN " + chan + "\r\n")

while(1):
	buffer = irc.recv(2048)
	if buffer.find("PING") != -1:
		irc.send("PONG " + buffer.split()[1] + "\r\n")
	
	#Message handling!
	status = buffer.split(" ")[1]
	if status == "PRIVMSG":
		username = str(buffer.split(" ")[0].strip(":").split("!")[0])
		msg = buffer.split(":", 2)[2].strip("\r\n")
		location = buffer.split(" ")[2].strip(":")
		print(username + ": " + msg)
		try:
			if msg[0] == "!":
				parts = msg.split(" ")
				cmd = parts[0].strip("!")
				print(cmd)
				#THIS IS WHERE THE COMMANDS START#
				if cmd == "hello":
					irc.send("PRIVMSG " + location +" Hello!\r\n")
				if cmd == "bye":
					irc.send("PRIVMSG " + location +" Bye!\r\n")
				else:
					pass
		except IndexError:
			print("Shiiiiiit")
		print("No Message")
		