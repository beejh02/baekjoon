import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = []
visited = [[False]*n for i in range(n)]
cnt = 0
directions = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(n):
    arr.append(input())

def basic_dfs(y, x, color):
    visited[y][x] = 1

    for dy, dx in directions:
        ny, nx = dy+y, dx+x
        if(0 <= ny < n and 0 <= nx < n):
            if (arr[ny][nx] == color and visited[ny][nx] == False):
                basic_dfs(ny, nx, color)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            basic_dfs(i, j, arr[i][j])
            cnt += 1

print(cnt)

visited = [[False]*n for i in range(n)]
cnt = 0

for i in range(n):
    arr[i] = arr[i].replace('G', 'R')

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            basic_dfs(i, j, arr[i][j])
            cnt += 1

print(cnt)