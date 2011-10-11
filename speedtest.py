# RapidSMS messaging
# testing through put for message sending in kannel

from kannel import SmsSender, SmsReceiver
import random

def send_some_texts(dest="12346"):
    sender = SmsSender(username="kannel", password="kannel")
    sender.send(dest.strip(), "Test message")


# you can run this test using a live modem and if you've got $$ to spend
def send_to_number_of_users(population=100,elements=10):
    # choose a population for random function
    # choose the numbers you want returned, elements.
    if elements <= population:
        destination_numbers = random.sample(xrange(population),elements)
        for num in destination_numbers:
            send_some_texts(dest=str(num))
    else:
        print "choices should not be more than the population size"




if __name__ == "__main__":
    from timeit import Timer        
    t = Timer("send_some_texts()", "from __main__ import send_some_texts")
    print t.timeit()