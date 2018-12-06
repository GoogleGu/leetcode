# author: Arthur Gu
# date: 2018.12.5

from collections import Counter


def score(dices):
    """
    给骰子结果进行打分
    入参为骰子的结果数列，返回骰子结果数列对应的总分
    """
    dice_results = dices.copy()
    dice_count = Counter(dice_results)
    total_score = 0
    # 为三连打分
    for num, count in dice_count.items():
        # 如果找到了三连，打分并处理骰子数组
        if count >= 3:
            total_score += 1000 if num == 1 else num * 100
            for _ in range(3):
                dice_results.remove(num)
    # 为单1和单5打分
    if dice_results:
        dice_count = Counter(dice_results)
        total_score += dice_count.get(1, 0) * 100
        total_score += dice_count.get(5, 0) * 50
    return total_score


def score_improved(dices):
    """
    比上一种方法优化了计算过程，只需遍历一次counter，且不需创建新结果数列以及从结果数列中移除已打分的骰子
    复杂度O(M+N)
    """
    triplet = [0, 1000, 200, 300, 400, 500, 600]
    lone = [0, 100, 0, 0, 0, 50, 0]
    total_score = 0
    dice_count = Counter(dices)
    for num, count in dice_count.items():
        total_score += triplet[num] * int(count/3) + lone[num] * (count % 3)
    return total_score


def score_online(dices):
    """
    比上一种方法优化了计算过程，不使用Counter，且不需创建新结果数列以及从结果数列中移除已打分的骰子
    复杂度O(N)
    """
    triplet = [0, 1000, 200, 300, 400, 500, 600]
    lone = [0, 100, 0, 0, 0, 50, 0]
    count = [0, 0, 0, 0, 0, 0]
    sum = 0
    for i in dices:
        if count[i] == 2:
            sum += triplet[i] - lone[i] * 3
            count[i] = 0
        else:
            sum += lone[i]
            count[i] += 1
    return sum


if __name__ == '__main__':
    print(score_improved([1, 3, 2, 1, 2, 5]))
