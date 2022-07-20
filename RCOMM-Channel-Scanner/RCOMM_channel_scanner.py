import lightblue
from signal import signal ,SIGALARM ,alarm
import sys

channel_status = 0
got_timeout = False
timeout = 2

def sig_alarm_handler(signum ,frame):
    global got_timeout
    got_timeout = True

signal(SIGALARM ,sig_alarm_handler)

if len(sys.argv) < 2:
    print("Usage : " + sys.argv[0] + "<addr>")
    sys.exit(0)

for channel in range(1 ,31):
    sock = lightblue.socket()
    got_timeout = False
    channel_status = 0

    try:
        alarm(timeout)
        sock.connect((sys.argv[1] ,channel))
        alarm(0)

        sock.close()
        channel_status = 1

    except IOError:
        pass

    if got_timeout == True:
        print("channel " + str(channel) + " filtered")
        got_timeout = False
    elif channel_status == 0:
        print("channel " + str(channel) + "closed")
    elif channel_status == 1:
        print("channel" + str(channel) + "open")