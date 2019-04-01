class Solution:
    def reOrderArray(self, array):
        ## 重置数组顺序的位置
        j = 0
        for index in range(0, len(array)):
            if array[index] % 2 == 1:
                ## 奇数
                temp = array[index]
                for reset_index in range(index, j, -1):
                    ## 之前的元素向后异味
                    array[reset_index] = array[reset_index-1]
                array[j] = temp
                j += 1
        return array

