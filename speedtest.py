# RapidSMS messaging
# testing through put for message sending in kannel

from kannel import SmsSender, SmsReceiver

url = "http://localhost:13013/cgi-bin/sendsms?from=1234&username=kannel&password=kannel&to=%s&smsc=dmark&text=hello+world"
num_base = 8675309
url = url % "+".join([str(num_base + i) for i in range (0,1000)])
print url

sender = SmsSender(username="kannel",password="kannel")
sender.send("8675309","hello world")
print "message sent"

#if __name__ == "__main__":
    #from timeit import Timer
    #t = Timer("send_some_texts()", "from __main__ import send_some_texts")
    #print t.timeit()