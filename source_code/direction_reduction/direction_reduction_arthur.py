# author: Arthur
# date: 2018.12.24
import itertools


cancel = {
    'EAST': 'WEST',
    'WEST': 'EAST',
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
}


def dirReduc(path):
    """ O(MN)"""
    while True:
        reduction_filter = [True for _ in path]
        # 遍历获取要消减的数据
        i = 0
        while i < len(path)-1:
            if cancel[path[i]] == path[i+1]:
                reduction_filter[i] = reduction_filter[i+1] = False
                i += 2
            else:
                i += 1
        if all(reduction_filter):
            break
        path = itertools.compress(path, reduction_filter)

    return path


# ------------  最高票答案 O(N) ------------------ #
# 这个问题本质上配对检测，和检查括号是否匹配是一样的，使用stack来处理是最好的。

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


def highest_vote(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan