def solution(n, words):
    arr = set()
    endChr = words[0][0]

    for index, value in enumerate(words):
        if (index > 0 and value[0] != endChr) or (value in arr):
            return [(index % n) + 1, (index // n) + 1]
        
        arr.add(value)
        endChr = value[-1]

    return [0, 0]