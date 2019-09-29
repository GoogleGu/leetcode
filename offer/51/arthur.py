
# -*- coding:utf-8 -*-
class Solution:

    def multiply(self, A):
        B = []
        forwards = [1]
        backwards = [1]
        for i in range(1, len(A)):
            forwards.append(forwards[i-1] * A[i-1])
            backwards.append(backwards[i-1] * A[-i])

        for i in range(len(A)):
            B.append(forwards[i] * backwards[-i-1])

        return B


if __name__ == '__main__':
    print(Solution().multiply([1,2,3,4,5]))
