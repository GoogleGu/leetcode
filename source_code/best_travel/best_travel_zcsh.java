package com.zcsh.code.tribinacci;

import java.util.Arrays;
import java.util.List;

/**
 * @description: 最佳旅途
 * @author: Carey丶zsh
 * @date: 2018-12-15
 */
public class best_travel_zcsh {

    /**
     * @param t  需要走多少路程
     * @param k  需要去几个城市
     * @param ls 城市距离
     * @return
     */
    public static Integer chooseBestSum(int t, int k, List<Integer> ls) {
        Integer execute = execute(t, k, ls, ls.size() - 1);
        return execute == -1 ? null : execute;
    }

    /**
     * @param t     剩余路径
     * @param k     要去几个城市
     * @param ls    城市列表
     * @param index 去往的城市
     * @return
     */
    public static Integer execute(int t, int k, List<Integer> ls, int index) {

        // 没有路程走了,所以本次消耗为 0
        if (k == 0 && t >=0) {
            return 0;
        }

        // 需要走的城市没走完,就不能走的话 返回 -1
        if (t  < 0 || index < 0) {
            return -1;
        }

        // 这个城市去
        Integer case1 = execute(t - ls.get(index), k - 1, ls, index - 1);

        // 这个城市不去
        Integer case2 = execute(t, k, ls, index - 1);

        // 如果剩余的城市去不了,则这条路径错误 , case 即为 -1
        case1 = case1 != -1 ? case1 + ls.get(index) : -1;

        // 比较两个谁消耗的多
        return Math.max(case1, case2);

    }



}
