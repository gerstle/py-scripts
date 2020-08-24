import time
import argparse
from datetime import datetime
from tzlocal import get_localzone  # $ pip install tzlocal
import pytz

str_format = "%Y-%m-%dT%H:%M:%S%z"


def print_time(time_input):
    time_val = datetime.fromtimestamp(time_input)
    print(time_val.astimezone(get_localzone()))
    utc = pytz.utc
    print(time_val.astimezone(utc))


def print_time_string(input):
    time_val = datetime.strptime(input, str_format)
    utc = pytz.utc
    print(time_val.astimezone(utc))
    print(int(time_val.timestamp()))


parser = argparse.ArgumentParser(description='unix timestamp utility')
parser.add_argument("-t", "--timestamp", help="optional unix timestamp to parse", type=int)
parser.add_argument("-s", "--string", help="optional date time as string to parse - YYYY-mm-ddTHH:MM::SSz")
args = parser.parse_args()

if args.timestamp:
    try:
        print_time(int(args.timestamp))
    except ValueError:
        print("oooooooo, too big to be seconds, trying as milliseconds")
        print_time(int(args.timestamp) / 1000)
elif args.string:
    try:
        print_time_string(args.string)
    except ValueError:
        print("failed to parse string. format - " + str_format)
else:
    print(int(time.time()))
