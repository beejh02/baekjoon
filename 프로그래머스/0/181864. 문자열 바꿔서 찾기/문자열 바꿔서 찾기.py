def solution(myString, pat):
    
    changed = ""
    
    for ch in myString:
        if ch == 'A':
            changed += 'B'
        else:
            changed += 'A'
    
    if pat in changed:
        return 1
    else:
        return 0