def solution(s):
    cnt = 0
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i in range(len(s)):
        test_s = s[i:] + s[:i] 
        stack = []
        is_valid = True

        for char in test_s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    is_valid = False
                    break
                stack.pop()

        if is_valid and not stack:
            cnt += 1
    
    return cnt