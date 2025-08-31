import math

a, b = map(int, input().split())

g = math.gcd(a,b)

small, large = [], []
i = 1
while (i*i <= g):
    if(g%i == 0):
        small.append(i)
        if(i*i != g):
            large.append(g//i)
    i += 1

arr = small + large[::-1]

for i in arr:
    print(i, a//i, b//i)
