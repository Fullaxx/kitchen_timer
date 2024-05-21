#!/usr/bin/env python3
#
# naive datetime objects are now deprecated?
# https://blog.miguelgrinberg.com/post/it-s-time-for-a-change-datetime-utcnow-is-now-deprecated

import os
import sys
import time
import signal
import datetime

sys.path.append('.')
sys.path.append('/app')
from mymintimer import MinuteTimer

usleep = lambda x: time.sleep(x/1000000.0)

g_shutdown = False

def signal_handler(sig, frame):
	global g_shutdown
	g_shutdown = True

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def bailmsg(*args, **kwargs):
	eprint(*args, **kwargs)
	sys.exit(1)

def every_60min(r):
	print(f'{r}: 60min')

def every_30min(r):
	print(f'{r}: 30min')

def every_15min(r):
	print(f'{r}: 15min')

def every_10min(r):
	print(f'{r}: 10min')

def every_5min(r):
	print(f'{r}: 5min')

def every_1min(r):
	print(f'{r}: 1min')

if __name__ == '__main__':
	signal.signal(signal.SIGINT,  signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)
	signal.signal(signal.SIGQUIT, signal_handler)

	timer_1min = MinuteTimer()
	timer_5min = MinuteTimer(minutes=5)
	timer_10min = MinuteTimer(minutes=10)
	timer_15min = MinuteTimer(minutes=15)
	timer_30min = MinuteTimer(minutes=30)
	timer_60min = MinuteTimer(minutes=60)
	while not g_shutdown:
		now_z = datetime.datetime.now(datetime.timezone.utc).timestamp()
		now_sec = int(now_z)
		r = now_sec
		if timer_1min.check_for_ding(now_sec):
			every_1min(r)
		if timer_5min.check_for_ding(now_sec):
			every_5min(r)
		if timer_10min.check_for_ding(now_sec):
			every_10min(r)
		if timer_15min.check_for_ding(now_sec):
			every_15min(r)
		if timer_30min.check_for_ding(now_sec):
			every_30min(r)
		if timer_60min.check_for_ding(now_sec):
			every_60min(r)

		usleep(250)
