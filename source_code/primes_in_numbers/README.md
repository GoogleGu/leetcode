# 数字中的质因数

**日期**: 2018.12.8

**等级**: 5

**链接：https://www.codewars.com/kata/primes-in-numbers**

## 题目
给定一个大于1的正整数n，找出n的所有质因子。结果应是以下形式的字符串：`"(p1**n1)(p2**n2)...(pk**nk)"`
p(i)应该递增，并且在n(i)为1时忽略掉n(i)。
比如说，n=86240应该返回`"(2**5)(5)(7**2)(11)"`


## 原文

> Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

`"(p1**n1)(p2**n2)...(pk**nk)"`

> with the p(i) in increasing order and n(i) empty if n(i) is 1.
Example: n = 86240 should return 

`"(2**5)(5)(7**2)(11)"`