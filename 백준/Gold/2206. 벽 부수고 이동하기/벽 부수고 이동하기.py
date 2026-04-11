from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        y, x, broken = queue.popleft()

        if(y == n - 1 and x == m - 1):
            return visited[y][x][broken]

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if(0 <= ny < n and 0 <= nx < m):
                if graph[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                    visited[ny][nx][broken] = visited[y][x][broken] + 1
                    queue.append((ny, nx, broken))
                
                elif graph[ny][nx] == 1 and broken == 0:
                    if visited[ny][nx][1] == 0:
                        visited[ny][nx][1] = visited[y][x][0] + 1
                        queue.append((ny, nx, 1))
    
    return -1

print(bfs())