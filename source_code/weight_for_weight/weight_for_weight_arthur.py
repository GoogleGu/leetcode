# author: Arthur
# date: 2018.12.10


def pythonic_order_weight(strng):
    """ 使用最pythonic的方法 """
    return " ".join(sorted([num for num in strng.split() if num], key=lambda x: (sum(int(c) for c in x), x)))


def order_weight(strng):
    """ 使用自己写的quick sort """
    weighted_nums = [(sum(int(c) for c in num), num) for num in strng.split(' ') if num]
    quick_sort_tuples(weighted_nums, 0, len(weighted_nums)-1)
    return ' '.join(weighted_num[1] for weighted_num in weighted_nums)


def sub_sort(tuples, first, right):
    pivot = tuples[first]
    left = first + 1
    while left <= right:
        while left <= right and tuples[right] >= pivot:
            right -= 1
        while left <= right and tuples[left] <= pivot:
            left += 1
        if left <= right:
            tuples[right], tuples[left] = tuples[left], tuples[right]
    tuples[right], tuples[first] = tuples[first], tuples[right]
    return right


def quick_sort_tuples(tuples, left, right):
    if left < right:
        pivot_index = sub_sort(tuples, left, right)
        quick_sort_tuples(tuples, left, pivot_index - 1)
        quick_sort_tuples(tuples, pivot_index + 1, right)


if __name__ == '__main__':
    source = "123 235 99 81 180"
    print(order_weight(source))

