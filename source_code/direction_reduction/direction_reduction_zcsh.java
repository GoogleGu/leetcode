package com.zcsh.code.tribinacci;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @description:缩减方向
 * @author: Carey丶zsh
 * @date: 2018-12-27
 */
public class direction_reduction_zcsh {

    private static List<Integer> arrList = null;


    public static String[] dirReduc(String[] arr) {

        arrList = new ArrayList(arr.length);
        for (int i = 0; i < arr.length; i++) {
            arrList.add(ConstantArr.valueOf(arr[i]).ordinal() - 2);
        }
        execute(0, 1);

        List<String> resultList = arrList.stream()
                .filter(item -> item != 0)
                .map(item -> ConstantArr.values()[item + 2].name()).collect(Collectors.toList());

        String[] resultArr = new String[resultList.size()];
        resultList.toArray(resultArr);
        return resultArr;
    }

    private static void execute(int startIndex, int endIndex) {

        // 到最后两个的时候,返回抵消了0个
        if (endIndex == arrList.size()) {
            return;
        }
        execute(endIndex, endIndex + 1);

        if (arrList.get(startIndex) + arrList.get(endIndex) == 0) {
            if (endIndex == arrList.size() - 1) {
                arrList.set(startIndex, 0);
                arrList.set(endIndex, 0);
            } else if (endIndex == arrList.size() - 2) {

                arrList.set(startIndex, arrList.get(startIndex + 2));
                arrList.set(startIndex + 2, 0);
                arrList.set(endIndex, 0);
            } else {
                arrList.set(startIndex, arrList.get(startIndex + 2));
                arrList.set(endIndex, arrList.get(endIndex + 2));
                arrList.set(startIndex + 2, 0);
                arrList.set(endIndex + 2, 0);
            }
        }

    }


    enum ConstantArr {
        NORTH, WEST, DEFAULT, EAST, SOUTH
    }

}
