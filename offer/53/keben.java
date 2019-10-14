public class Solution {
     public static boolean isNumeric(char[] str) {
        boolean hasFu = false, hasDian = false, hasE = false;

        for (int i = 0; i < str.length; i++) {
            if (str[i] == 'e' || str[i] == 'E') {
                // 检测符号e E
                if (i == str.length - 1) {
                    return false;
                }
                if (hasE) {
                    return false;
                }
                hasE = true;
            } else if (str[i] == '+' || str[i] == '-') {
                // 检测 +,-符号
                if (hasFu && str[i-1] != 'e' && str[i-1] != 'E') {
                    return false;
                }
                if (!hasFu && i > 0 && str[i-1] != 'e' && str[i-1] != 'E') {
                    return false;
                }
                hasFu = true;

            } else if (str[i] == '.') {
                // 检测小数点
                if (hasE || hasDian) {
                    return false;
                }
                hasDian = true;
            } else if (str[i] < '0' || str[i] > '9') {
                // 检测合法数字
                return false;
            }
        }
        return true;
    }
}
