from collections import Counter


class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        """ 利用内置counter，借用哈希表完成计数统计 """
        counter = Counter(numbers)
        common_num = counter.most_common(1)[0] if counter.most_common(1) else None
        if common_num and common_num[1] > len(numbers) / 2:
            return common_num[0]
        else:
            return 0

    def sort_and_get_common_number(self, numbers):
        """ 排序后取中位数 """
        numbers.sort()
        half_len = int(len(numbers) / 2)
        common_num = numbers[half_len]
        common_count, other_count = 0, 0
        for num in common_num:
            if num == common_num:
                common_count += 1
            else:
                other_count += 1
            if common_count > half_len:
                return common_num
            if other_count > half_len:
                return 0


if __name__ == '__main__':
    test = [1,1,2,2,2]
    print(Solution().MoreThanHalfNum_Solution(test))