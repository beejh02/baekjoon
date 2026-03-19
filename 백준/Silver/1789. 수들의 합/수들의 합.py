n = int(input())
summary = 0
cnt = 0

while(1):
    cnt += 1
    summary += cnt
    
    if summary > n:
        print(cnt - 1)
        break
    elif summary == n:
        print(cnt)
        break