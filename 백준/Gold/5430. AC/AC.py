import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().strip()
    capacity = int(input())
    arr = input().strip()

    if capacity > 0:
        real = arr[1:-1].split(',')
    else:
        real = []

    queue = deque(real)
    direction = True
    is_error = False

    for item in string:
        if item == 'R':
            direction = not direction
        elif item == 'D':
            if not queue:
                print("error")
                is_error = True
                break
            
            if direction:
                queue.popleft()
            else:
                queue.pop()

    if not is_error:
        if not direction:
            queue.reverse()
        print("[" + ",".join(queue) + "]")