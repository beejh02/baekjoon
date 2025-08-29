import sys

while True:
    n = sys.stdin.readline().strip()
    if n == "0":
        break

    orign = n
    arr = []

    while len(n) != 1:
        temp = 1
        for ch in n:
            temp *= int(ch)
        n = str(temp)
        arr.append(n)

    sys.stdout.write(orign + " " + " ".join(arr) + "\n")
