from collections import deque
import sys

def main():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        size = int(input())
        start_y, start_x = map(int, input().split())
        des_y, des_x = map(int, input().split())

        if start_y == des_y and start_x == des_x:
            print(0)
            continue

        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        arr = [[0 for _ in range(size)] for _ in range(size)]
        visited = [[False for _ in range(size)] for _ in range(size)]
        
        queue = deque([(start_y, start_x)])
        visited[start_y][start_x] = True

        while(queue):
            nowy, nowx = queue.popleft()
            
            if nowy == des_y and nowx == des_x:
                print(arr[nowy][nowx])
                break
                
            for dy, dx in directions:
                ny, nx = dy + nowy, dx + nowx
                
                if 0 <= ny < size and 0 <= nx < size and not visited[ny][nx]:
                    visited[ny][nx] = True
                    arr[ny][nx] = arr[nowy][nowx] + 1
                    queue.append((ny, nx))

main()