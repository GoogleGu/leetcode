package com.zcsh.code.tribinacci;

/**
 * @description: 数字中的质因数
 * @author: Carey丶zsh
 * @date: 2018-12-08
 */
public class Primes_in_numbers_Zcsh {

    private static Integer CURRENT_VALUE = 0;

    private static Integer CURRENT_NUMBER = 0;

    public static String factors(int n) {

        StringBuffer sb = new StringBuffer();
        execute(n, sb);
        // 将最后一个质因子存入字符串,并初始化 CURRENT_VALUE
        append(0, sb);

        return sb.toString();
    }

    /**
     * 递归方法,找到第一个能整除的数就结束循环
     *
     * @param n
     */
    public static void execute(int n, StringBuffer sb) {

        for (int i = 2; i < ((int) Math.sqrt(n) + 1); i++) {
            if (n % i == 0) {
                append(i, sb);
                execute(n / i, sb);
                return;
            }
        }
        append(n, sb);
    }

    /**
     * 如果存在则加1,不存在则添加为1
     *
     * @param integer
     */
    public static void append(Integer integer, StringBuffer sb) {

        if (CURRENT_VALUE.equals(integer)) {
            CURRENT_NUMBER++;
            return;
        }
        if (CURRENT_VALUE != 0) {
            sb.append("(").append(CURRENT_VALUE);
            if (CURRENT_NUMBER != 1) {
                sb.append("**").append(CURRENT_NUMBER);
            }
            sb.append(")");
        }

        // 当输入的数和上一个数不同,则对变量重新赋值
        CURRENT_VALUE = integer;
        CURRENT_NUMBER = 1;

    }

}
