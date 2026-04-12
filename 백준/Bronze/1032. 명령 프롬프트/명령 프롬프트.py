import sys

n = int(sys.stdin.readline())
standard = list(sys.stdin.readline().strip())
slen = len(standard)

for _ in range(n - 1):
    next = sys.stdin.readline().strip()
    for i in range(slen):
        if standard[i] != next[i]:
            standard[i] = '?'

print("".join(standard))