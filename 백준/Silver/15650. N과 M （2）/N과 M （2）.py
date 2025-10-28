from itertools import combinations

n, m = map(int,input().split())

n = [i+1 for i in range(n)]
arr = combinations(n,m)

for i in arr:
    print(*i)