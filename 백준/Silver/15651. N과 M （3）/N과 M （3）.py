n, m = map(int,input().split())

arr = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        arr.append(i)
        dfs(depth + 1)
        arr.pop()

dfs(0)