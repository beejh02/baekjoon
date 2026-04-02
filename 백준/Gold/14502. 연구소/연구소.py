from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
original = []
virus_pos = []
empty_pos = []

for i in range(n):
    row = list(map(int, input().split()))
    original.append(row)
    for j in range(m):
        if row[j] == 2:
            virus_pos.append((i, j))
        elif row[j] == 0:
            empty_pos.append((i, j))

queue = deque([])

def bfs(map_copy, que):
    que.clear()
    for pos in virus_pos:
        que.appendleft(pos)

    while que:
        y, x = que.pop()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and map_copy[ny][nx] == 0:
                map_copy[ny][nx] = 2
                que.appendleft((ny, nx))

ans = 0
empty_cnt = len(empty_pos)

for i in range(empty_cnt):
    for j in range(i + 1, empty_cnt):
        for k in range(j + 1, empty_cnt):
            temp_map = [row[:] for row in original]
            
            y1, x1 = empty_pos[i]
            y2, x2 = empty_pos[j]
            y3, x3 = empty_pos[k]
            
            temp_map[y1][x1] = 1
            temp_map[y2][x2] = 1
            temp_map[y3][x3] = 1
            bfs(temp_map, queue)
            
            score = 0
            for row in temp_map:
                score += row.count(0)
            
            if score > ans:
                ans = score

print(ans)