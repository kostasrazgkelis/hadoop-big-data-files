import sys

current_ip = None
current_time = "0"
ip = None
timeSet = []

thisdict = {

}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    tmp = line.split(" ", 1)

    IP = tmp[0]
    time = tmp[1]
    thisdict[str(IP)] = str(time)
    print("----")
    print(thisdict)


totalTime = len(set(timeSet))

# do not forget to output the last word if needed
print('%s\t%s' % (ip, totalTime))
