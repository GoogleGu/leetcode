package integers_recreation_one;

import java.util.LinkedList;
import java.util.List;


/**
 * @description: 整数
 * @author: Meteor
 * @date: 2018/12/17
 */
public class integers_recreation_one_meteor {
    public static void main(String[] args) {
        System.out.println(listSquared(1,42));
    }
    public static String listSquared(long m, long n) {
        // your code
        List<List> resultList = new LinkedList<>();
        for (long i = m; i <= n; i++) {
            List<Long> one = new LinkedList<>();
            long square = 0;
            for (long j = 1; j <= i; j++) {
                if (i % j == 0) {
                    square += Math.pow(j,2);
                }
            }
            int answer = (int) Math.sqrt(square);
            if (answer == Math.sqrt(square)) {
                one.add(i);
                one.add(square);
                resultList.add(one);
            }
        }
        return resultList.toString();
    }
}
