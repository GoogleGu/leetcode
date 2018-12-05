# Tribinacci数列

**链接：https://www.codewars.com/kata/tribonacci-sequence/python**

Tribinacci 数列是菲比那齐数列的变种，前三项数字可以自定，之后的每项为前三项之和。因此如果一个 Tribinacci 数列的前三项为`[1,1,1]`的话，我们将得到以下数列：
`[1, 1 ,1, 3, 5, 9, 17, 31, ...]`
但是如果我们以`[0, 0, 1]`开头的话，将会得到如下数列：
`[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]`
那么问题就来了，写出一个函数，它需要接受一个外界给定的前三项（称为签名数列），并依此返回由此生成的 Tribinacci 数列的前 n 个元素组成的数列。
输入函数的签名数列永远包含3个数字，输入函数的n永远为非负整数。如果 `n == 0`，则函数应返回空数列。

> Well met with Fibonacci bigger brother, AKA Tribonacci.
> As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
> So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
> [1, 1 ,1, 3, 5, 9, 17, 31, ...]
> But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
> [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
> Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
> Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array and be ready for anything else which is not clearly specified ;)
