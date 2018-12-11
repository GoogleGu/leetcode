package com.zcsh.code.tribinacci;

/**
 * @description: 数字重量
 * @author: Carey丶zsh
 * @date: 2018-12-10
 */
public class weight_for_weight_Zcsh {

    private static int index = 0;

    public static String orderWeight(String str) {


        // your code
        // 0存合 1:存最大的数字 2:存原来的数字
        Weight[] weights = new Weight[str.length()];
        if (weights.length == 0) {
            return "";
        }
        weights[0] = new Weight();

        char[] chars = str.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            char val = chars[i];
            boolean isLast = i == chars.length - 1;
            if (val == ' ' || isLast) {
                // array[0][0] 保证开头不是空格
                if (weights[0] != null && (chars[i - 1] != ' ' || weights[index].sum == 0)) {
                    next(weights, val, isLast);
                }
            } else {
                operationArray(weights, val);
            }
        }

        index = 0;
        return result(weights);
    }

    private static void operationArray(Weight[] weights, char val) {

        Weight weight = weights[index];
        int currentVal = val - 48;
        weight.sum += currentVal;
        weight.str += currentVal;
    }


    private static void next(Weight[] weights, char val, boolean isLast) {

        if (isLast) {
            operationArray(weights, val);
            return;
        }
        weights[++index] = new Weight();
    }

    private static String result(Weight[] weights) {


        for (int i = 0; i < weights.length - 1; i++) {
            if (weights[i + 1] == null) {
                break;
            }
            for (int j = i + 1; j < weights.length; j++) {
                if (weights[j] == null) {
                    break;
                }
                boolean flag = weights[i].sum > weights[j].sum ||
                        (weights[i].sum == weights[j].sum && sort(weights[i].str,weights[j].str));
                if (flag) {
                    Weight weight = weights[i];
                    weights[i] = weights[j];
                    weights[j] = weight;
                }

            }

        }
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < weights.length; i++) {
            if (weights[i] != null) {
                result.append(weights[i].str).append(" ");
            }
        }

        return result.toString().substring(0, result.toString().length() - 1);
    }

    private static boolean sort(String str1, String str2) {

        int length = str1.length() > str2.length() ? str2.length() : str1.length();
        char[] chars1 = str1.toCharArray();
        char[] chars2 = str2.toCharArray();

        for (int i = 0; i < length; i++) {
            if (chars1[i] != chars2[i]) {
                return chars1[i] > chars2[i];
            }
        }

        return false;
    }

    static class Weight {

        public int sum = 0;


        public String str = "";

    }


}
