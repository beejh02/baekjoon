is_mul_three = False
zero_presence = False

string = input()
text = []
cnt = 0

for item in string:
    text.append(item)
    if(item == '0'):
        zero_presence = True
    cnt += int(item)

if(cnt % 3 == 0):
    is_mul_three = True


if(not zero_presence or not is_mul_three):
    print(-1)
else:
    text.sort(reverse=True)
    print(''.join(text))