# RapidSMS messaging
# testing through put for message sending in kannel
import urllib

num_base = 8675309

STRESS_TEST_RANGE = [i for i in range(10,100000,1000)]


#logfile = file()
TIME = []

def send_text(num=10):
    url="http://localhost:13013/cgi-bin/sendsms?from=1234&username=kannel&password=kannel&to=%s&smsc=dmark&text=hello+world"
    url = url%"+".join([str(num_base+i) for i in range(0,num)])
    f = urllib.urlopen(url)
    f.read()

if __name__ == "__main__":
    import time
    for i in STRESS_TEST_RANGE:
        t1 = time.time()
        send_text(num=i)
        t2 = time.time()
        print "done sending %d messages %f"% (i,t2-t1)