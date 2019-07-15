import operator


class Solution:

    def PrintMinNumber(self, numbers):
        self.quick_sort(numbers, 0, len(numbers)-1)
        numbers_str = [str(x) for x in numbers]
        return "".join(numbers_str)

    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]

        while low < high:
            while low < high and self.compareTo(array[high], key, True):
                high -= 1
            array[low] = array[high]
            array[high] = key

            while low < high and self.compareTo(array[low], key, False):
                low += 1
            array[high] = array[low]
            array[low] = key

        self.quick_sort(array, left, low - 1)
        self.quick_sort(array, low + 1, right)

    def compareTo(self, value1, value2, gt):
        compare_value1 = str(value1)+str(value2)
        compare_value2 = str(value2)+str(value1)
        if gt and (operator.gt(compare_value1, compare_value2) or operator.eq(compare_value1, compare_value2)):
            return True
        elif not gt and (operator.lt(compare_value1, compare_value2) or operator.eq(compare_value1, compare_value2)):
            return True
        return False
