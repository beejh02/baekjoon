import sys

t = int(sys.stdin.readline())

for _i in range(t):
    n = int(sys.stdin.readline())
    itemset = {}

    for i in range(n):
        i, category = sys.stdin.readline().split()
        if category in itemset:
            itemset[category] += 1
        else:
            itemset[category] = 1

    ans = 1
    for count in itemset.values():
        ans *= (count + 1)
        
    print(ans - 1)