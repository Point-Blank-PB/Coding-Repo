import math

perfect_squares = [x ** 2 for x in range(1, 55)]
perfect_squares = set(perfect_squares)

def find_digit_square_sum(x):
    string = str(x)
    if '0' in string:
        return False
    sum = 0
    for digit in string:
        sum += int(digit) ** 2
    return sum in perfect_squares


def is_perfect_square(x):
    for i in range(int(math.sqrt(x)) + 2):
        if i ** 2 == x:
            return True
    return False

for case in range(int(input())):

    n = int(input())
    smallest_number = int('1' * n)
    min_possible_sum = n
    max_possible_sum = n * (9 ** 2)


