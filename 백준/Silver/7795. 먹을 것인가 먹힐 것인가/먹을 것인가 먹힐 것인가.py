import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a_group = list(map(int, input().split()))
    b_group = list(map(int, input().split()))

    b_group.sort()
    
    total_count = 0
    
    for a in a_group:
        left = 0
        right = m - 1
        current_count = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if b_group[mid] < a:
                current_count = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        
        total_count += current_count
    
    print(total_count)