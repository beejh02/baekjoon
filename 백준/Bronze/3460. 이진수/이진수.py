T = int(input())

for _ in range(T):
    n = int(input())
    binary_str = bin(n)
    reversed_bits = binary_str[::-1]
    positions = []

    for i, bit in enumerate(reversed_bits):
        if bit == '1':
            positions.append(str(i))

    print(" ".join(positions))
