public class Solution {
    public int StrToInt(String str) {
                if (str == null) {
            return 0;
        }

        boolean isF = false;
        if (str.startsWith("+")) {
            str = str.replace("+", "");
        } else if (str.startsWith("-")) {
            str = str.replace("-", "");
            isF = true;
        }

        String regex = "^[0-9]{0,10}";
        if (!str.matches(regex)) {
            return 0;
        }

        char[] chars = str.toCharArray();
        long sum = 0L;
        int temp = chars.length - 1;
        for (int i = 0; i < chars.length; i++, temp--) {
            double sss = Math.pow(10, temp);
            int num = ((int) chars[i] - (int) '0');
            sum = sum + (long)(num * sss);
        }
        if (isF) {
            sum = 0 - sum;
        }

        if (sum > Integer.MAX_VALUE) {
            return 0;
        }
        if(sum < Integer.MIN_VALUE){
            return 0;
        }
        return (int) sum;
    }
}
