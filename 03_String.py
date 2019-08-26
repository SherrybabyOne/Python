# [1]字符串格式化
# %d表示整数 %s表示文本 %.1f表示一位小数
s1 = '欢迎%d号机，来自%s的最强王者来本网咖消费，免费赠送%d小时上网时长,%.2f'
print(s1%(20,'诺克萨斯',10,8.88))

# [2]find函数
s2 = "2019年8月26日东北大学Python课程实训"
# 通过find函数可以获取查询元素的开始下标
# 找不到的情况下，返回值为-1
# 规定查询的区间 第一个参数： 要查询的元素，第二个参数： 开始查询的下标，第三个参数： 结束查询的下标
print(s2.find('东北大学'))

# [3]英文大小写的转换
print('Python is not the Best'.lower())
print('python is not the best'.upper())

# [4]判断大小写
print('Y'.isupper())
print('abC'.islower())

# [5]文本的替换
s3 = '我要学习Python，Python'
# 第一个参数： 旧数据，第二个参数： 新数据，第三个参数： 要替换的个数(默认替换全部)
print(s3.replace('Python','JavaScript',3),s3)
# 注意：replace替换的数据，不会影响到有关的数据

# [6]去除字符串的空格
s4 = '    Python   '
print(s4.strip(),s4)
print(s4.replace(' ',''))