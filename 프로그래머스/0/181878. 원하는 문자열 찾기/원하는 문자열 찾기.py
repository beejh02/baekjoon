def solution(myString, pat):
    answer = myString.upper()
    
    if(pat.upper() in answer):
        return 1
    else:
        return 0