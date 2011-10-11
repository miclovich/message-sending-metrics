# testing through put for message sending in kannel
# RapidSMS messaging

import timeit
from kannel import SmsSender

sender = SmsSender("kannel","kannel")
sender.send("1234566","hello")

if __name__ == "__main__":

	dest = raw_input("Please enter a phone number to receive SMS: ").strip()
	sender = SmsSender(username="user", password="pass")
	sender.send(dest, "Test message")

	class TestReceiver():
		def iGotAnSMS(self, caller, msg):
			msg = "%s says: %s" % (caller, msg)
			sender.send(dest, msg)

	tr = TestReceiver()
	print "Waiting for incomming SMS..."
	SmsReceiver(tr.iGotAnSMS).run()
