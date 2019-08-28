# 父亲
class Father():
    def __init__(self,getmoeny,name):
        self.getmoeny = getmoeny;
        self.name = name
        pass
    # 共有的函数
    def Run(self):
        print("父亲")
        pass
    # 共有的函数
    def Run1(self):
        print("父亲不同")
        pass
    pass

# 母亲
class Mother():
    def __init__(self,remoeny,name):
        self.remoeny = remoeny;
        self.name = name
        pass
    # 共有的函数
    def Run(self):
        print("母亲")
        pass
    def Run2(self):
        print("母亲不同")
        pass

    pass





# 孩子继承父亲和母亲所有的属性
class Child(Father,Mother):
    # 需要重写构造函数
    def __init__(self,getmoney,remoney,name):
        # 调用父亲和母亲的构造函数 - 才能完成孩子的实例化
        # 调用父亲: Child Father Mother Teach
        super(Child,self).__init__(getmoney,name)
        super(Father,self).__init__(remoney,name)

        pass
    pass
# 实例化:继承了父亲和母亲，拥有父亲和母亲花钱和挣钱的属性
ch_01 = Child(100,50,"小白");
print('父亲挣钱',ch_01.getmoeny)
print('母亲花钱',ch_01.remoeny)
ch_01.Run()
ch_01.Run1()
ch_01.Run2()
print(ch_01.name)

