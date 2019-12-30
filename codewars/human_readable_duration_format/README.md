# 易读的时间段表示

**日期**: 2019.1.9

**等级**: 4

**链接：https://www.codewars.com/kata/human-readable-duration-format**

## 题目

你的任务是编写一个函数，它接受一个代表多少秒的整数，将其以易读的形式返回。

这个函数的入参是非负整数，如果是0的话则返回"now"。否则以年日时分秒的形式将入参表示的时间长度返回。

用例子来解释更好理解一些：

```
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```

在这个题目中，一年有365天，一天有24小时。
注意返回的答案中的空格不能省略。

### 详细规则
返回的结果由诸如4 seconds, 1 year等部分组成。一般情况下，每个部分由一个正整数和时间单位以及间隔它们的空格来组成。如果整数部分大于1则时间单位应为复数形式。

各个部分之间由一个逗号加一个空格分隔(", ")。但是最后一部分和倒数第二部分之间要像英语里的用法一样，使用" and "来间隔的。

表示时间段更长的单位应该排在前面，也即1 second and 1 year是错误的, 而1 year and 1 second才是正确的。

各个部分的时间单位都不一样，因此不能有像5 seconds and 1 second这样单位重复的部分。

如果某个部分的整数值为0，则该部分不会展示。因此1 minute and 0 seconds是不正确的，应该表示为1 minutes。

能使用较大的时间计量单位时必须用更大的，也即61 seconds是不对的，应该表示为1 minute and 1 second。

## 原文

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

```
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

### Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
