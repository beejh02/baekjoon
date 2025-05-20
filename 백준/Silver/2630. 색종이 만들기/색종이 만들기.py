def checker(x, y, size):
    global white, blue
    color = arr[y][x]
    same = True

    for i in range(y, y+size):
        for j in range(x, x+size):
            if(arr[i][j] != color):
                same = False
                break
            if not same:
                break
    if same:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size//2
        checker(x,y,half)
        checker(x,y+half, half)
        checker(x+half, y, half)
        checker(x+half, y+half, half)

N = int(input())
arr = [[] for i in range(N)]
white = 0
blue = 0

for i in range(N):
    arr[i] = list(map(int,input().split()))

checker(0,0,N)
print(white)
print(blue)