/**
 * 这个题看不懂不会做   觉得这样写挺好   虽然不知道为啥
 */

public class Solution {
    public boolean match(char[] str, char[] pattern)
    {
        return  new String(str).matches(new String(pattern));
    }
}


/**
 * 看过答案之后的
 */

public class Solution {
    public boolean match(char[] str, char[] pattern)
    {
        if (str == null || pattern == null) {
            return false;
        }
        int strIndex = 0;
        int patternIndex = 0;
        return isMatch(str, strIndex, pattern, patternIndex);
    }

    public boolean isMatch(char[] str, int strIndex, char[] pattern, int patternIndex){
        // str 和 pattern 都比完了
        if (strIndex == str.length && patternIndex == pattern.length) {
            return true;
        }
        // str 还没用完    pattern就用完了
        if (strIndex != str.length && patternIndex == pattern.length) {
            return false;
        }
        // str 用完了  pattern还没用完 （有特殊情况  就是后边存在*） a*这样的情况
        if (strIndex == str.length && patternIndex != pattern.length) {
            if (patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*') {
                return isMatch(str, strIndex, pattern, patternIndex + 2);
            }
            return false;
        }
        // 两个都没用完的情况
        if (patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*') {
            // 前边的字母相同 或者  出现.
            if (pattern[patternIndex] == str[strIndex] || (pattern[patternIndex] == '.' && strIndex != str.length)) {
                return isMatch(str, strIndex, pattern, patternIndex + 2) // 就后移俩  就相当于a* 没有
                        || isMatch(str, strIndex + 1, pattern, patternIndex + 2) // 就 a* = a
                        || isMatch(str, strIndex + 1, pattern, patternIndex);//  a* = a   还想看看下一个str中是否还是一个a
            }else {
                // 匹配到* 跳过   这个不太理解
                return isMatch(str, strIndex, pattern, patternIndex + 2);
            }
        }
        // 下一个没出现*
        if ((strIndex != str.length && pattern[patternIndex] == str[strIndex]) || (pattern[patternIndex] == '.' && strIndex != str.length)) {
            return isMatch(str, strIndex + 1, pattern, patternIndex + 1);
        }
        return false;
    }
}