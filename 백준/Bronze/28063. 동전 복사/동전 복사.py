N = int(input())
x, y = map(int, input().split())

if N == 1:
    print(0)
elif N == 2:
    print(2)
else:
    if (x == 1 or x == N) and (y == 1 or y == N):
        print(2)  # 꼭짓점
    elif x == 1 or x == N or y == 1 or y == N:
        print(3)  # 가장자리
    else:
        print(4)  # 내부