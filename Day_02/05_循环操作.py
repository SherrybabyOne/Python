
# [1]赋值操作
a = 10;
b = 20;
# 通过序列解包的的形式赋值
x,y,z = "上路","下路","中路";
print(x,y,z);
# 交换数据
x,z = z,x;
print(x,y,z);
# [2]循环操作
# while循环
list_01 = ["亚瑟","李白","蔡文姬","荆轲"]
i = 0;
while i<len(list_01):
    print(list_01[i])
    i+=1;
    pass
# while True:
#     pass
# for循环的几种表现形式[1,4)
for j in range(0,len(list_01)):
    print("%d = %s"%(j,list_01[j]))
    pass
print("=======for循环倒序查询==========")
# for循环倒序查询
for k in range(len(list_01)-1,-1,-1):
    print("%d = %s"%(k,list_01[k]))
    pass
print("====================")
for j in range(0,10,2):
    print(j)
    pass
print("===================")
for item in list_01:
    print(item)
    pass
# 稍微复杂一些for循环
print("========稍微复杂一些for循环=========")
list_02 = [["星期一","星期二","星期三"],["星期四","星期五","星期六"]]
for a in list_02:
    print(a)
    for b in a:
        print(b)
        pass
    pass

print("===================")
for x,y,z in list_02:
    print(x)
    print(y)
    print(z)
    pass
# 针对字典的for循环-
d_01 = {"01":"华为","02":"小米","03":"苹果","04":"努比亚"}
# 方式一:
for item in d_01:
    print(item+"对应的值："+d_01[item]);
    pass
# 方式二
for key in d_01.keys():
    print(key)
    pass
# 方式三
for key,value in d_01.items():
    print(key+":"+value);
    pass
# 方式四
for kn in d_01.items():
    print(kn)
    pass
# 练习：乘法口诀 通过Python for循环形式打印控制台
print("===================================");
# 跳过当前将要执行循环:continue
print("=======跳过当前将要执行循环========")
for i in range(0,100):
    if i%10 == 0:
        continue
        pass
    print(i)
    pass
# 结束循环
print("=======结束循环========")
for i in range(1,100):
    if i%10 == 0:
        break
        pass
    print(i)
    pass

