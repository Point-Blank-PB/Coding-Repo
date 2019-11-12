# STATUS 100% ON BOTH PYPY3 AND PYTHON3.6
# NOTE: THIS WAS NOT THE BEST IMPLEMENTATION
# it worked because of many minor tweakings that i did in the algorithm

for case in range(int(input())):
    n, m = [int(x) for x in input().split()]
    all_boxes = [int(x) for x in input().split()]

    color_wise_boxes = []
    for j in range(0, n, m):
        for i in range(m):
            try:
                color_wise_boxes.append([all_boxes[i+j], i])
            except IndexError:
                break
    color_wise_boxes.sort()

    initials = {}
    diff = 1e10
    _min = 1e10
    _max = 0
    flag = False

    for box in color_wise_boxes:
        min_flag = False
        try:
            if initials[box[1]] == _min:
                min_flag = True
        except KeyError:
            pass
        initials[box[1]] = box[0]
        if not flag:
            if len(initials) >= m:
                flag = True
        if (initials[box[1]] < _min or initials[box[1]] > _max) and flag:
            if min_flag or _min == 1e10:
                _min = min(initials.values())
            _max = initials[box[1]]
            diff = min(diff, abs(_max - _min))
    print(diff)


# 1
# 11 4
# 16 1 22 4 46 2 7 29 37 11 56