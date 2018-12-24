# 字母战争-牧师版

**日期**: 2018.12.7

**等级**: 5

**链接：https://www.codewars.com/kata/alphabet-war-wo-lo-loooooo-priests-join-the-war**

## 介绍
这是一场没有人知道的战争——字母战争！
有两组敌对的字母，左右两派字母之间剑拔弩张，最终走向了战争。他们刚刚发现了一种新的军事单位：牧师。

## 任务
编写一个函数，接受一个只包含小写字母的字符串，然后返回战斗结果：当左派赢的时候返回Left side wins!，右派赢的时候返回Right side wins!，如果平手则返回Let's fight again!。
左派字母及它们的战斗值：
```
 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (但是这一个牧师，有特殊能力)
```
右派字母及它们的战斗值：
```
 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (但是这一个牧师，有特殊能力)
```
其他字母没有战斗值，只是战斗中的待宰羔羊。
牧师单位t和j可以将相邻的敌方字母转化成具有相同战斗值的己方字母。
```
mtq => wtp
wjs => mjz
```
同时被两j和t邻接的字母不被转化：
```
tmj => tmj
jzt => jzt
```
牧师单位j和t不能转化对方的牧师( jt => jt)。
运行示例：
```
alphabet_war("z")         #=>  "z"  => "Right side wins!"
alphabet_war("tz")        #=>  "ts" => "Left side wins!" 
alphabet_war("jz")        #=>  "jz" => "Right side wins!" 
alphabet_war("zt")        #=>  "st" => "Left side wins!" 
alphabet_war("azt")       #=> "ast" => "Left side wins!"
alphabet_war("tzj")       #=> "tzj" => "Right side wins!"
```


> Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters have discovered a new unit - a priest with Wo lo looooooo power.
Task
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
The left side letters and their power:
```
 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (but it's priest with Wo lo loooooooo power)
```
> The right side letters and their power:
```
 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (but it's priest with Wo lo loooooooo power)
```
> The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly letters with the same power.
```
mtq => wtp
wjs => mjz
```
> A letter with adjacent letters j and t is not converted i.e.:
```
tmj => tmj
jzt => jzt
```
> The priests (j and t) do not convert the other priests ( jt => jt).
> Example
```
alphabet_war("z")         #=>  "z"  => "Right side wins!"
alphabet_war("tz")        #=>  "ts" => "Left side wins!" 
alphabet_war("jz")        #=>  "jz" => "Right side wins!" 
alphabet_war("zt")        #=>  "st" => "Left side wins!" 
alphabet_war("azt")       #=> "ast" => "Left side wins!"
alphabet_war("tzj")       #=> "tzj" => "Right side wins!"
```