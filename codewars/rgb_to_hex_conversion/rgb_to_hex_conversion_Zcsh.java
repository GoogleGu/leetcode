package com.zcsh.code.tribinacci;

/**
 * @description: RGB转换为十六进制
 * @author: Carey丶zsh
 * @date: 2018-12-20
 */
public class rgb_to_hex_conversion_Zcsh {

    private static final char[] RGB_ARRAY = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    public static String rgb(int r, int g, int b) {
        return execute(r, g, b);
    }


    public static String execute(int... rgbs) {

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < rgbs.length; i++) {
            int rgb = rgbs[i];
            rgb = rgb > 255 ? 255 : rgb < 0 ? 0 : rgb;
            sb.append(RGB_ARRAY[rgb / 16]).append(RGB_ARRAY[rgb % 16]);
        }
        return sb.toString();
    }

}
