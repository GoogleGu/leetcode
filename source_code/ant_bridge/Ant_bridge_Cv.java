package ant_bridge;


/**
 * @description: 蚂蚁桥
 * @author: C.v.
 * @date: 2018-12-11
 */
public class Ant_bridge_Cv {

// GFEDCBA

// --------..--...----------- 4+5
// GFE ABCD
// ABCD EFG AB
// BA GFEDC

// --------..--.-- 4+3
// GFE ABCD
// ABCD EFG

// ------.----  3
//  GFED ABC
//  CBA DEFG

//   --.--  3
//   --..-- 4
//   -.-.-  5

    public static String antBridge(final String ants, final String terrain) {
        if (terrain.length() < 3)
            return ants;
        //计算沟数(加上沟前后的桥)
        int sum = terrain.charAt(1) == '.' ? 1 : 0;
        for (int i=1; i<terrain.length()-1; i++)
            if ('.' == terrain.charAt(i)
                    || '.' == terrain.charAt(i+1)
                    || '.' == terrain.charAt(i-1))
                sum++;
        if (terrain.charAt(terrain.length() - 2) == '.')
            sum++;
        if (sum == 0)
            return ants;

        return turnCutting(ants, sum);
    }

    /**
     * 翻转与切割
     */
    private static String turnCutting(final String ants, int sum) {
        boolean turn = sum / ants.length() % 2 == 1;
        String a = turn ? new StringBuffer(ants).reverse().toString() : ants;

        int cutting = sum % ants.length();
        if (cutting == 0)
            return turn ? ants : a;

        if (turn)
            return new StringBuffer(a.substring(0,cutting)).reverse().append(new StringBuffer(a.substring(cutting)).reverse()).toString();

        int surplus = a.length() - cutting;
        return a.substring(surplus) + a.substring(0,surplus);
    }



    public static void main (String[] args) {
        System.out.println(antBridge("GFEDCBA", "------.-------")); // CBA GFED
        System.out.println(antBridge("GFEDCBA", "------...-------"));//EDCBA GF  5

        //ABCDEFG
        // BA GFEDC
        System.out.println(antBridge("GFEDCBA", "--------..--...------"));// 9

        System.out.println(antBridge("GFEDCBA", "-..-.-...------..-----.-"));//17
        System.out.println(antBridge("LKJIHGFEDCBA", "-----..........-"));//LKJIHGFEDCBA

        System.out.println(antBridge("IHGFEDCBA", "-.------..------...-..----.-----"));//IHGFEDCBA

        System.out.println(antBridge("CBA", "--.---------"));//CBA

    }



}
