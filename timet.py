import time
import argparse
from datetime import datetime
from tzlocal import get_localzone # $ pip install tzlocal
import pytz


def print_time(time_input):
    time_val = datetime.fromtimestamp(time_input)
    print(time_val.astimezone(get_localzone()))
    utc = pytz.utc
    print(time_val.astimezone(utc))


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--timestamp", help="optional unix timestamp to parse", type=int)
args = parser.parse_args()

if args.timestamp:
    try:
        print_time(int(args.timestamp))
    except ValueError:
        print("oooooooo, too big to be seconds, trying as milliseconds")
        print_time(int(args.timestamp)/1000)
else:
    print(int(time.time()))