from random import randint
import time

count = 0

with open('apache.log','w') as f:
    while count < 20000:
        count  = count + 1
        response = randint(2367,6000000)
        string = '136.159.240.75 - - [19/Jan/2012:19:51:36 +0000] "GET /main/channels.cgi?url=http%3A%2F%2Fwww.telegraph.co.uk%2 Fsport%2Frugbyunion%2F HTTP/1.1" 200 32 "http://www.telegraph.co.uk/sport/rugbyunion/" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.1; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)" ' + str(response) + ' "94zv630" "OK" "C=1 BC=0 BF=0 CU=0 CC=0" "-" "gs_england_rugby (22.848) " "1672251521" "main" "http://www.telegraph.co.uk/sport/rugbyunion/"'
        f.write(string + "\n")
        #time.sleep(5)

    f.close()