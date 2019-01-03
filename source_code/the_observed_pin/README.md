# 偷窥到的密码

**日期**: 2018.12.28

**等级**: 4

**链接：https://www.codewars.com/kata/5263c6999e0f40dee200059d**

## 题目

好了，侦探先生，我们的一个同事成功地监视了我们的目标大盗先生。我们跟踪他到了一间秘密仓库，在那里应该能找到所有赃物。仓库的门被一个密码锁锁着。很不幸的是我们的同事在大盗输入密码的时候没能看准他输的是啥。
密码锁键盘布局如下：

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

他注意到了密码是1357，但是他还说可能他看到的每个数字是其相邻的数字（垂直或水平方向的相邻，斜角不算相邻）。举个例子，他看到的第一位数字可能不是1，而是2或4.而看到的5可能不是5，而是2，4，6，8中的一个。

他还提到他认识这种锁，你可以无限次数地输入错误密码也不会触发警报或导致系统锁死。因此我们可以将所有可能的变化都尝试一遍。（在这里我们说的所有可能的变化是指被监测到的密码本身和所有考虑到相邻数字的组合变化）

你能不能帮我们找出所有的这些变化？最好是能写个函数，对于输入的一个1到8位长度的密码，将其所有的变化以列表的形式输出。注意所有的密码，包括输入的和输出的都是以字符串的形式存储的，因为可能开头为0。具体的输入和输出请看测试用例。

侦探先生，我们全靠你了！

## 原文

Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!