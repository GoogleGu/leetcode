# 蚂蚁桥

**链接：https://www.codewars.com/kata/ant-bridge**


## 题目
### 背景
我的造桥蚁宠物正在一块土地上由左向右前进。
如果它们遇到了一处沟壑，第一只会停下，然后下一只爬过它，接着再下一只，直到一座桥梁在沟上搭建起来。
它们多聪明啊！这样的话所有的蚂蚁都能从蚂蚁桥走过去了。
当最后一只蚂蚁走过去时，蚂蚁桥会以其建造的类似方式拆解。
这个过程可能会重复多次，因为可能有不止一个沟要过，直到所有蚂蚁都到达右边。

### Kata任务
我的小蚂蚁正在以ABCD排列的方式从左向右走。
在到达最右边时他们会以怎样的顺序离开？
注意：
```
- 是正常的陆地
. 是沟
```
蚂蚁的数量可能不同，但是蚂蚁的数量永远都足够搭桥跨越沟壑。
地形的起始和末尾不会是沟。
除了通过蚂蚁桥以外，蚂蚁不能穿过其他蚂蚁。
如果遇到特殊情况多只蚂蚁可以移动，后面的蚂蚁先动。

### 例子

输入
```
蚂蚁 = GFEDCBA
地形 = ------------...-----------
```
输出
```
结果 = EDCBAGF
```

详情
蚂蚁从左向右走。
```
GFEDCBA
------------...-----------
```
第一只蚂蚁到达沟壑。
```
GFEDCB     A
------------...-----------
```
它们开始搭桥...
```
GFED       ABC
------------...-----------
```
直到桥梁搭建完毕
```
GF         ABCDE
------------...-----------
```
剩下的蚂蚁越过桥梁。
```
               F
G          ABCDE
------------...-----------
```
直到没有更多的蚂蚁需要过桥...
```
           ABCDE        GF
------------...-----------
```
...蚂蚁桥一只一只开始拆掉自己...
```
             CDE      BAGF
------------...-----------
```
...直到所有的蚂蚁到达另一边。
```
                   EDCBAGF
------------...-----------
```


## 原文 
**Background**

My pet bridge-maker ants are marching across a terrain from left to right.
If they encounter a gap, the first one stops and then next one climbs over him, then the next, and the next, until a bridge is formed across the gap.
What clever little things they are!
Now all the other ants can walk over the ant-bridge.
When the last ant is across, the ant-bridge dismantles itself similar to how it was constructed.
This process repeats as many times as necessary (there may be more than one gap to cross) until all the ants reach the right hand side.

**Kata Task**

My little ants are marching across the terrain from left-to-right in the order A then B then C...
What order do they exit on the right hand side?
Notes
```
- = solid ground
. = a gap
```
The number of ants may differ but there are always enough ants to bridge the gaps
The terrain never starts or ends with a gap
Ants cannot pass other ants except by going over ant-bridges
If there is ever ambiguity which ant should move, then the ant at the back moves first

**Example**

Input
```
ants = GFEDCBA
terrain = ------------...-----------
```
Output
```
result = EDCBAGF
```
Details

Ants moving left to right.	
```
GFEDCBA
------------...-----------
```
The first one arrives at a gap.	
```
GFEDCB     A
------------...-----------
```
They start to bridge over the gap...	
```
GFED       ABC
------------...-----------
```
...until the ant-bridge is completed!	
```
GF         ABCDE
------------...-----------
```
And then the remaining ants can walk across the bridge.	
```
               F
G          ABCDE
------------...-----------
```
And when no more ants need to cross...	
```
           ABCDE        GF
------------...-----------
```
... the bridge dismantles itself one ant at a time....	
```
             CDE      BAGF
------------...-----------
```
...until all ants get to the other side	
```
                   EDCBAGF
------------...-----------
```