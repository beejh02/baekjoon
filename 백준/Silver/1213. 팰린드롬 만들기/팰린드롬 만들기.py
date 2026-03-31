import sys

string = sys.stdin.readline().strip()
spel = sorted(list(set(string)))

odd_count = 0
odd_char = ""
half = ""

for s in spel:
    count = string.count(s)
    if count % 2 != 0:
        odd_count += 1
        odd_char = s
    
    if odd_count > 1:
        break
    
    half += s * (count // 2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(half + odd_char + half[::-1])