def arr_split(x, y, size):
    first_color = arr[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first_color:
                half = size // 2
                top_left = arr_split(x, y, half)
                top_right = arr_split(x, y + half, half)
                bottom_left = arr_split(x + half, y, half)
                bottom_right = arr_split(x + half, y + half, half)
                return '(' + top_left + top_right + bottom_left + bottom_right + ')'
    return str(first_color)


N = int(input())
arr = []

for i in range(N):
    arr.append(input())

print(arr_split(0, 0, N))
