# RGB转换为十六进制

**日期**: 2018.12.18

**等级**: 5

**链接：https://www.codewars.com/kata/rgb-to-hex-conversion**

## 题目

rgb()方法尚未完成。将该方法写完，它应该接受RGB的十进制数字，返回对应的十六进制表达。RGB的有效十进制数值范围是0-255.任何不在该范围内的入参都应被近似为最接近的有效值。

以下为期望输出的例子。

```
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3 
```

## 原文

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:
```
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3 
```