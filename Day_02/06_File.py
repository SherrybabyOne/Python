
# [1] 文本读取
# 第一个参数：打开文件的路径
# 第二个参数：读写方式 r表示只读 w 表示写入 a表示追加
# 第三个参数：缓存模式 1表示缓存 0表示不缓存 默认：1
# 第四个参数：编码格式的设置
# 打开文件
file = open("/Users/aihao/Desktop/Demo/Python实训/Day_02/a.txt","r",1,encoding="utf-8");
# C:\\Users\\MrLiu\\Desktop\\abc.txt
# 读取文件
print(file.read())
# 关闭文件
file.close()
# [2]写入文件
# 打开一个文件
file_01 = open("/Users/aihao/Desktop/Demo/Python实训/Day_02/b.txt","w",1,encoding="utf-8");
# 写入一个信息
file_01.write("2019年8月27日高价宿舍上头条")
# 关闭
file_01.close()
# [3]判断路径是否存在
file_path = "/Users/aihao/Desktop/Demo/Python实训/Day_02/东北大学/"
# 判断路径是否存在
import os;
print(os.path.exists(file_path));
# os.path.exists 用于检测路径是否存在 True False
if not os.path.exists(file_path):
    # 创建文件
    os.makedirs(file_path);
    print("路径创建成功")
    pass
else:
    print("路径存在")
    pass
# [2]写入文件
# 打开一个文件
file_01 = open(file_path+"头条日.txt","w",1,encoding="utf-8");
# 写入一个信息
file_01.write("2019年8月27日高价宿舍上头条")
# 关闭
file_01.close()


# C:\/Users\/MrLiu\/Desktop\/东北大学\/