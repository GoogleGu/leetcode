class Solution:

    def isMatch(self, s, pattern):
        # s='ab' and p='' or
        # s='' and p=''
        if len(pattern) == 0:
            return len(s) == 0

        # s='' and p='a*b*c*'
        if len(s) == 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.isMatch(s, pattern[2:])
            return False
        # s='acb' and p='a*.*b*'
        else:
            if len(pattern) > 1:
                # s='acb' and p='ac*'
                if pattern[1] != '*':
                    return (pattern[0] == s[0] or pattern[0] == '.') and self.isMatch(s[1:], pattern[1:])
                # s='acb' and p='a*cb'
                else:
                    if pattern[0] == '.':
                        return self.isMatch(s[1:], pattern) or self.isMatch(s, pattern[2:])
                    elif s[0] == pattern[0]:
                        return self.isMatch(s[1:], pattern) or self.isMatch(s, pattern[2:])
                    else:
                        return self.isMatch(s, pattern[2:])
            else:
                return len(s) == 1 and (pattern[0] == '.' or s[0] == pattern[0])