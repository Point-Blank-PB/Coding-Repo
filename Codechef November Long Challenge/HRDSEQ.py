series = [-1] * 128
series[0] = 0

for i in range(1, 128):
    flag = series[i-1]
    flag_count = 0
    count = 0
    for x in series[i-1::-1]:
        count += 1
        if x == flag:
            flag_count += 1

            if flag_count == 2:
                break
    if flag_count == 2:
        series[i] = count-1
    else:
        series[i] = 0

for case in range(int(input())):
    n = int(input())
    count = 0
    for x in series[n-1::-1]:
        if x == series[n-1]:
            count += 1
    print(count)
