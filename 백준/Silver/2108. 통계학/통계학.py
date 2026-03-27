import sys
from collections import Counter

input = sys.stdin.readline

def solve():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))

    nums.sort()

    print(round(sum(nums) / n))

    print(nums[n // 2])

    counts = Counter(nums).most_common()
    if len(counts) > 1 and counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])

    print(nums[-1] - nums[0])

if __name__ == "__main__":
    solve()