# author: Arthur
# date: 2018.12.24


cancel = {
    'EAST': 'WEST',
    'WEST': 'EAST',
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
}


def dirReduc(path):

    removal_slices = []
    # 遍历一遍获取要消减的数据
    i = 0
    while i < len(path)-1:
        if cancel[path[i]] == path[i+1]:
            removal_slices.append([i, i+1])
            i += 2
        else:
            i += 1

    return path

