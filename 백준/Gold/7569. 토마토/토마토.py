import sys
from collections import deque

def main():
    input = sys.stdin.readline
    m, n, h = map(int, input().split())

    arr = []
    queue = deque([])
    left = 0

    for i in range(h):
        layer = []
        for j in range(n):
            row = list(map(int, input().split()))
            for k in range(m):
                if row[k] == 1:
                    queue.append((i, j, k))
                elif row[k] == 0:
                    left += 1
            layer.append(row)
        arr.append(layer)

    if left == 0:
        print(0)
        return

    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            curh, cury, curx = queue.popleft()
            
            for dh, dy, dx in directions:
                nh, ny, nx = curh + dh, cury + dy, curx + dx
                
                if 0 <= nh < h and 0 <= ny < n and 0 <= nx < m:
                    if arr[nh][ny][nx] == 0:
                        arr[nh][ny][nx] = 1
                        left -= 1
                        queue.append((nh, ny, nx))
        
        if queue:
            cnt += 1

    if left == 0:
        print(cnt)
    else:
        print(-1)

if __name__ == "__main__":
    main()