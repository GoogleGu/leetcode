# author: Arthur
# date: 2018.12.23


def generate_solved_katas(n):
    """ 生成ann和john在第n天时的解题数量表"""
    john_katas = [0]
    ann_katas = [1]
    for i in range(1, n):
        john_katas.append(i - ann_katas[john_katas[i-1]])
        ann_katas.append(i - john_katas[ann_katas[i-1]])
    return john_katas, ann_katas


def john(n):
    return generate_solved_katas(n)[0]


def ann(n):
    return generate_solved_katas(n)[1]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))


if __name__ == '__main__':
    print(john(11))
