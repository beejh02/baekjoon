import sys
n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    if(18 in arr and 17 in arr):
        for j in arr:
            sys.stdout.writelines(str(j) + " ")
        print("\nboth")
    elif(18 in arr):
        for j in arr:
            sys.stdout.writelines(str(j) + " ")
        print("\nmack")
    elif(17 in arr):
        for j in arr:
            sys.stdout.writelines(str(j) + " ")
        print("\nzack")
    else:
        for j in arr:
            sys.stdout.writelines(str(j) + " ")
        print("\nnone")
    print("")