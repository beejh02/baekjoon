n = int(input())
students = input().split()
like_count = {s: 0 for s in students}

for _ in range(n):
    for liked in input().split():
        like_count[liked] += 1

for name, cnt in sorted(like_count.items(), key=lambda x: (-x[1], x[0])):
    print(name, cnt)