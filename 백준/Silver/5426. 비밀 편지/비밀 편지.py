import sys


input = sys.stdin.readline

play = int(input())

for T in range(play):
    string = input().strip()

    for i in range(1, len(string)+1):
        if(i**2 == len(string)):
            token = i
            break

    arr = []

    for i in range(0, len(string), token):
        arr.append(string[i:i+token])

    for i in range(token, 0, -1):
        for j in range(token):
            sys.stdout.writelines(arr[j][i-1])
    sys.stdout.write("\n")