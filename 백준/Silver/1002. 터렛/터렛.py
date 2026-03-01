import math

N = int(input())
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    xygap_sq = (x2 - x1)**2 + (y2 - y1) ** 2
    roundgap_sq = (r1 + r2)**2
    diffgap_sq = (r1 - r2)**2
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if xygap_sq == roundgap_sq or xygap_sq == diffgap_sq:
            print(1)
        elif diffgap_sq < xygap_sq < roundgap_sq:
            print(2)
        else:
            print(0)