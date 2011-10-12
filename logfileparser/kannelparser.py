#!/usr/bin/env python
"""
How to use this
You can chmod kannelparser (i.e. chmod a+x kannelparser.py)

kannelparser.py <a_log_file>
or
./kannelparser.py <a_log_file>

This script takes only one command line argument and it is the name of the log file you want to parse.

Typical log files in Kannel include:
-> smsbox.log
-> bearerbox.log
-> dummy.log
-> access.log

And they are found in the /var/log/kannel path (On Mac, I guess the same can be said for Linux)
"""
import sys
#def change_to_dictionary(line):
#


#count occurence of "sms received" instances in a time X
def count_messages_received(log):
    total = 0
    f = open(log)
    for line in f:
        if "sms received" in line:
            total += 1
    f.close()
    return total