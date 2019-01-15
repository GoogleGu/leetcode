package com.zcsh.code.tribinacci;

/**
 * @description:乱中有序
 * @author: Carey丶zsh
 * @date: 2019-01-15
 */
public class scramblies_zcsh {


    public static boolean scramble(String str1, String str2) {

        int[] counter = new int[26];

        char[] chars = str1.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            counter[chars[i] - 97]++;
        }
        char[] chars1 = str2.toCharArray();
        for (int i = 0; i < chars1.length; i++) {
            counter[chars1[i] - 97]--;
        }

        for (int i = 0; i < chars1.length; i++) {
            if (chars1[i] > 0) {
                return false;
            }
        }

        return true;
    }



}
