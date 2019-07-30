
# -*- coding:utf-8 -*-
class Solution:

    count = 0

    def InversePairs(self, data):
        self.count = 0
        self.divide(data, 0, len(data))
        return self.count % 1000000007

    def divide(self, data, start, end):
        """
        将整个数组拆分，拆分结束后两两归并比较计算其中的逆序对数目。
        """
        length = end - start
        if length == 1:
            pass
        else:
            mid = (start + end) // 2
            left_start, left_end = self.divide(data, start, mid)
            right_start, right_end = self.divide(data, mid, end)
            self.merge_and_count_inver_pairs(data, left_start, left_end, right_start, right_end)
        return start, end

    def merge_and_count_inver_pairs(self, data, left_start, left_end, right_start, right_end):
        """
        将两个相邻数组归并，在归并的过程中计算逆序对数目
        """
        temp = []
        left_index, right_index = left_start, right_start
        # print(left_start, left_end, right_start, right_end)
        for pos in range(left_start, right_end):
            pair_nums = left_end - left_index
            if left_index == left_end:
                temp.append(data[right_index])
                right_index += 1
            elif right_index == right_end:
                temp.append(data[left_index])
                left_index += 1
            else:
                if data[left_index] <= data[right_index]:
                    temp.append(data[left_index])
                    left_index += 1
                else:
                    temp.append(data[right_index])
                    right_index += 1
                    self.count += pair_nums

        for i in range(len(temp)):
            data[left_start + i] = temp[i]


if __name__ == '__main__':
    source = [1, 2, 3, 4, 5, 6, 7, 0]
    pairs_num = Solution().InversePairs(source)
    print(pairs_num)
