import sys

n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        sys.stdout.write("*")
    sys.stdout.write("\n")
    