import sys
from bisect import bisect_left

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a_group = list(map(int, input().split()))
    b_group = list(map(int, input().split()))

    b_group.sort()
    
    count = 0
    for a_item in a_group:
        count += bisect_left(b_group, a_item)
    
    print(count)