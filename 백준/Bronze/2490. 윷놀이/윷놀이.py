for i in range(3):
    first, second, third, fourth = map(int,input().split())
    cnt = sum([first, second, third, fourth])

    match cnt:
        case 0:
            print("D")
        case 1:
            print("C")
        case 2:
            print("B")
        case 3:
            print("A")
        case 4:
            print("E")