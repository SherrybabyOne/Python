
# 孩子的类 - 继承父亲和母亲
# 导入父亲和母亲的类
from Case03.father import Father
from Case03.mother import Mother
# 多继承  继承多个类，需要使用逗号分隔
class Child(Mother,Father):
    # 补全父亲和母亲的构造函数
    def __init__(self,getmoney,remoney):
        # 第一步：补全母亲
        super(Child,self).__init__(remoney);
        # 第二步：补全父亲
        super(Mother,self).__init__(getmoney);
        pass


    pass

# [1]实例化孩子的类
ch_01 = Child(50,20);
# [2]调用父亲和母亲的属性
print(ch_01.getmoney)
print(ch_01.remoney)
# [3]调用父亲和母亲的函数
ch_01.getMM()
ch_01.rmMM()
# [3]在调用共有的函数的时候:拥有先继承的函数
ch_01.Run()

