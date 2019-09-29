# -*- coding:utf-8 -*-
class Solution:
    def match(self, s, pattern):
        # 如果s与pattern都为空，则True
        if not s and not pattern:
            return True
        # 如果s不为空，而pattern为空，则False
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 如果s为空，而pattern不为空，则需要判断
        elif len(s) == 0 and len(pattern) != 0:
            # pattern中的第二个字符为*，则pattern后移两位继续比较
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        if pattern[1:2] == "*":
            if s[0:1] == pattern[0:1] or pattern[0:1] == ".":
                # 匹配1个或多个时，str当前字符移向下一个，pattern当前字符不变
                # 匹配0个字符时，str当前字符不变，pattern当前字符后移两位
                return self.match(s[1:], pattern) or self.match(s, pattern[2:])
            else:
                return self.match(s, pattern[2:])
        else:
            if s[0:1] == pattern[0:1] or pattern[0:1] == ".":
                return self.match(s[1:], pattern[1:])


print(Solution().match("\"\"", "\".*\""))
