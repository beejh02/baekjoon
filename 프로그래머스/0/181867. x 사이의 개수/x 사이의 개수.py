def solution(myString):
    arr = myString.split("x")
    answer = []
    for i in arr:
        answer.append(len(i))
    return answer