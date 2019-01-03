# 缩减方向

**日期**: 2018.12.24

**等级**: 5

**链接：https://www.codewars.com/kata/directions-reduction**

## 题目
从前有一天在穿越蛮荒西部的路上，一个人收到了一份指示他行动的方向列表。方向可能是"NORTH", "SOUTH", "WEST", "EAST"(也就是东西南北)。很显然，北和南是反的，东和西也是如此。先向一个方向前进接着又走回头路显然是没什么意义的。由于这是蛮荒的西部，气候恶劣水源缺乏，为自己保持体能是很重要的，否则很快你就会死于干渴。


假设给定的方向是以下的列表：
`["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]`
或
`{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }`;

你马上就能看出向北走紧接着向南走是没有道理的，最好干脆别动。因此你的任务就是要给这个人一份简化版的列表，因此更好的行动计划应该是：`["WEST"]`或`{ "WEST" }`。

其他的例子：

对于`["NORTH", "SOUTH", "EAST", "WEST"]`，方向"NORTH" + "SOUTH"先北再南太浪费时间了，干脆啥也别干。接着剩下的路途就变成了`["EAST", "WEST"]`，东和西互相抵消，因此最后的结果就变成了[]。

对于 `["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]`，北和南并没有直接邻接着相反，但是在东和北抵消后北和南就邻接着了，因此整个路线就变成了`["WEST", "WEST"]`。

*任务*

编写一个函数dirReduc，入参为一个字符串数组，返回将相邻相反方向抵消后的字符串数组（相邻的W<->E 或者 S<->N）

更多例子参考测试用例。

*注意*
不是所有的路径都可以被简化的。路径`["NORTH", "WEST", "SOUTH", "EAST"]`就不能被缩减。北和西、西和南、南和东互相邻接且彼此无法互相抵消，因此处理后的结果依然为原路径：`["NORTH", "WEST", "SOUTH", "EAST"]`





## 原文

Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following:

`["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]`.
or

`{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }`;
or (haskell)

`[North, South, South, East, West, North, West]`
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

`["WEST"]`
or

`{ "WEST" }`
or (haskell)

`[West]`
or (rust)

`[WEST]`;
Other examples:
In `["NORTH", "SOUTH", "EAST", "WEST"]`, the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing.

The path becomes `["EAST", "WEST"]`, now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In `["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]`, "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to `["WEST", "WEST"]`.

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing. The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.

Examples
```
dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH", @"WEST"]); // => @[@"WEST"]
dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH"]); // => @[]
```
See more examples in "Example Tests"
Note
Not all paths can be made simpler. The path `["NORTH", "WEST", "SOUTH", "EAST"]` is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : `["NORTH", "WEST", "SOUTH", "EAST"]`.
