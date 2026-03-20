import sys

s = sys.stdin.readline().strip()

cnt0 = len([m for m in s.split('1') if m])
cnt1 = len([m for m in s.split('0') if m])

print(min(cnt0, cnt1))