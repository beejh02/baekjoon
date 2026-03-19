import heapq

n = int(input())
result = 0
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

while(len(cards) > 1):
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    result += temp
    heapq.heappush(cards, temp)

print(result)