package com.zcsh.code.tribinacci;

/**
 * @description: Tribinacci 数列
 * @author: Zcsh
 * @date: 2018-12-05
 */
public class Tribinacci_Zcsh {

    private static final int INIT_SIZE = 3;

    public static void main(String[] args) {

        int size = 5;

        long[] array = new long[size];
        array[0] = 1;
        array[1] = 1;
        array[2] = 3;

        simple(array, size - 1);

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + ",");
        }

    }

    /**
     * 简单便利(建议用这种)
     *
     * @param array 计算的数组
     * @param n     n 的值
     */
    public static void simple(long[] array, int n) {

        for (int i = INIT_SIZE; i <= n; i++) {
            array[i] = array[i - 1] + array[i - 2] + array[i - 3];
        }
    }

    /**
     * 递归计算
     *
     * @param array        需要计算的数组
     * @param currentIndex 计算出当前位置的值(也会把当前坐标前的值带出来)
     * @return
     */
    public static long recursion(long[] array, int currentIndex) {

        if (currentIndex < INIT_SIZE) {
            return array[currentIndex];
        }

        array[currentIndex] = recursion(array, currentIndex - 1)
                + recursion(array, currentIndex - 2)
                + recursion(array, currentIndex - 3);

        return array[currentIndex];
    }

}
