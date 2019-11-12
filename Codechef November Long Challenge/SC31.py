# STATUS AC(100% ON PYTHON AND PYPY)


def to_binary(s):
    s = s[::-1]
    count = 0
    for J in range(10):
        count += ((2 ** J) * int(s[J]))
    return count


def count_set_bits(x):
    set_bits = 0
    while x > 0:
        x = x & (x-1)
        set_bits += 1
    return i


for case in range(int(input())):
    n = int(input())
    total_xor = 0
    for i in range(n):
        total_xor = total_xor ^ to_binary(input())

    print(count_set_bits(total_xor))
