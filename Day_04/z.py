# [1]导包
import pymysql;
# [2]创建和连接数据库
# db = pymysql.connect(host="localhost",user="root",passwd="qwer",port=3306,db="test",charset="utf8");
db = pymysql.connect(host="localhost",user="root",passwd="qwer",port=3306,db="test",charset="utf8");
print(db)

print('连接成功了！')