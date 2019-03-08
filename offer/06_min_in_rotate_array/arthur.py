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
