# author: Arthur
# date: 2018.12.11

from queue import deque


def ant_bridge(ants, terrain):

    def march_forward(marching_ants, bridge_ants):
        """
        将整个行进蚁前移一格，并拆掉最尾端空闲的桥蚁
        :param marching_ants: 行进蚁队列
        :param bridge_ants: 桥蚁队列
        """
        print(marching_ants, bridge_ants)
        for ant in marching_ants:
            ant[1] += 1
        if len(marching_ants) == 0 or (len(bridge_ants) > 0 and bridge_ants[0][1] < marching_ants[0][1]):
            marching_ants.appendleft(bridge_ants.popleft())

    terrains = '-' + terrain + '-'
    marching_ants = deque([ant, -len(ants)+count+1] for count, ant in enumerate(ants))
    print(marching_ants)
    bridge_ants = deque()
    # 在地形上前进
    for pos in range(1, len(terrains)-1):
        if '.' in terrains[pos-1:pos+2]:
            # 当前位置是坑，拿最前面的行进蚁填坑，其他的前移一步,并检查是否要拆掉最尾端的桥蚁
            leading_ant = marching_ants.pop()
            leading_ant[1] = pos
            bridge_ants.append(leading_ant)
            march_forward(marching_ants, bridge_ants)
        else:
            # 当前位置不是坑，所有行进蚁前移一步，并检查是否要拆掉最尾端的桥蚁
            march_forward(marching_ants, bridge_ants)
    # 到达最右端后，继续行进所有的蚂蚁，直到没有桥蚁为止
    while len(bridge_ants) > 0:
        march_forward(marching_ants, bridge_ants)
    return ''.join(ant[0] for ant in marching_ants)


def best_practice(ants, terrains):
    n_pits = 0
    for pos in range(1, len(terrains) - 1):
        if '.' in terrains[pos-1:pos+2]:
            n_pits += 1
    n_pits = n_pits % len(ants)
    return  ants[-n_pits:] + ants[:-n_pits]


if __name__ == '__main__':
    a = "DCBA"
    t = "-..-"
    print(ant_bridge(a, t))
