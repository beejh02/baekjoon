n = int(input())

temp = (~n)+1 & 0xFFFFFFFF
diff = n^temp

print(bin(diff).count('1'))