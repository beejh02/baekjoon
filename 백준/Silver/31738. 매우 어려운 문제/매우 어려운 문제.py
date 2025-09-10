import sys

N, M = map(int, sys.stdin.readline().split())
 
if N >= M :
    sys.stdout.write("0")
else :
    temp = 1
    for i in range(1, N + 1) :
        temp *= i
        temp %= M
        
    sys.stdout.write(str(temp))