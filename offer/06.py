class Solution:

    @staticmethod
    def min_number_in_rotate_array(rotate_array):
        """
        运行时间：666ms
        占用内存：5856k
        """
        if not rotate_array:
            return 0

        first_num = rotate_array[0]
        for current_num in rotate_array[1:]:
            if current_num < first_num:
                return current_num
        return first_num

    def min_number_in_rotate_array_through_binary_search(self, rotate_array):
        """
        运行时间：1019ms
        占用内存：5856k
        """
        # 对空数组返回0
        if not rotate_array:
            return 0

        left_index = 0
        right_index = len(rotate_array)-1
        middle_index = (left_index + right_index) // 2
        #  出现大量相同值的情况，改用遍历
        if (rotate_array[left_index] == rotate_array[right_index]
                and rotate_array[right_index] == rotate_array[middle_index]):
                return self.min_number_in_rotate_array(rotate_array)

        # 通用情况，进行二分查找
        while left_index < right_index-1:
            middle_index = (left_index + right_index) // 2
            if rotate_array[left_index] <= rotate_array[middle_index]:
                left_index = middle_index
            else:
                right_index = middle_index
        return rotate_array[right_index]


if __name__ == '__main__':
    print(Solution().min_number_in_rotate_array_through_binary_search([]))