package com.zcsh.code.tribinacci;

/**
 * @description: 字母战争-牧师版
 * @author: Carey丶zsh
 * @date: 2018-12-07
 */
public class Alphabet_war_with_priesta_Zcsh {

    /**
     * 0~4是右战队.5~9是左战队
     */
    private static final String REGIH_AND_LEFT = "tsbpwjzdqm";

    /**
     * 阵容人员数量
     */
    private static final int LINEUP_NUMBER = 5;

    public static String woLoLoooooo(String battlefield) {
        // Your code here!
        char[] chars = battlefield.toCharArray();

        int result = 0;

        for (int i = 0; i < chars.length; i++) {

            int previousIndex = i > 0 ? REGIH_AND_LEFT.indexOf(chars[i - 1]) : -1;
            int currentIndex = REGIH_AND_LEFT.indexOf(chars[i]);
            int nextIndex = i != chars.length - 1 ? REGIH_AND_LEFT.indexOf(chars[i + 1]) : -1;

            // 当前值不在阵容里或当前值是牧师
            if (currentIndex == -1 || currentIndex % LINEUP_NUMBER == 0) {
                continue;
            }
            boolean isSwap = isSwap(previousIndex, currentIndex, nextIndex);
            // 将坐标转换成战斗力
            currentIndex = currentIndex > LINEUP_NUMBER ? currentIndex - LINEUP_NUMBER : currentIndex * -1;
            // 是否转换
            if (isSwap) {
                currentIndex = currentIndex * -1;
            }
            result += currentIndex;

        }


        return result == 0 ? "Let's fight again!" : result > 0 ? "Right side wins!" : "Left side wins!";
    }

    /**
     * 判断是否交换
     *
     * @param previousIndex
     * @param currentIndex
     * @param nextIndex
     * @return
     */
    public static boolean isSwap(int previousIndex, int currentIndex, int nextIndex) {

        int previousIndexSurplus = previousIndex % LINEUP_NUMBER;
        int nextIndexSurplus = nextIndex % LINEUP_NUMBER;

        // 都是牧师,并且同一种族
        if (previousIndexSurplus == 0 && previousIndex == nextIndex) {
            // 判断当前值是否和牧师不在一个族里,不同一个组 true,同一个组 false
            return isIdenticalLineup(nextIndex, currentIndex);
        }

        // 都是牧师且不同种族
        if (nextIndexSurplus == previousIndexSurplus && nextIndexSurplus != -1) {
            return false;
        }

        return previousIndexSurplus == 0 ?
                isIdenticalLineup(previousIndex, currentIndex) :
                nextIndexSurplus == 0 ? isIdenticalLineup(nextIndex, currentIndex) : false;
    }

    /**
     * 判断是否属于同一阵容
     *
     * @param nearbyIndex
     * @param currentIndex
     * @return
     */
    public static boolean isIdenticalLineup(int nearbyIndex, int currentIndex) {

        return (nearbyIndex < LINEUP_NUMBER) != (currentIndex < LINEUP_NUMBER);
    }

}
