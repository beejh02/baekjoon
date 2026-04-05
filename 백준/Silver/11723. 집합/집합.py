import sys
input = sys.stdin.readline

def main():
    m = int(input())
    S = 0

    for _ in range(m):
        line = input().split()
        cmd = line[0]
        
        if cmd == "all":
            S = (1 << 21) - 1
        elif cmd == "empty":
            S = 0
        else:
            num = int(line[1])
            if cmd == "add":
                S |= (1 << num)
            elif cmd == "remove":
                S &= ~(1 << num)
            elif cmd == "check":
                print(1 if S & (1 << num) else 0)
            elif cmd == "toggle":
                S ^= (1 << num)

if __name__ == "__main__":
    main()