# 剑指 Offer (九) 变态跳台阶
## 题目
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
## 问题代码

```java
public class Solution {
    public int JumpFloorII(int target) {
        
    }
}
```
## 解决代码
> 解决问题思路:  
> 运行时间：运行时间：14ms
占用内存：9400k

```java
public class Solution {

    public int JumpFloorII(int target) {
        
      return target <= 1 ? target : 1 << target - 1;
    }
}
```
## 总结
###1. 本题考查了什么
考查了数学功底,用数学的方式找出规律,解答起来更方便
### 2. 收获了什么
在算法中忘记了使用数学的能力,只是单纯的看,找规律,如果用数学的方法那么这道题讲相当简单, **还是不能小看数学的能力**
