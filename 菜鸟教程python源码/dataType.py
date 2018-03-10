#!/usr/bin/python3
'''
变量：Python在使用变量之前必须赋值，
变量名：以字母或者下划线开头，紧跟着字母下划线和数字
变量声明时不需要指定数据类型，赋值什么类型的值，变量就是什么类型的

'''

# 变量赋值
TEST = 123;
print(type(TEST));
TEST = 'hello world';
print(type(TEST));
# 多个变量赋值
a = b = c = 124;
print(a,b,c);3
a,b,c = 12,22,33;
print(a,b,c);

# 数据类型type函数
strs = "hello world"
print(type(str))
num = 1000
print(type(num))
boolean = True
print(type(boolean))

# instance 函数
print(isinstance(num, int))
print(isinstance(strs, str))
# del关键字，删除变量
print(num)
del num
# print(num)
# string
print(strs)
print(strs[0:5])
print(strs[6:12])
print(strs[0])
# 字符串拼接
print("hello" + "world")
# 字符串重复
print("hello world" * 3)

# list列表
ll = ["hello", "world", "test1"]
print(ll)
print(ll[0])
print(ll[1:2])
print(ll+ll)
print(ll * 3)



