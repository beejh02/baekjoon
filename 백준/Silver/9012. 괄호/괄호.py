def check(s):
    for i in range(len(s)):
        if(s[i] == "("):
            stack.append(s[i])
        else:
            if(stack):
                stack.pop()
            else:
                return False
    if(stack):
        return False
    return True

n = int(input())

for i in range(n):
    string = input()
    stack = []

    if(check(string)):
        print("YES")
    else:
        print("NO")