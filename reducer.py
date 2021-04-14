#!/usr/bin/env python

import sys

current_ip = None
current_time = 0
timeSet = list()
ip = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace

    line = line.strip()

    # parse the input we got from mapper.py
    ip, time = line.split(' ', 1)

    try:
        time = int(time)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if current_ip == ip:
        timeSet.append(time)
    else:
        timeSet.append( time )
        # write result to STDOUT
        if current_ip:
            print('%s\t%s' % (current_ip, len(set(timeSet))))
        current_time = time
        current_ip = ip

if current_ip == ip:
    print('%s\t%s' % (current_ip, len(set(timeSet))))