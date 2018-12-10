# 

**链接：https://www.codewars.com/kata/weight-for-weight**

## 题目
我和我的朋友约翰是减肥俱乐部的成员。约翰总是忧心忡忡的，因为每个月所有成员的体重都会列在一张表上，而他总是在表的最后一名，也就意味着他是最重的。我负责制作这张表，于是我告诉他："别再担心了，我会把名单的顺序修改一下。"我决定为每个数字分配一个重量属性。一个数字代表的重量的计算方法是取其各个位上的所有数字之和。
比如说：
"56 65 74 100 99 68 86 180 90" 按照数字重量来排序就变成了 "100 180 90 56 65 74 68 86 99"
当两个数字拥有同样的重量时，我们把他们当做字符串而非数字："100"排在"180"前面因为它的重量(1)比180的(9)要小，而180排在90前面因为两者重量相等(9)，但是180作为字符串排在90之前。
所以列表里的数字都是正数，列表可能为空。
注意：
输入的字符串中可能开头和末尾有额外的空格，两个连续的数字之间可能被不止一个空格分隔。
不要修改入参


## 原文

> My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.
I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.
All numbers in the list are positive numbers and the list can be empty.
Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
Don't modify the input
