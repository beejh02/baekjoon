import sys
sys.setrecursionlimit(10**6)

directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

def DFS(y, x):
    visited[y][x] = True
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < m and 0 <= nx < n:
            if arr[ny][nx] == 1 and not visited[ny][nx]:
                DFS(ny, nx)

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                DFS(i, j)
                cnt += 1

    sys.stdout.writelines(str(cnt) + "\n")