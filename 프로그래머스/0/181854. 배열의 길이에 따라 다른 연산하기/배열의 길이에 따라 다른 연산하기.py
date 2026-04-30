def solution(arr, n):
    start = 0
    jump = 2
    
    if len(arr) % 2 == 0:
        start = 1
        jump = 2
    
    for i in range(start, len(arr), jump):
        arr[i] += n
    
    return arr