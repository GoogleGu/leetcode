public class Solution {
   
    public boolean match(char[] str, char[] pattern)
    {
        return match(str,0,pattern,0);
    }
    
    public boolean match(char[] str, int strIndex, char[] pattern, int patternIndex) {
        if (patternIndex == pattern.length) {
            return strIndex == str.length;

        }
        boolean flag = false;

        if (strIndex < str.length && (str[strIndex] == pattern[patternIndex] || pattern[patternIndex] == '.')) {
            flag = true;
        }

        if (patternIndex < pattern.length - 1 && pattern[patternIndex + 1] == '*') {
            return match(str, strIndex, pattern, patternIndex + 2)
                    || (flag && match(str, strIndex + 1, pattern, patternIndex));
        } else {
            return (flag && match(str, strIndex + 1, pattern, patternIndex + 1));

        }

    }

}
