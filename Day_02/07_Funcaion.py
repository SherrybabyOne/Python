
# 函数的创建和使用
# [1]基本的函数
def func():
    print("2019年8月27日 今天天气不错");
    pass
func();
# # [2]位置参数:必须传值
def func_01(a,b):
    print(a,"+",b,"=",a+b);
    pass
func_01("2019年8月27日","不好");
# # [3]默认参数值:默认参数值不强制传入参数
def func_02(datatime,c = "去考试！！！"):
    print(datatime,c);
    pass
func_02("2019年8月27日")
func_02(c=123,datatime="2019年8月27日");
# # [4]参数组的形式:1.可以传递多个参数值，通过索引进行获取  2.参数可以不传递，不限制数据类型
def func_03(*args):
    print(len(args))
    print(args[1])
    pass
func_03([1,2,3,4],[5,6,7,8])
# func_03()
# # [5]带返回值的函数
def func_04(a,c):
    return a+c;
    pass
print(func_04(10,50))
# # 5.1返回多个数值
def func_05(a,b):
    return a,b,a+b;
    pass
x,y,z = func_05("上午","下午")
print(x)
print(y)
print(z)
# # [6]递归 = 修改全局变量
i = 0;
def func_06():
    # 【注意】递归调用有上限限制
    # 函数要修改全局变量必须 修改全局变量的声明：global，
    global i;
    print(i);
    i+=1;
    # 递归调用
    if i>=997:
        return
    func_06();
    pass
func_06();
