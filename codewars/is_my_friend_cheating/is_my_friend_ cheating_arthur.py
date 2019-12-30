# author: Arthur
# date: 2018.12.31


def removNb(n):

    total_sum = n * (n + 1) / 2
    removables = set()

    for i in range(1, n+1):
        j = (total_sum - i) / (i + 1.0)
        if j.is_integer() and j <= n:
            removables.add((i, j))
            removables.add((j, i))

    return sorted(list(removables))

if __name__ == '__main__':
    print(removNb(10000))