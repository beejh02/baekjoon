import sys

string = sys.stdin.readline().rstrip()

arr = [0 for i in range(26)]

for _ in string:
    arr[ord(_)-97] += 1

print(*arr)