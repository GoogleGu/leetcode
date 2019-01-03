package com.zcsh.code.tribinacci;

import java.util.*;

/**
 * @description: 整数：创意1
 * @author: Carey丶zsh
 * @date: 2018-12-20
 */
public class integers_recreation_one_Zcsh {

    public static String listSquared(long m, long n) {

        List<List<Long>> resultList = new LinkedList();
        for (long i = m; i <= n; i++) {
            Long execute = execute(i);
            if (execute != null) {
                List<Long> temp = new LinkedList();
                temp.add(i);
                temp.add(execute);
                resultList.add(temp);
            }
        }
        return resultList.toString();
    }

    private static Long execute(long num) {

        Set<Long> hashSet = new HashSet<>();
        for (long i = 1; i < Math.sqrt(num) + 1; i++) {
            if (num % i == 0) {
                long temp2 = num / i;
                hashSet.add(temp2);
                hashSet.add(i);
            }
        }
        Iterator<Long> iterator = hashSet.iterator();
        long sum = 0;
        while (iterator.hasNext()) {
            Long next = iterator.next();
            sum += next * next;
        }
        long sqrt = (long) Math.sqrt(sum);

        return sqrt * sqrt == sum ? sum : null;
    }

}
