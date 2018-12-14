# 整数：创意1

**链接：https://www.codewars.com/kata/integers-recreation-one**

## 题目

42的因数为：1, 2, 3, 6, 7, 14, 21, 42。这些因数的平方为：1, 4, 9, 36, 49, 196, 441, 1764。这些因数额平方和为2500，也就是50的平方，也是一个平方数！

给定两个整数m，n(1 <= m <= n)。我们想要找出所有在m和n之间因数和为平方数的数。42就是一个这样的数字。

返回的结果应该是数组，其元素为数组或元组或字符串，每个子数组都应有两个元素，第一个是因数平方和为平方数的数（比如42），另一个是这些因数的平方和（比如2500）。

**例子**

```
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
```

例子的形式可能因语言而不同，详情请查看示例测试中的测试。

**注意**
在Fortran中——正如任何其他语言一样——返回的字符串中不允许包含任何多余的空白字符：你可以使用动态分配的字符串。


## 原文

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

**Examples:**

```
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
```

The form of the examples may change according to the language, see Example Tests: for more details.

**Note**

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.