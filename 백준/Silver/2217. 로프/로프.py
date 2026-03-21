import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

temp = 0
for i in range(n):
    current_weight = arr[i] * (n - i)
    if current_weight > temp:
        temp = current_weight

print(temp)