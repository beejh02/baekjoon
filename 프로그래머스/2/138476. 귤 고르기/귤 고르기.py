from collections import Counter

def solution(k, tangerine):
    counts = sorted(Counter(tangerine).values(), reverse=True)
    total = 0
    types_used = 0
    for c in counts:
        total += c
        types_used += 1
        if total >= k:
            return types_used
    return types_used