n, j, l = map(int,input().split())
j += 1
l += 1
cnt = 1

while n > 1:
    if j//2 == l//2:
        break
    else:
        n = n//2
        l //= 2
        j //= 2
        l += 1
        j += 1
        cnt += 1

print(cnt)