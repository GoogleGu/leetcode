# author: Arthur
# date: 2018.12.13


def choose_best_sum(k, t, ls):

    def sub_best(left_distances, left_towns, n_towns):
        best = 0
        # 如果只有一个城镇可去
        if left_distances <= 0:
            return 0
        if left_towns == 1:
            for town in ls[:n_towns]:
                if best < town <= left_distances:
                    best = town
        # 如果还有多个城镇可去
        else:
            if n_towns == left_towns:
                best = sum(ls[:n_towns]) if sum(ls[:n_towns]) <= left_distances else 0
            elif n_towns > left_towns:
                # 不选当前城镇
                best_sum_if_forfeit_current = sub_best(left_distances, left_towns, n_towns-1)
                # 选当前城镇
                best_sum_if_choose_current = 0
                if ls[n_towns-1] <= left_distances:
                    temp = sub_best(left_distances - ls[n_towns-1], left_towns - 1, n_towns-1)
                    if temp != 0:
                        best_sum_if_choose_current = ls[n_towns-1] + temp
                best = max(best_sum_if_forfeit_current, best_sum_if_choose_current)
        return best

    best_sum = sub_best(k, t, len(ls))
    return best_sum if best_sum else None


if __name__ == '__main__':
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    print(choose_best_sum(230, 4, xs))
    print(choose_best_sum(430, 5, xs))
    print(choose_best_sum(430, 8, xs))
    print(choose_best_sum(5, 2, [6, 4, 3, 4, 5, 9]))
