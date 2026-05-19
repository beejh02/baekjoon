def solution(strArr):
    arr = []
    for i in strArr:
        if("ad" not in i):
            arr.append(i)
            
    return arr