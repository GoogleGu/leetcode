package com.zcsh.code.tribinacci;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

/**
 * @description: 约翰和安
 * @author: Carey丶zsh
 * @date: 2018-12-25
 */
public class john_and_ann_sign_up_for_codewars_zcsh {

    public static List<Long> john(long n) {


        return execute(n,false);
    }

    public static List<Long> ann(long n) {

        return execute(n,true);
    }

    public static long sumJohn(long n) {
        // your code
        long sum = 0;
        for (Long item : john(n)) {
            sum += item;
        }
        return sum;
    }

    public static long sumAnn(long n) {

        long sum = 0;
        for (Long item : ann(n)) {
            sum += item;
        }
        return sum;
    }

    private static List<Long> execute(long n, boolean isAnn) {
        int intN = (int) n;
        long[] johnArray = new long[intN];
        long[] annArray = new long[intN];
        johnArray[0] = 0;
        annArray[0] = 1;
        for (int index = 1; index < intN; index++) {
            johnArray[index] = index - annArray[(int) johnArray[index - 1]];
            annArray[index] = index - johnArray[(int) annArray[index - 1]];
        }
        List<Long> resultList = new ArrayList<>(intN);
        long[] resultArray = isAnn ? annArray : johnArray;
        IntStream.range(0, intN).forEach(index -> resultList.add(resultArray[index]));
        return resultList;
    }
}
