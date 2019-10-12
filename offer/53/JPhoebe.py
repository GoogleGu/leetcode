# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):

        for char in s:
            ## 判断字符是否合法
            if not ((char>='0' and char <= '9') or char=='e' or char=='E' or char=='+' or char=='-'or char=='.'):
                return False
        ## +/-/E不能再最后
        if s[-1] == '+' or s[-1] == '-' or s[-1] == 'E' or s[-1] == 'e':
            return False
        ## 小数点
        if s.find('.') != s.rfind('.'):
            return False
        for i in range(1, len(s)-1):
            ## 正负号在中间，前面是e/E, 后面数字
            if s[i] == '+' or s[i] == '-':
                if not(s[i-1] == 'e' or s[i-1] == 'E') or not(s[i+1]>='0' and s[i+1]<='9'):
                    return False
            ## e后面不能是小数，入12E+4.3
            if s[i] == 'E' or s[i] == 'e':
                if s[i:].find('.') != -1:
                    return False
        return True
