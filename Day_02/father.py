
# 父亲的类
# 导入包
from Case03.person import Person
class Father(Person):
    # [1]重写构造函数
    def __init__(self,getmoney):
        # 调用父类的构造函数进行赋值: super(Father,self)
        # super(Father,self).__init__(name,age,sex,money)
        self.getmoney = getmoney;
        pass
    # [2]重写函数
    def Run(self):
        print("这是一个父亲的实体类，可以奔跑");
        pass
    # [3]父亲的方法
    def getMM(self):
        print("父亲需要挣钱")
        pass
    pass
# # 实例化父亲的类
# fa_01 = Father("李白",18,"男",1000,1000);
# # 调用继承的属性
# print(fa_01.name);
# # 调用继承的函数
# fa_01.Run()
# # 无法找到私有化的函数：私有化的函数不能被继承
# # fa_01.__abc();

