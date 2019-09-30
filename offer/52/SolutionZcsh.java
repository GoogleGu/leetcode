public class SolutionZcsh {

    public boolean match(char[] str, char[] pattern) {

        return doMatch(str, 0, pattern, 0);
    }

    private boolean doMatch(char[] str, int strIndex, char[] pattern, int patternIndex) {
        if (str.length == strIndex && patternIndex == pattern.length) return true;
        if (str.length != strIndex && patternIndex == pattern.length) return false;

        // 多个字符之间的匹配
        if (patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*') {
            // * 前面的字符,等于 0 个 是否通过
            boolean matchOne = doMatch(str, strIndex, pattern, patternIndex + 2);

            // 0 个匹配不成功, 匹配多个, 是否通过,递归 + 1
            if (!matchOne && strIndex != str.length
                    && (str[strIndex] == pattern[patternIndex] || pattern[patternIndex] == '.')) {
                // * 前面的字符,至少匹配 1 个(因为递归原因,所以可匹配多个)
                return doMatch(str, strIndex + 1 , pattern , patternIndex);
            }
            return matchOne;
        }

        // 当前单个字符是否通过
        return strIndex != str.length && (pattern[patternIndex] == '.' || str[strIndex] == pattern[patternIndex])
                ? doMatch(str, strIndex + 1, pattern, patternIndex + 1) : false;
    }

}
