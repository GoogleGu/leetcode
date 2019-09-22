public class SolutionZcsh {
    public int StrToInt(String str) {

        if (str == null || str.length() == 0) {
            return 0;
        }
        int maxBigNumber = Integer.MAX_VALUE / 10;
        char[] strArray = str.toCharArray();
        int result = 0, index = 0, resultHandle = 1;
        if (strArray[0] == '-' || strArray[0] == '+') {
            resultHandle = strArray[0] == '-' ? -1 : 1;
            index++;
        }

        for (; index < strArray.length; index++) {
            if (strArray[index] > '9' || strArray[index] < '0') return 0;
            // 0 - 9 的 ascii 的低四位二进制位,刚好就是 0-9 对应的数字
            int value = strArray[index] & 0xf;
            if (maxBigNumber < result) return 0;
            result = (result << 1) + (result << 3);
            if (resultHandle == 1 && Integer.MAX_VALUE - result - value < 0) { // 判断正式最大值
                return 0;
            } else if (Integer.MAX_VALUE - result - value < -1) { // 判断负数最大值
                return 0;
            }
            result += value;
        }

        return result * resultHandle;
    }
}
