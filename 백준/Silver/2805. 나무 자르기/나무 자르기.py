import sys

input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
low, high = 0, max(arr)

while(low < high):
    mid = (low+high)//2+1
    s = 0

    for x in arr:
        if x > mid:
            s += x - mid

    if(s >= m):
        low = mid
    else:
        high = mid-1

sys.stdout.write(str(low))