package com.zcsh.code.tribinacci;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * @description: 偷窥到的密码
 * @author: Carey丶zsh
 * @date: 2019-01-01
 */
public class the_observed_pin_zcsh {

    /**
     * 0:原坐标 1:上 2:下 3:左 4:右
     */
    private static String[][] array = {{"0","8",null,null,null},
                                    {"1",null,"4",null,"2"},
                                    {"2",null,"5","1","3"},
                                    {"3",null,"6","2",null},
                                    {"4","1","7",null,"5"},
                                    {"5","2","8","4","6"},
                                    {"6","3","9","5",null},
                                    {"7","4",null,null,"8"},
                                    {"8","5","0","7","9"},
                                    {"9","6",null,"8",null}};

    public static List<String> getPINs(String observed) {

        char[] chars = observed.toCharArray();
        List<String> result = new LinkedList<>();
        for (int i = 0; i < chars.length; i++) {
            List<String> temp = new ArrayList<>(result.size() * 5);
            for (int j = 0; j < 5; j++) {
                String value = array[chars[i] - 48][j];
                if (value != null) {
                    if (i != 0) {
                        result.stream().forEach(item -> temp.add(item + value));
                    } else {
                        temp.add(value);
                    }
                }
            }
            result = temp;
        }

        return result;
    }

}
