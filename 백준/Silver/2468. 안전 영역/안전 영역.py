import sys
sys.setrecursionlimit(100000)

def DFS(rainfall, nowy, nowx):
    visited[nowy][nowx] = True
    for dy, dx in directions:
        ny, nx = dy+nowy, dx+nowx
        if(0 <= ny < n and 0 <= nx < n and arr[ny][nx] > rainfall and visited[ny][nx] == False):
            DFS(rainfall, ny, nx)


n = int(input())
directions = [(-1,0), (0,1), (1,0), (0,-1)]
arr = []
ans = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
max_height = max(max(_) for _ in arr)


for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                DFS(h, i, j)
                count += 1

    ans = max(ans, count)

print(ans)