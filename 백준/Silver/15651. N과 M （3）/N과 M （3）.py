import sys
from itertools import product

input = sys.stdin.readline
N, M = map(int, input().split())

digits = [str(i) for i in range(1, N + 1)]
out = []
append = out.append

for tup in product(range(N), repeat=M):
    append(' '.join(digits[i] for i in tup))

sys.stdout.write('\n'.join(out))
