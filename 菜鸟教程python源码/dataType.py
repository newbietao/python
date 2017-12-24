#!/usr/bin/python3
'''
变量：Python在使用变量之前必须赋值，
变量名：以字母或者下划线开头，紧跟着字母下划线和数字
变量声明时不需要指定数据类型，赋值什么类型的值，变量就是什么类型的

'''
# 变量赋值
test = 123;
print(type(test));
test = 'hello world';
print(type(test));
# 多个变量赋值
a = b = c = 12;
print(a,b,c);
a,b,c = 12,22,33;
print(a,b,c);
