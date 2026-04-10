import sys

n = int(sys.stdin.readline())
ingredients = []
for _ in range(n):
    ingredients.append(list(map(int, sys.stdin.readline().split())))

min_diff = float('inf')

for i in range(1, 1 << n):
    sinmat = 1
    ssunmat = 0
    
    for j in range(n):
        if i & (1 << j):
            s, b = ingredients[j]
            sinmat *= s
            ssunmat += b
            
    diff = abs(sinmat - ssunmat)
    if diff < min_diff:
        min_diff = diff

print(min_diff)