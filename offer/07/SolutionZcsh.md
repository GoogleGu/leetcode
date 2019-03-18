# 剑指 Offer (七)斐波那契数列
## 题目
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
## 问题代码

```java
public class Solution {
    public int Fibonacci(int n) {

    }
}
```
## 解决代码
> 解决问题思路:  current 为当前 n 位置的值,首先检查 n 是否小于2 ,如果是则 n 是 就是自身,如果不是则设置初始值 0 ,1 然后从第2个位置开始相加;
> 运行时间：13ms
占用内存：9568k

```java
public class Solution {
    public int Fibonacci(int n) {
        int current = n < 2 ? n : 1;
        for (int i = 2, after = 0;  i <= n ; i++){
            int temp = current + after;
            after = current;
            current = temp;
        }
        
        return current;
    }
}
```

**带缓存解决方法**
> 解决问题思路:  缓存以前计算过的记录,如果有则直接返回,如果没有则从当前存在的最大的下标值开始计算(不明白为什么网页上老是报数组越界,但是本地跑没事)

```java
public class Solution {
    private static final int[] array = new int[40];
    private static int CURRENT_MAX_INDEX = 1;
    static {
        array[0] = 0;
        array[1] = 1;
    }
    public int Fibonacci(int n) {
        if (array[n] != 0) {
            return array[n];
        }
        for (int i = CURRENT_MAX_INDEX + 1; i <= n ; i++){
            array[i] = array[i - 1] + array[i - 2]; 
        }
        CURRENT_MAX_INDEX = n;
        return array[n];
    }
}
```
## 总结
###1. 本题考查了什么
考查对斐波那契数列的理解,以及缓存对缓存的使用
### 2. 收获了什么
对算法的提炼,代码编写的提炼,虽然这题很简单 ,但是和以前比起来,写出来更加老练了....
