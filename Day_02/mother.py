
# 母亲的类
# 导入包
from person import Person
class Mother(Person):
    # [1]重写构造函数
    def __init__(self,remoney):
        # 调用父类的构造函数进行赋值: super(Father,self)
        # super(Mother,self).__init__(name,age,sex,money)
        self.remoney = remoney;
        pass
    # [2]重写函数
    def Run(self):
        print("这是一个母亲的实体类，可以飞");
        pass
    # [3]母亲的方法
    def rmMM(self):
        print("母亲需要花钱")
        pass
    pass
# # 实例化父亲的类
# fa_01 = Mother("李白",18,"男",1000,1000);
# # 调用继承的属性
# print(fa_01.name);
# # 调用继承的函数
# fa_01.Run()
# # 无法找到私有化的函数：私有化的函数不能被继承
# # fa_01.__abc();

