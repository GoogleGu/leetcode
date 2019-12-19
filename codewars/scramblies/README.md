# 乱中有序

**日期**: 2019.1.7

**等级**: 5

**链接：https://www.codewars.com/kata/scramblies**

## 题目

编写一个函数scramble(str1, str2)，如果str1中的部分字母重新排序后与str2一致，则返回真，否则返回假。

注意：

只会用到小写字母，数字和标点符号等不会被包含在str1与str2中。

需要考虑性能。

### 例子

```
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```

## 原文

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.

Performance needs to be considered

Input strings s1 and s2 are null terminated.

### Examples
```
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```