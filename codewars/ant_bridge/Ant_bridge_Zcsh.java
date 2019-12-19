package com.zcsh.code.tribinacci;

/**
 * @description: 蚂蚁桥
 * @author: Carey丶zsh
 * @date: 2018-12-10
 */
public class Ant_bridge_Zcsh {

    public static String antBridge(final String ants, final String terrain) {
        // Your code here!
        int point = 0;
        char pre = ' ';
        char[] chars = terrain.toCharArray();
        char[] antsArray = new char[ants.length()];

        for (int i = 0; i < chars.length; i++) {
            char currentChar = chars[i];
            point += currentChar != '-' ? 1 : pre == '.' ? 2 : 0;
            point -= i < chars.length - 1 && pre == '.' && currentChar == '-' && chars[i + 1] == '.' ? 1 : 0;
            pre = currentChar;
        }

        for (int i = 0; i < ants.length(); i++) {
            antsArray[(i + point) % ants.length()] = ants.charAt(i);
        }

        return new String(antsArray);
    }

}
