This is a series of testing and benchmarking scripts for kannel. With these scripts,
you can tweak your kannel settings off of real data...

### Setup

This assumes that you have set up Kannel correctly. Using Linux, you can start the following sequence of steps

 * /usr/lib/kannel/test/test_http_server -p 20022
 * /usr/sbin/bearerbox /etc/kannel/kannel.conf
 * /usr/sbin/smsbox /etc/kannel/kannel.conf

### Prerequisites to running the test

You will get the best results if you flush out your existing logs, restart your smsbox/bearerbox and start "CLEAN".

Logs to flush out or clear include:
 * /var/log/kannel/smsbox.log
 * /var/log/kannel/bearerbox.log

 Note: location for these logs might be a lot different from system to system.

 ### Running the test

 When kannel has restarted successfully, run `speedtest.py`; posting to `kannel` will take a short while, now,
 the wait begins before you actually run the second test found inside `logfileparser/kannelparser.py`

 
