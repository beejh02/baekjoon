import sys

input_data = sys.stdin.read().split()
ptr = 0

if input_data:
    t = int(input_data[ptr])
    ptr += 1

    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1

        grades = []
        for _ in range(n):
            grades.append([int(input_data[ptr]), int(input_data[ptr+1])])
            ptr += 2

        grades.sort()
        
        cnt = 1
        standard_min = grades[0][1]

        for i in range(1, n):
            if grades[i][1] < standard_min:
                cnt += 1
                standard_min = grades[i][1]

        print(cnt)