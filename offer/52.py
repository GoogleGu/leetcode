"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # s='ab' and p='' or
        # s='' and p=''
        if len(pattern) == 0:
            return len(s) == 0

        # s='' and p='a*b*c*'
        if len(s) == 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            return False
        # s='acb' and p='a*.*b*'
        else:
            if len(pattern) > 1:
                # s='acb' and p='ac*'
                if pattern[1] != '*':
                    return (pattern[0] == s[0] or pattern[0] == '.') and self.match(s[1:], pattern[1:])
                # s='acb' and p='a*cb'
                else:
                    if pattern[0] == '.':
                        return self.match(s[1:], pattern) or self.match(s, pattern[2:])
                    if s[0] == pattern[0]:
                        return self.match(s[1:], pattern) or self.match(s, pattern[2:])
                    elif s[0] != pattern[0]:
                        return self.match(s, pattern[2:])
            else:
                return len(s) == 1 and (pattern[0] == '.' or s[0] == pattern[0])


if __name__ == '__main__':
    print(Solution().match('aa', '.'))


