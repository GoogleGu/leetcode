# 贪婪游戏

**日期**: 2018.12.6

**等级**: 5

**链接：https://www.codewars.com/kata/greed-is-good**

贪婪游戏是种用五个六面骰子玩的游戏。你的任务就是按照以下的规则来为掷出的结果打分。你的输入永远是一组由五个六面骰掷出的结果组成的数组，得分规则如下：
 三个1 => 1000 points
 三个6 =>  600 points
 三个5 =>  500 points
 三个4 =>  400 points
 三个3 =>  300 points
 三个2 =>  200 points
 一个1   =>  100 points
 一个5   =>   50 point
在一次掷骰结果中，每个骰子只能被计分一次。比如说，一个5只能被算为三个五中的一部分来计分，或是单独计为50分，但是不能同时算两次分。
打分的例子如下：
 ```
 掷骰结果      分数
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450
```


> Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
Example scoring
 ```
 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450
```