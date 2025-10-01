import sys

while(1):
    male, female = map(int,input().split())
    if(male == 0 and female == 0):
        break
    sys.stdout.write(str(male+female)+'\n')
