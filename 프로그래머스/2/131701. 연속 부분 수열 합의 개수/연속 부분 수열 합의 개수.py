def solution(elements):
    n = len(elements)
    results = set()
    
    extended_elements = elements * 2
    
    for i in range(1, n + 1):
        for j in range(n):
            sub_sum = sum(extended_elements[j:j+i])
            results.add(sub_sum)
    
    return len(results)