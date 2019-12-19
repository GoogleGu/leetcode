package alphabet_war_with_priest;


import java.util.HashMap;
import java.util.Map;

/**
 * @author Dream
 * @date 2018/12/7 10:11
 */
public class AlphabetWarWithPriestDr {
    public static Map<Character, Float> pow = new HashMap<>();
    public static String leftWin = "Left side wins!";
    public static String rightWin = "Right side wins!";
    public static String allWin = "Let's fight again!";
    public static String format = "aa%saa";

    static {
        pow.put('w', -4F);
        pow.put('p', -3F);
        pow.put('b', -2F);
        pow.put('s', -1F);
        pow.put('t', -0.1F);
        pow.put('m', 4F);
        pow.put('q', 3F);
        pow.put('d', 2F);
        pow.put('z', 1F);
        pow.put('j', 0.1F);
        pow.put('a', 0F);
        pow.put('c', 0F);
        pow.put('e', 0F);
        pow.put('f', 0F);
        pow.put('g', 0F);
        pow.put('h', 0F);
        pow.put('i', 0F);
        pow.put('k', 0F);
        pow.put('l', 0F);
        pow.put('n', 0F);
        pow.put('o', 0F);
        pow.put('r', 0F);
        pow.put('u', 0F);
        pow.put('v', 0F);
        pow.put('x', 0F);
        pow.put('y', 0F);
    }

    public static String woLoLoooooo(String str) {
        char[] chars = String.format(format, str).toCharArray();
        int sum = 0;
        for (int i = 2; i < chars.length - 2; i++) {
            if (chars[i] == 't' || chars[i] == 'j') {
                boolean left = pow.get(chars[i]) * pow.get(chars[i - 1]) < 0;
                boolean leftPriest = !((chars[i] == 't' ? 'j' : 't') == chars[i - 2]);
                boolean right = pow.get(chars[i]) * pow.get(chars[i + 1]) < 0;
                boolean rightPriest = !((chars[i] == 't' ? 'j' : 't') == chars[i + 2]);
                if (left && leftPriest) {
                    if (chars[i] == chars[i - 2]) {
                        sum += (int) (0 - pow.get(chars[i - 1]));
                        chars[i - 1] = 'a';
                    } else {
                        sum += (int) (0 - pow.get(chars[i - 1])) * 2;
                    }
                }
                if (right && rightPriest) {
                    if (chars[i] == chars[i + 2]) {
                        sum += (int) (0 - pow.get(chars[i + 1]));
                        chars[i + 1] = 'a';
                    } else {
                        sum += (int) (0 - pow.get(chars[i + 1])) * 2;
                    }
                }
            } else {
                sum += pow.get(chars[i]);
            }
        }
        return sum < 0 ? leftWin : sum > 0 ? rightWin : allWin;
    }

}
