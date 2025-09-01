def solution(n, k):
    arr = []
    i = 1
    while(1):
        if((k*i) <= n):
            arr.append(k*i)
        else:
            break
        i += 1
    return arr