package main;


/**
 * @description:
 * @author: Meteor
 * @date: 2018/12/10
 */
public class PrimeFactor {

    public static String factors(int number) {
        StringBuilder result = new StringBuilder();
        for (int i = 2; i <= number; i++) {
            Integer count = 0;
            if (number % i == 0 && !primeNumber(i)) {
                while (number % i == 0) {
                    number = number / i;
                    count++;
                }
                result.append("(" + i + (count == 1 ? "" : "**" + count) + ")");
            }
        }
        return result.toString();
    }

    public static Boolean primeNumber(Integer number) {
        Boolean flag = false;
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                flag = true;
            }
        }
        return flag;
    }
}
