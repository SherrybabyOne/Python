
# 人
class Person(object):
    # 构造函数
    def __init__(self,name,age,sex,money):
        self.name = name;
        self.age = age;
        self.sex = sex;
        self.money = money;
        pass
    # 函数 - 方法
    def Run(self):
        print("这是一个人的实体对象，可以行走")
        pass
    # [1]私有方法
    def __abc(self):
        print("该方法为私有方法，不能被继承")
        pass
    pass

