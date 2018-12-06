package com.zcsh.code.tribinacci;

/**
 * @description: 贪婪游戏
 * @author: Carey丶zsh
 * @date: 2018-12-06
 */
public class Greed_is_good_Zcsh {

    /**
     * 为了对应 点数1 就是坐标1,则增加坐标0为补位,可以省去  (dice[i] - 1) 的计算
     */
    private static final int[][] points = {{0, 0}, {100, 1000}, {0, 200}, {0, 300}, {0, 400}, {50, 500}, {0, 600}};

    public int greedy(int[] dice) {

        int sum = 0;
        int[] existenceArray = new int[7];
        for (int i = 0; i < dice.length; i++) {
            int die = dice[i];

            if (existenceArray[die] == 2) {
                sum += points[die][1] - points[die][0] * 2;
                existenceArray[die] = 0;
            } else {
                sum += points[die][0];
                existenceArray[die] += 1;
            }

        }
        return sum;
    }

}
