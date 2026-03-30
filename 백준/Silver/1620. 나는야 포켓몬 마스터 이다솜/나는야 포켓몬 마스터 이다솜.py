import sys

input = sys.stdin.readline

n, m = map(int,input().split())

dict = {}
for i in range(1, n+1):
    dict.update({str(i) : input().rstrip()}) 

reversed_dict = {v: k for k, v in dict.items()}

for i in range(m):
    command = input().rstrip()
    if(command.isdigit()):
        print(dict[command])
    else:
        print(reversed_dict[command])