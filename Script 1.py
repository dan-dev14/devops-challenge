'''
Dan Bartram

A script that "watches" the apache log file and only prints out lines that correspond to
slow requests (slow being more 1 second) as they are logged

'''

import time

convert = lambda n: n / 1000


def parse(line):
    #Function to take the raw log and extract the RTT
    parsed = line.split('"')
    return parsed[6].strip()


def listen():
    #Open the apache log file, find the end, and track what is written to it...
    #Using yield to give us what we need on the fly.
    file = 'apache.log'
    with open(file) as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield (line.strip())


if __name__ == '__main__':
    for log in listen():
        #Loop round what yield gives us and only print if it's above 1000ms (1 second)
        response = parse(log)
        if convert(int(response)) > 1000:
            print(log)
