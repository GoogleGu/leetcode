package com.zcsh.code.tribinacci;

import java.util.LinkedList;
import java.util.List;

/**
 * @description: 我的朋友在作弊吗
 * @author: Carey丶zsh
 * @date: 2019-01-08
 */
public class is_my_friend_cheating_zcsh {

    public static List<long[]> removNb(long n) {

        // your code
        List<long[]> result = new LinkedList<>();
        long sum = (1 + n) * n / 2;
        for (long i = n; i >= 1; i--) {
            long quotient = (sum - i) / (i + 1);
            long remainder = (sum - i) % (i + 1);
            if (quotient <= n && remainder == 0) {
                result.add(new long[]{i, quotient});
            }
        }
        return result;
    }

}
