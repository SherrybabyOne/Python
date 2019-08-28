
# [1]类的创建和使用
class Student():
    # 定义属性
    name = "李白"
    age = 18;
    # 构造函数
    def __init__(self):
        print("构造函数的调用！")
        # self 表示当前类本身:在构造函数中声明当前类的属性
        self.sex = "男";
        # 两个下划线定义私有化属性
        self.__add = "北京";
        pass
    # 函数 - 方法
    def Run(self):
        print("可以行走！！")
        pass
    # 定义函数修改属性
    def setAge(self,age):
        # 函数修改当前类的属性
        self.age = age;
        pass
    # 定义函数私有化属性：给私有属性赋值
    def setAdd(self,add):
        self.__add = add;
        pass
    def getAdd(self):
        return self.__add;
        pass
    pass
# 实例化
st_01 = Student();
print(st_01.name,st_01.age,st_01.sex);
# [2]属性的修改
st_01.age = "一百";
print(st_01.age)
# [3]调用实例类的函数
st_01.Run();
# 通过函数修改当前类的属性
st_01.setAge(1000);
print(st_01.age)
# 调用私有化属性设置的函数
st_01.setAdd("辽宁")
print(st_01.getAdd())

# [02]沟通构造函数传入参数实例化
class Studen_01():
    def __init__(self,name,age = 19):
        self.name = name;
        self.age = age;
        pass
    pass
# 实例化
st_02 = Studen_01("张三")
print(st_02.name,st_02.age)