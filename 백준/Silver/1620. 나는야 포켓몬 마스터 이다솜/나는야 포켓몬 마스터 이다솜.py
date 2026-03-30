n, m = map(int,input().split())

dict = {}
command = []
for i in range(1, n+1):
    dict.update({str(i) : input()}) 

reversed_dict = {v: k for k, v in dict.items()}

for i in range(m):
    command = input()
    if(command.isdigit()):
        print(dict[command])
    else:
        print(reversed_dict[command])