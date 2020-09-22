# devops-challenge

- Script 1
1. A script that "watches" the apache log file and only prints out lines that correspond to
slow requests (slow being more 1 second) as they are logged

- Script 2
2. A script that looks at the last 10,000 lines of the file and counts up
a. average response time
b. number of responses slower than 100ms, 500ms and 1s respectively

- Script 3
3. You think you’ve narrowed down the server that might be delivering slow responses,
write a script that:
a. makes a hundred requests (1 per second)
b. shows the average and maximum response times
