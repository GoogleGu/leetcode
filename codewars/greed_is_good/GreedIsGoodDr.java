package greed_is_good;

import java.util.Arrays;

/**
 * @author Dream
 * @date 2018/12/6 13:51
 */
public class GreedIsGoodDr {

    private static int[][] points = {{111, 1000}, {666, 600}, {555, 500}, {444, 400}, {333, 300}, {222, 200}, {1, 100}, {5, 50}};

    public static int greedy(int[] dice) {
        Arrays.sort(dice);
        StringBuffer sb = new StringBuffer();
        for (int die : dice) {
            sb.append(die);
        }
        String param = sb.toString();
        
        Integer score = 0;
        for (int[] point : points) {
            while (param.indexOf(point[0] + "") != -1) {
                score += point[1];
                param = param.replaceFirst(point[0] + "", "");
            }
        }
        return score;
    }



}
