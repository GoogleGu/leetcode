import java.util.*;
public class Solution {
    public int StrToInt(String str) {
        if (str == null || str.trim().equals("")) {
            return 0;
        }
        List<Character> list = Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-');
        Boolean plus = true; // 正是 true 负是 false
        if (String.valueOf(str.charAt(0)).equals("-")) {
            str.replace("-", "");
            plus = false;
        } else if (String.valueOf(str.charAt(0)).equals("+")) {
            str.replace("+", "");
            plus = true;
        }
        int strLen = str.length();
        double sum = 0;
        for (int i = 0; i < str.length(); i++) {
            double n = Math.pow(10, strLen - 1);
            if (list.contains(str.charAt(i))) {
                switch (String.valueOf(str.charAt(i))) {
                    case "9":
                        sum = (sum + 9 * n);
                        break;
                    case "8":
                        sum = (sum + 8 * n);
                        break;
                    case "7":
                        sum = (sum + 7 * n);
                        break;
                    case "6":
                        sum = (sum + 6 * n);
                        break;
                    case "5":
                        sum = (sum + 5 * n);
                        break;
                    case "4":
                        sum = (sum + 4 * n);
                        break;
                    case "3":
                        sum = (sum + 3 * n);
                        break;
                    case "2":
                        sum = (sum + 2 * n);
                        break;
                    case "1":
                        sum = (sum + 1 * n);
                        break;
                    case "0":
                        sum = (sum*n);
                        break;
                }
                strLen--;
            } else {
                return 0;
            }
        }
        if(plus){
            return (int) sum;
        }else{
            return (int)-sum;
        }

    }
}