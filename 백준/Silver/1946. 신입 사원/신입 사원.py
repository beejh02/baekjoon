import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    grades = []
    for _ in range(n):
        grades.append(list(map(int, sys.stdin.readline().split())))

    grades.sort()
    
    cnt = 1
    standard_min = grades[0][1]

    for i in range(1, n):
        if grades[i][1] < standard_min:
            cnt += 1
            standard_min= grades[i][1]

    print(cnt)