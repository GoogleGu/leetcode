# 约翰与安加入了Codewars

**链接：https://www.codewars.com/kata/john-and-ann-sign-up-for-codewars**

## 题目

约翰和他的妻子安决定加入Codewars。

第一天安会完成一个题目，而约翰决定先搞清楚Codewars是怎么回事，所以他没有完成题目。

我们用a(n)和j(n)来表示安和约翰在第n天完成的题目数。a(0)=1，j(0)=0

他们选择了以下的规则：

安在第n天完成的题目应该等于n减去约翰在第t天完成的题目，t等于安在第n-1天完成的题目数。

约翰在第n天完成的题目应该等于n减去安在第t天完成的题目，t等于约翰在第n-1天完成的题目数。

我勒个去，我觉得他们应该把他们自己想干什么弄得更清楚点。

请你写出以下代码：
1）两个函数ann(n)和john(n)，接受入参都为第n天，分别返回安和约翰在前n天每天应该完成的题目的数组。
2）能够算出安第n天解题总数的函数sum_ann(n)，和算约翰解题总数的函数sum_john(n)。

**例子:**
```
john(11) -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6) -->  [1, 1, 2, 2, 3, 3]

sum_john(75) -->  1720
sum_ann(150) -->  6930
```

**注意:**
留神代码的执行效率.


## 原文

John and his wife Ann have decided to go to Codewars.

On first day Ann will do one kata and John - he wants to know how it is working - 0 kata.

Let us call a(n) the number of katas done by Ann at day n. We have a(0) = 1 and in the same manner j(0) = 0 (or a(1) = 1 and j(1) = 0 for languages that have arrays with indices beginning at 1).

They have chosen the following rules:

On day n the number of katas done by Ann should be n minus the number of katas done by John at day t, t being equal to the number of katas done by Ann herself at day n - 1.

On day n the number of katas done by John should be n minus the number of katas done by Ann at day t, t being equal to the number of katas done by John himself at day n - 1.

Whoops! I think they need to lay out a little clearer exactly what there're getting themselves into!

Could you write:
1) two functions ann and john (parameter n) giving the list of the numbers of katas Ann and John should take on the first n days (see first examples below)?
2) The total number of katas taken by ann function sum_ann(n) and john function sum_john(n) - on the first n days?
The functions in 1) are not tested in Fortran and not tested in Shell.

**Examples:**
```
john(11) -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6) -->  [1, 1, 2, 2, 3, 3]

sum_john(75) -->  1720
sum_ann(150) -->  6930
```

Shell Note:
sumJohnAndAnn has two parameters:
```
first one : n (number of days, $1)

second one : which($2) ->

1 for getting John's sum

2 for getting Ann's sum.
```
See "Sample Tests".


Note:
Keep an eye on performance.
