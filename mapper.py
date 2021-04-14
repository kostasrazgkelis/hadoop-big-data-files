import sys
from datetime import datetime

# input comes from STDIN (standard input)

for line in sys.stdin:

    line = line.strip()

    data = line.split(',')

    if not ( data[0] == 'ip' or data[1] == 'date' or data[2] == 'time' ):
        IP = data[0]
        date = data[1].split('-')
        time = data[2].split(':')

        b = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
        timestamp = int(datetime.timestamp(b))

        value = timestamp - timestamp % 60
        print('%s\t%s' % (IP, value))
