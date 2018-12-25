# 最佳旅程

**日期**: 2018.12.13

**等级**: 5

**题目链接**：https://www.codewars.com/kata/best-travel

## 题目
约翰和玛丽想要在几个小镇ABC等之间旅行，玛丽手上有一份这些城镇之间距离的清单：ls = `[50, 55, 57, 58, 60]`。约翰开车开得很累，他和玛丽说他不想开超过t = 174英里的距离，并且他只愿再造访三个小镇。

为了让玛丽和约翰都尽可能开心，他们会选择开多少距离，去哪些城镇，以此来最大化开车的距离，同时又满足约翰提的条件？

例子：

用列表ls和只访问三个小镇，他们可以在以下旅程中选择： `[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60]`.

这些距离的总和即为162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

小于174的最大距离因此是173，符合条件的三个城镇是 `[55, 58, 60]`。

函数chooseBestSum(或choose_best_sum or ... 依语言耳钉）接受入参t（距离和的上限，非负整数），k（要访问的城镇数，k>=1)以及ls（距离的数组，所有的距离都为正整数，该数组至少有一个元素），函数返回在允许范围内的最大距离和，如果不存在一个有效解，则返回null或none等相关语言内代表空的值，C++, C, Rust, Swift, Go, Kotlin 返回 -1。

示例

ts = `[50, 55, 56, 57, 58]` choose_best_sum(163, 3, ts) -> 163

xs = `[50]` choose_best_sum(163, 3, xs) -> nil 或 null 或 none 或 -1 (C++, C, Rust, Swift, Go)

ys = `[91, 74, 73, 85, 73, 81, 87]` choose_best_sum(230, 3, ys) -> 228


## 原文

John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = `[50, 55, 57, 58, 60]`. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John- ?

Example:

With list ls and 3 towns to visit they can make a choice between: `[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60]`.

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is `[55, 58, 60]`.

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. With C++, C, Rust, Swift, Go, Kotlin return -1.

Examples:

ts = `[50, 55, 56, 57, 58]` choose_best_sum(163, 3, ts) -> 163

xs = `[50]` choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)

ys = `[91, 74, 73, 85, 73, 81, 87]` choose_best_sum(230, 3, ys) -> 228