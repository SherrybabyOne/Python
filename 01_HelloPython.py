
# [1]注释方式：两种
# 单行注释  Ctrl+/

'''

'''
"""
多行注释
"""
# [2]Python输出语句
print("2019年8月26日 东北大学Python人工智能短期实训");
# 在Python2.x版本中不支持中文的显示:需要添加# coding=utf-8
# coding=utf-8
# print ""

# [3]数据类型 - 变量
# Python是动态数据语言，变量的数据类型在被赋值的时候定义
# int it = 3;
a = 3;
# type()函数：查看数据的类型
print(type(a));
b = 3.14
print(type(b))
c = "2019年8月26日 - 计科专业 - 2016级"
print(type(c))
# 【注意】在Python中bool类型必须为：True False;
d = False
print(type(d))
# [4]运算
"""
+ - * / %
"""
print(2+4)
print(4-2)
# 【注意】"/"除法运算中，两个整数相除，会的到一个以为小数点的浮点类型
print(4/2)
# 【注意】两个整数相除，除不尽的情况
print(5/3)
# 1.1Python  "//" 在运算过程中只保留整数部分，舍弃小数部分
print(5//3)
print(5.0//3)
# 练习：3.14159 //3  练习乘法
# 1.2 双**的运算:次方
print(2**3);
# 取余数
print(7%3)
# [5]比较运算符
"""
> = < >= 
"""
e = 65
print(70>e)
print(50>e)
'''
if(e>50&&e<70){

}
'''
# 【注意】Python中支持连续比较
print(50<e<70);

# [6] 条件语句 - 语法结构 :pass 占位符
# 作用域：代码作用域是通过首行缩进来决定
if e<60:
   print("没有及格！！");
   pass
elif 60<=e<=80:
    print("成绩及格")
    pass
else:
    print("成绩优异")
    if e==100:
        print("成绩满分")
        pass
    pass






