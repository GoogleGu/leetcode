# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        length = len(A)
        B = []
        for i in range(0, length):
            result = 1
            for j in range(0, length):
                if i == j:
                    continue
                result *= A[j]
            B.append(result)
        return B

    ## B[0]     1、A[1]、A[2] --- A[n-1]
    ## B[1]     A[0]、1、A[2] --- A[n-1]
    ## B[2]     A[0]、A[1]、1 --- A[n-1]
    ## B[---]   A[0]、A[1]、A[2] --- 1 --- A[n-1]
    ## B[n-2]   A[0]、A[1]、A[2] --- A[n-3]、1、A[n-1]
    ## B[n-1]   A[0]、A[1]、A[2] --- A[n-3]、A[n-2]、1

    def multiply(self, A):
        length = len(A)
        B = []
        B.append(1)
        # 先算左下角
        for i in range(1, length):
            B.append(B[i-1] * A[i-1])
            # 计算右上角
        right_temp = 1
        for i in range(length-2, -1, -1):
            right_temp = right_temp * A[i+1]
            B[i] *= right_temp
        return B




print(Solution().multiply([1,2,3,4,5]))
