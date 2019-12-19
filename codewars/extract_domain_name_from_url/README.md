# 从url中抽取域名

**日期**: 2018.12.26

**等级**: 5

**链接：https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1**

## 题目

编写一个函数，其入参为字符串形式的url，将其中的域名解析出来并以字符串的形式返回，比如：

```
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```


## 原文

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```