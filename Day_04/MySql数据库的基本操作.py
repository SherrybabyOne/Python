
"""
1.创建数据库的连接对象
2.获取cursor游标
3.执行语句
4.处理数据
5.关闭cursor游标
6.关闭数据库连接对象

"""
# [1]导包
import pymysql;
# [2]创建和连接数据库
db = pymysql.connect(host="localhost",user="root",passwd="qwer",port=3306,db="test",charset="utf8");
print(db)
# [3]获取游标 - 用来给数据库发送sql语法，执行数据操作
cur = db.cursor();
# [4]执行sql语法
# 判断，如果数据表标存在，进行删除

# cur.execute("drop table if exists tao")

sql_01 = """
CREATE TABLE `tao` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(50) COLLATE utf8_bin NOT NULL,
  `PASSWORD` varchar(50) COLLATE utf8_bin NOT NULL,
  `ADDRESS` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin

"""
# 插入一条数据
sql_02 = """
insert into `test`.`taro` (`NAME`, `PASSWORD`, `ADDRESS`) values ('曹操', '123456', '三国')
"""
# [5]开启事务
db.begin();
# [6]执行sql语法
# cur.execute(sql_01);
# 执行一条插入语句
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
cur.execute(sql_02);
# 提交事务
db.commit()
# [7]关闭事务
cur.close();
# [8]关闭数据连接
db.close();
print("创建成功")


























