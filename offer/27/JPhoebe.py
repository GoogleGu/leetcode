# -*- coding:utf-8 -*-
"""
abc
a[bc] --> a[bc][cb]
b[ac] --> b[ac][ca]
c[ab] --> c[ab][ba]

abcd
a[dcd] ...
b[acd] ...

aba
a[ba] --> a[ba][ab]
b[aa] --> b[aa]
a[ab] --> a[ab][ba] \\


"""

class Solution:

    res = []

    def Permutation(self, ss):
        # 初始化结果集，测试时会重复使用这个值
        self.res = []
        array = []
        if ss:
            for c in ss:
                array.append(c)
            self.handle(array, 0, len(array))
        print(sorted(self.res))
        return sorted(self.res)

    @staticmethod
    def has_same(array, start, end):
        for i in range(start, end):
            if array[i] == array[end]:
                return True
        return False

    def handle(self, array, start, end):
        if start == end:
            self.res.append("".join(array))
        else:
            for i in range(start, end):
                # 检查之前是否存在相同的字符，如果存在，则不再交换重复字符
                if not self.has_same(array, start, i):
                    # 将可能性的首字母放在第一位
                    self.swap(array, start, i)
                    self.handle(array, start+1, end)
                    # 恢复原始数据
                    self.swap(array, start, i)

    @staticmethod
    def swap(ss, start, i):
        if start is not i:
            temp = ss[i]
            ss[i] = ss[start]
            ss[start] = temp
