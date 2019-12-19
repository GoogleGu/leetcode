# 我的朋友在作弊吗

**日期**: 2018.12.28

**等级**: 5

**链接：https://www.codewars.com/kata/is-my-friend-cheating**

## 题目

- 我的一个朋友接受一组从1到n的数字。
- 在这个序列里，他会挑选两个数字，a和b。
- 他说a和b的积等于序列里除了a和b以外所有数的和。
- 给定一个数字n，你能告诉我他排除的是哪个数字吗？
- 函数应该接受正整数n为参数，返回以下形式的数组：

`[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]` 其中所有的(a, b)是可以从1到n中移除的数字。结果应该以a升序排列。

（a, b）的组合往往有多种可能。如果没有可能移除的ab组合，返回空数组，这表明我的朋友在说谎！

详细的输入输出例子见测试用例。


## 原文

- A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
- Within that sequence, he chooses two numbers, a and b.
- He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
- Given a number n, could you tell me the numbers he excluded from the sequence?
- The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

`[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]`
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

`[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".`

It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).

(See examples of returns for each language in "RUN SAMPLE TESTS")

Examples:
removNb(26) should return` [(15, 21), (21, 15)]`
or

removNb(26) should return `{ {15, 21}, {21, 15} }`
or

removeNb(26) should return `[[15, 21], [21, 15]]`
or

removNb(26) should return` [ {15, 21}, {21, 15} ]`
or

removNb(26) should return `"15 21, 21 15"`
or

in C:
removNb(26) should return  **an array of pairs` {{15, 21}{21, 15}}`**
tested by way of strings.
