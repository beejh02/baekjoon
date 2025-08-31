import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        w, c = map(int, input().split())
        arr.append((w, c))

    best_w, best_c = arr[0]

    for w, c in arr[1:]:
        if w * best_c > best_w * c:
            best_w, best_c = w, c
        elif w * best_c == best_w * c:
            if c < best_c:
                best_w, best_c = w, c
            elif c == best_c:
                if w > best_w:
                    best_w, best_c = w, c

    sys.stdout.write(str(best_c) + '\n')
