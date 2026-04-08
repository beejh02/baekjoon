import sys

input = sys.stdin.readline

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    right = 0
    value = 0
    ans = int(1e9)

    while(1):
        if value >= s:
            ans = min(ans, right - left)
            value -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            value += arr[right]
            right += 1

    if ans == int(1e9):
        print(0)
    else:
        print(ans)

if __name__ == "__main__":
    main()