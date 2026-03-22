import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = []
queue = deque([])

for i in range(h):
    layer = [list(map(int, input().split())) for j in range(n)]
    for j in range(n):
        for k in range(m):
            if layer[j][k] == 1:
                queue.append([i, j, k])
    arr.append(layer)

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

while queue:
    curh, cury, curx = queue.popleft()
    for dh, dy, dx in directions:
        nh, ny, nx = dh + curh, dy + cury, dx + curx
        if 0 <= nh < h and 0 <= ny < n and 0 <= nx < m and arr[nh][ny][nx] == 0:
            arr[nh][ny][nx] = arr[curh][cury][curx] + 1
            queue.append([nh, ny, nx])

cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            cnt = max(cnt, arr[i][j][k])

print(cnt - 1)