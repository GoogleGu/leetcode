# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        result = {}
        for num in numbers:
            count = 0
            exist = result.__contains__(num)
            if exist:
                count = result[num]
            result[num] = count + 1

        for key, count in result.items():
            if count > length / 2:
                return key
        return 0
    

# 一次循环
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        result = numbers[0]
        count = 1
        last_change_type = 0
        # 它出现的次数比其他所有数字出现的次数的和还要多
        for index in range(1, len(numbers)):
            if result == numbers[index]:
                count += 1
            elif count == 0:
                result = numbers[index]
                count = 1
                # 记录最后一位count的改变类型
                last_change_type = 1
            else:
                count -= 1
            # 记录倒数第二位的数字
            if index == len(numbers) - 2:
                last_temp = result
        # 偶数判断count
        if length % 2 == 0 and count > 0:
            return result
        # todo 如何判断最后一个数是否为重复的数字
        # 记录倒数第二位的数字
        elif length % 2 == 1:
            if count == 1:
                if last_change_type is not 1:
                    print(result)
                    return result
                elif last_change_type == 1 and last_temp == numbers[len(numbers) - 1]:
                    print(result)
                    return result
            elif count > 1:
                print(result)
                return result
        return 0
