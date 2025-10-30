import sys

input = sys.stdin.readline

arr = [0 for i in range(100)]
arr[0] = 1
arr[1] = 1

for i in range(2, len(arr)):
    arr[i] = arr[i-2]+arr[i-3]

n = int(input())
for i in range(n):
    sys.stdout.writelines(str(arr[int(input())-1])+'\n')