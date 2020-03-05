# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        numbers = [str(num) for num in numbers]
        quick_sort(numbers, 0, len(numbers)-1)
        return int(''.join(numbers))


def quick_sort(array, first, last):
    if first < last:
        index = partition(array, first, last)
        quick_sort(array, first, index-1)
        quick_sort(array, index+1, last)


def partition(array, first, last):
    pivot = array[last]
    i = first-1
    for j in range(first, last):
        if former_is_smaller(array[j], pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[last] = array[last], array[i+1]
    return i + 1


def former_is_smaller(former, latter):
    return former + latter <= latter + former


if __name__ == '__main__':
    number = Solution().PrintMinNumber([2, 21, 234])
    print(number)
