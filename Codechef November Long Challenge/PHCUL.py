# STATUS ACCEPTED AC(100%) ON PYPY 3.5
# PARTIAL ACCEPTED (50%) ON PYTHON 3.6

import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


for case in range(int(input())):
    p, q = [int(x) for x in input().split()]
    origin = (p, q)
    n, m, k = [int(x) for x in input().split()]

    set_1 = []
    temp = [int(x) for x in input().split()]
    for index in range(0, 2*n, 2):
        set_1.append((temp[index], temp[index+1]))

    set_2 = []
    temp = [int(x) for x in input().split()]
    for index in range(0, 2*m, 2):
        set_2.append((temp[index], temp[index+1]))

    set_3 = []
    temp = [int(x) for x in input().split()]
    for index in range(0, 2*k, 2):
        set_3.append((temp[index], temp[index+1]))

    # print(origin)
    # print(set_1)
    # print(set_2)
    # print(set_3)

    # considering path x -> a -> b -> c
    min_x_to_a = [0] * n
    for i in range(n):
        min_x_to_a[i] = distance(origin, set_1[i])

    min_x_to_b = [0] * m
    for i in range(m):
        min_x_to_b[i] = min([distance(set_2[i], set_1[j]) + min_x_to_a[j] for j in range(n)])

    min_x_to_c = [0] * k
    for i in range(k):
        min_x_to_c[i] = min([distance(set_3[i], set_2[j]) + min_x_to_b[j] for j in range(m)])
    #
    # print(min_x_to_a)
    # print(min_x_to_b)
    # print(min_x_to_c)
    min_d1 = min(min_x_to_c)

    # considering path x -> b -> a -> c
    min_x_to_b = [0] * m
    for i in range(m):
        min_x_to_b[i] = distance(origin, set_2[i])

    min_x_to_a = [0] * n
    for i in range(n):
        min_x_to_a[i] = min([distance(set_1[i], set_2[j]) + min_x_to_b[j] for j in range(m)])

    min_x_to_c = [0] * k
    for i in range(k):
        min_x_to_c[i] = min([distance(set_3[i], set_1[j]) + min_x_to_a[j] for j in range(n)])

    # print(min_x_to_a)
    # print(min_x_to_b)
    # print(min_x_to_c)
    min_d2 = min(min_x_to_c)

    print(min(min_d1, min_d2))
