import sys
N = int(input())

def top(n):
    sys.stdout.write('@'*n+'   '*n+'@'*n+'\n')
    sys.stdout.write('@'*n+'   '*n+'@'*n)

def middle(n):
    sys.stdout.write('@@@@@'*n)

def middle_2(n):
    sys.stdout.write('@'*n+'   '*n+'@'*n)


for i in range(N):
    top(N)
    sys.stdout.write('\n')

for i in range(N):
    middle(N)
    sys.stdout.write('\n')

for i in range(N):
    middle_2(N)
    sys.stdout.write('\n')

for i in range(N):
    middle(N)
    sys.stdout.write('\n')