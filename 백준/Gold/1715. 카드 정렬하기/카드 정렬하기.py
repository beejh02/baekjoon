import heapq
import sys

n = int(sys.stdin.readline())
result = 0
cards = []

for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

while(len(cards) > 1):
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    result += temp
    heapq.heappush(cards, temp)

sys.stdout.writelines(str(result))