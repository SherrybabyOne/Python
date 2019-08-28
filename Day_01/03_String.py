
# [1]字符串格式化
# %d 表示整数字 %s表示文本 %.2f 表示2位小数
s1 = "欢迎%d号机，来自%s的最强王者来本网咖上网，免费赠送%.3f小时上网时长";
print(s1%(20,"诺克萨斯",10.95343))
# [2]find函数
s2 = "2019年8月26日东北大学Python课程实训东北大学"
# 通过find函数可以获取要查询元素的开始下标，只适配到第一个参数为止
# 找不到的情况下，返回值为：-1
print(s2.find("东北大学"))
print(s2.find("哈工大"))
# 规定查询区间:第一个参数：要查询的元素 ，第二个参数：开始查询的下标，第三参数：结束查询的下标
print(s2.find("东北大学",11,-1))
# [3]英文大小写的转换
print("Python is The Best".lower())
print("Python is The Best".upper())
# [4]判断大小写
print("Y".isupper())
print("W".islower())
# [5]文本的替换
s3 = "2019年8月26日东北大学Java课程实训东北大学 - Java"
# 第一个参数：旧数据 第二个参数：新数据 第三个参数：要替换的个数,默认参数：全部替换
print(s3.replace("Java","Python",3))
# 【注意】replace替换的数据，不会影响到有关的数据
print(s3)
# [6]去除字符串的空格
s4 = "   ====== = = = = =    "
print(s4)
print(s4.strip());
print(s4.replace(" ",""))

