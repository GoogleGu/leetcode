# author: Arthur Gu
# date: 2018.12.5

def simple_tribonacci(seed, n):
    """
    拷贝一份初始化列表，每次计算出的新结果保存在初始化列表里，实现方式简单易读，推荐用这个。
    """
    result = list(seed.copy())
    if n > 3:
        for i in range(3, n):
            result.append(result[i-3] + result[i-2] + result[i-1])
    return result[:n]


if __name__ == '__main__':
    seed = [1, 1, 1]
    print(simple_tribonacci(seed, 10))

