
# [1] 索引 - 下标
# Python语法中，最简单的数据结构 - 序列
s1 = "2019年8月26日东北大学Python课程实训"
# 通过索引找到对应的元素:两个索引实现分割需要通过":" 第一个参数：开始截取的位置，第二个参数：结束截取的前一位
print(s1[4]);
# 【注意】Python中，索引的定义双向定义：正方向：从0开始，反方向：从-1开始
# 输入语句可以用逗号做输出数据量
print(s1[-1],s1[-3]);
# [2]分片截取:通过索引截取 - -  包前不包后的原则s1[10:14)
print(s1[10:14])
print(s1[-14:-10])
print(s1[10:-10]);
# [2]数组的分割处理:分割完的数据，数据类型不发生变化
array_01 = [1,2,3,4,5,6,7,8,9,0];
print(array_01[1:5]);
print(array_01[1:])
print(array_01[:])
print(array_01[2:9:4]);
# [3]序列相加
print([1,2,3]+[4,5,6])
print([1,2,3]+["热情","人群"])
# 需要注意数据类型不同，不能够相加
# print([1,2,3]+"2019年8月26日")
# [4]乘法 = 序列
print("****"*10)
print([1,2,3]*10)
# [5] 成员资格
s2 = "2019年8月26日东北大学Python实训"
# python中成员资格返回数据的的格式bool类型：True False
print("东北大学" in s2);
s3 = ["狄仁杰","蔡文姬","李白","亚瑟","妲己"]
print("狄仁杰" in s3);
# [6]最大值 最小值 数据长度
print(max(array_01));
print(min(array_01))
print(len(s3))
# 英文 比较大小
s4 = "abcde"
print(min(s4))
# [7]序列的基本操作
s5 = ["狄仁杰","蔡文姬","李白","亚瑟","妲己"]
# 7.1根据索引进行重新赋值
s5[2] = "娜可露露"
print(s5)
# 7.2 删除一个元素
del s5[2]
# 通过下表删除
# s5.pop(0)
del s5[0]
print("=====",s5)
# 7.3添加一个元素
# s5.append("韩信")
# 7.4根据索引插入一个元素
s5.insert(2,"韩信")
print(s5)
# 7.5 查看重复元素个数
s5.insert(0,"韩信")
print(s5)
print(s5.count("韩信"))
# 7.6分片删除
del s5[0:3]
print(s5)




