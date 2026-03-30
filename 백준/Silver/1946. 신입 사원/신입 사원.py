import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    grades = [tuple(map(int, input().split())) for _ in range(n)]

    grades.sort()
    
    cnt = 1
    standard_min = grades[0][1]

    for i in range(1, n):
        if grades[i][1] < standard_min:
            cnt += 1
            standard_min = grades[i][1]

    print(cnt)