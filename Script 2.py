'''
Dan Bartram

A script that looks at the last 10,000 lines of the file and counts up
a. average response time
b. number of responses slower than 100ms, 500ms and 1s respectively

'''

import os


def tail(file):
    #Using tail to grab us what we need from the file
    lines = os.popen(f'tail -n 10000 {file}').read()
    return lines


convert = lambda n: n / 1000
find_average = lambda list: sum(list) / len(list)


def parse(line):
    #Split up the raw message and return just the RTT
    parsed = line.split('"')
    return parsed[6].strip()


if __name__ == '__main__':
    average = []
    over_100 = 0
    over_500 = 0
    over_1 = 0
    file = 'apache.log'
    lines = tail(file)
    for line in lines.split("\n"):
        try: #Sometimes we might have a blank line or a value out of place, and don't want the script to quit
            response = parse(line)
            if convert(int(response)) > 1000:
                over_1 += 1
            if convert(int(response)) > 500:
                over_500 += 1
            if convert(int(response)) > 100:
                over_100 += 1
            average.append(int(response)) #Add all the values to a list to eval later
        except:
            continue
    average_calc = find_average(average)
    print("Average response time is: {}ms".format(convert(average_calc)))
    print("Response time summary\nOver 100ms: {}\nOver 500ms: {}\nOver 1s: {}".format(over_100, over_500, over_1))
