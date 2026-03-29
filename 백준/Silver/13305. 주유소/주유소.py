n = int(input())

length = list(map(int,input().split()))
cost = list(map(int,input().split()))

value = 0

destination = len(length)
length_ptr = 0
cost_ptr = 0

cheap = float('inf')

while(destination != 0):
    if(cost[cost_ptr] < cheap):
        cheap = cost[cost_ptr]
        value += cheap * length[length_ptr]
        destination -= 1
        cost_ptr += 1
        length_ptr += 1
    else:
        value += cheap * length[length_ptr]
        destination -= 1
        cost_ptr += 1
        length_ptr += 1

print(value)