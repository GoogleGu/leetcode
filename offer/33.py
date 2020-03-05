# -*- coding:utf-8 -*-
class Solution:

    ugly_numbers = [1]
    total_num = 1

    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0

        base_index = 0
        while self.total_num < index * 2:
            base_num = self.ugly_numbers[base_index]
            self.generate_ugly_number(base_num, 2)
            self.generate_ugly_number(base_num, 3)
            self.generate_ugly_number(base_num, 4)
            self.generate_ugly_number(base_num, 5)
            base_index += 1
        if base_index > 0:
            self.ugly_numbers.sort()
        return self.ugly_numbers[index-1]

    def generate_ugly_number(self, base_num, multiple):
        new_ugly = base_num * multiple
        if new_ugly not in self.ugly_numbers:
            self.ugly_numbers.append(new_ugly)
            self.total_num += 1


if __name__ == '__main__':
    print(Solution().GetUglyNumber_Solution(1500))

