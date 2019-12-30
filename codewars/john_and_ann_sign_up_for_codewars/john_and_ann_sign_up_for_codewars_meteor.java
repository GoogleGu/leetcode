package john_and_ann_sign_up_for_codewars;

import java.util.LinkedList;
import java.util.List;

/**
 * @description:
 * @author: Meteor
 * @date: 2018/12/17
 */
public class john_and_ann_sign_up_for_codewars_meteor {
    public static void main(String[] args) {
        System.out.println(john(4).toString());
    }
    public static List<Long> john(long n) {
        // your code
        List<Long> johnList = new LinkedList<>();
        johnList.add(Long.valueOf(0));
        for (int i = 1; i < n; i++) {
            Long result = n - ann(Math.toIntExact(john(i).get(i - 1)) + 1).get(Math.toIntExact(john(i).get(i - 1)));
            johnList.add(result);
        }

        return johnList;
    }
    public static List<Long> ann(long n) {
        // your code
        List<Long> annList = new LinkedList<>();
        annList.add(Long.valueOf(1));
        for (int i = 1; i < n; i++) {
            Long result = n - john(Math.toIntExact(ann(i).get(i - 1)) + 1).get(Math.toIntExact(ann(i).get(i - 1)));
            annList.add(result);
        }
        return annList;
    }
    public static long sumJohn(long n) {
        // your code
        return n;
    }
    public static long sumAnn(long n) {
        // your code
        return  n;
    }
}
