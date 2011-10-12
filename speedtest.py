# RapidSMS messaging
# testing through put for message sending in kannel
import urllib, time

STRESS_TEST_RANGE = xrange(100,10000,1000)

def send_text(num_base=8675309,numbers=100,*args):
    url="http://localhost:13013/cgi-bin/sendsms?from=1234&username=kannel&password=kannel&to=%s&text=hello+world"
    if args:
        url = url%"+".join([str(num_base+i) for i in args[0]])
    else:
        url = url%"+".join([str(num_base+i) for i in xrange(0,numbers)])
        print "%s"%"+".join([str(num_base+i) for i in xrange(0,numbers)])
    f = urllib.urlopen(url)
    f.read()


def chunkify(tel_numbers,chunks):
    li = []
    for x in xrange(1,tel_numbers,chunks):
        li.append(i for i in xrange(x,x+chunks))
    num_list = []
    for item in li:
        num_list.append([i for i in item])
    return num_list


def send_text_in_chunks(number_of_users=100, chunks_of=10):
    # messages sent to 100 users will be sent in chunks of 10 for every iteration (~1s)
    index = 0
    num_base=8675309
    num_chunks_lists = chunkify(number_of_users,chunks_of)
    total_times = []
    for list_base in num_chunks_lists:
        t1 = time.time()
        send_text(num_base,number_of_users,list_base)
        t2 = time.time()
        total_times.append(t2-t1)
        
    print "#################################################"
    print "Sent a total of %d messages in chunks of %d : Max time<%f>, Min time<%f>"%(number_of_users,chunks_of,max(total_times),min(total_times))


if __name__ == "__main__":
    # sending default (100 messages in chunks of 10)
    send_text_in_chunks()

    # sending 1000 messages in chunks of 100
    send_text_in_chunks(number_of_users=1000,chunks_of=100)

#    for i in STRESS_TEST_RANGE:
#        t1 = time.time()
#        send_text(num=i)
#        t2 = time.time()
#        print "done sending %d messages %f"% (i,t2-t1)