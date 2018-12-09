package primes_in_numbers;


import java.util.LinkedHashMap;
import java.util.Map;

/**
 * @description: 数字中的质因数
 * @author: C.v.
 * @date: 2018-12-09
 */
public class Primes_in_numbers_Cv {

    /**
     * 记录质因数出现的次数，对应key(质因数)-value(次数)
     */
    static Map<Integer, Integer> primes = new LinkedHashMap<>();

    /**
     * 添加质因数
     * @param i 质因数
     */
    static void addPrimes(int i) {
        primes.put(i, primes.get(i) == null ? 1 : primes.get(i)+1);
    }

    /**
     * Pollard Rho因数分解
     * @param n 待分解的数
     */
    static void rho(int n) {
        if (n < 2) return;
        for (int i=2; i<=n; i++) {
            while (n != i) {
                if (n%i != 0) break;//不能整除肯定不是因数
                addPrimes(i);
                n = n/i;
            }
        }
        addPrimes(n);
    }

    /**
     * 输出格式处理
     */
    static String format() {
        StringBuffer sbuffer = new StringBuffer();
        primes.forEach((k,v) ->
                sbuffer.append(v == 1 ? "(" + k+ ")" : "(" + k + "**" + v + ")"));
        return sbuffer.toString();
    }

    public static void main (String[] args) {
        int n = 6105420;
        rho(n);
        System.out.println(format());
    }

}
