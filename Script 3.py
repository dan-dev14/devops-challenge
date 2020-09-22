'''
Dan Bartram

You think you’ve narrowed down the server that might be delivering slow responses,
write a script that:
a. makes a hundred requests (1 per second)
b. shows the average and maximum response times

'''

import argparse
import requests
import time


def send_request(target):
    r = requests.get(target + '/main/channels.cgi?url=http%3A%2F%2Fwww.telegraph.co.uk%2Fsport%2Frugbyunion%2F')
    rtt = r.elapsed.total_seconds()
    return int(rtt)

convert = lambda n: n * 1000
max = lambda list: max(list)
avg = lambda list: sum(list) / len(list)

if __name__ == '__main__':
    #Allows the user to specify which server they think is the problem
    parser = argparse.ArgumentParser()
    parser.add_argument("--server")
    args = parser.parse_args()
    count = 0
    results = [] #Could use a dict here if we were interested in preserving the timings of the requests
    while count < 100: #Loop round for the 100 requests
        count += 1
        print("Sending request {} out of 100".format(count))
        rtt = send_request(args.server)
        results.append(rtt) #Sticking all values into a list to eval later
        time.sleep(1)

    maximum = max(results)
    average = max(results)
    print("Performance report:\nMax: {} ms\nAverage: {} ms\n", format(convert(maximum), convert(average)))
