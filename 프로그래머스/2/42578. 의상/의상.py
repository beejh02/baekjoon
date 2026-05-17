def solution(clothes):
    dictionary = {}

    for i, j in clothes:
        if j in dictionary:
            dictionary[j] += 1
        else:
            dictionary[j] = 1
    
    summary = 1

    for i in dictionary.values():
        summary *= (i + 1)

    return summary - 1
        