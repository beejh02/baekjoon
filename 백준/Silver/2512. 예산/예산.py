import sys

n = int(sys.stdin.readline())
ask = list(map(int, sys.stdin.readline().split()))
ask.sort()

budget = int(sys.stdin.readline())

left = 0
right = ask[n-1]
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    
    for x in ask:
        if x > mid:
            total += mid
        else:
            total += x
            
    if total <= budget:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)