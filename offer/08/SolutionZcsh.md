# 剑指 Offer (八) 跳台阶
## 题目
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
## 问题代码

```java
public class Solution {
    
    public int JumpFloor(int target) {
        
    }
}
```
## 解决代码
> 解决问题思路:  规律和斐波那契一样,解题思路也一样
> 运行时间：19ms
占用内存：9344k

```java
import java.util.ArrayList;
import java.util.List;
public class Solution {
    
    private static final List<Integer> list = new ArrayList<>();

    private static int CURRENT_MAX_INDEX = 1;

    static {
        list.add(1);
        list.add(2);
    }

    public int JumpFloor(int target) {

        if (list.size() >= target) {
            return list.get(target - 1);
        }

        for (int i = CURRENT_MAX_INDEX + 1; i <= target; i++) {
            list.add(list.get(i - 1) + list.get(i - 2));
        }
        CURRENT_MAX_INDEX = target;
        return list.get(target - 1);

    }
}
```
## 总结
###1. 本题考查了什么
考查内容与上题类似,并且本题没有固定 n 的最大值,所以不能使用简单的数组;
### 2. 收获了什么
与上题类似;
