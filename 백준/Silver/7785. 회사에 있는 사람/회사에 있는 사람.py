n = int(input())

arr = set()

for i in range(n):
    name, state = map(str,input().split())
    if(state == "enter"):
        arr.add(name)
    else:
        arr.discard(name)

arr = list(arr)
arr.sort(reverse=True)

for item in arr:
    print(item)