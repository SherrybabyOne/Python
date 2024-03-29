
# [1]常规字典的创建和使用
d_01 ={"01":"宋小宝","02":"黄渤","03":"王宝强"}
#根据键值对的Key值进去获取
print(d_01["01"]);
# [2]通过字典函数进行创建
# 2.1 通过数组转换成字典的格式
ar_01 = [("01","宋小宝"),("02","黄渤"),("03","王宝强")];
# 转换
d_02 = dict(ar_01);
print(d_02)
# 2.2 成员资格是否适用于字典形式：
# 【注意】只能查询到 Key值是否存储
print("宋小宝" in d_02);
# [3]通过key修改对应value值：
# 输出形式
print("d_01旧数据为：",d_01);
d_01["01"] = "潘长江"
print("d_01新数据为：",d_01);
# [4]删除一个元素
del d_01["01"];
print(d_01)
# [5]清空字典
d_01.clear()
print(d_01)


