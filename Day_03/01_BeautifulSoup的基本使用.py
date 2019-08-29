
# [1]导入包
import urllib.request
# 导入网页结构解析的包
from bs4 import BeautifulSoup
# [2]目标网址
url = "https://www.i4.cn/ring_23_0_1.html";
# [3]访问网络
html = urllib.request.urlopen(url);
# [4]获取访问到的数据
data = html.read();
# ==============================================================
# [5]数据存储到本地
file_html = open("./Day_03/爱思助手铃声.html","wb",1)
file_html.write(data)
file_html.close()
html.close()
# ==============================================================
# [6]Beautiful soup的使用
# 6.1 创建一个soup对象
# soup = BeautifulSoup(open("01_爱思助手铃声.html"));
soup = BeautifulSoup(data,"html.parser");
# [7]掌握Beautiful基本使用方法
# Tag , NavigableString , BeautifulSoup , Comment
print(type(soup));
# 7.1获取标签:通过标签的形式获取
print(soup.title);
# 7.2获取标签中的文本信息
print(soup.title.string)
# 7.3获取标签的名称
print(soup.title.name);
# 7.4查找标签的父容器
# print(soup.title.parent);
# 7.5通过find函数来查找 = 可以追加条件
# find函数只会查找第一个匹配到的数据
# name="description"
link_01 = soup.find("meta",attrs={"name":"description"});
print(link_01);
# 7.6findall
metas = soup.find_all("meta");
print(len(metas))
print(metas)
print("========================")
for item in metas:
    print(item)
    pass
# ==============================================================================
# 查询所有音乐的容器
div_all = soup.find_all("div",attrs={"class":"list ring_list"});
print(len(div_all));
# print(div_all)
# 遍历查询每一个div标签
i = 0;
for div_item in div_all:
    print("第%d首铃声div容器：\n"%i)
    print(div_item)
    print("***********"*5)
    # 获取音乐名称
    mp3_name = div_item.find("div",attrs={"class":"title"}).string;
    print(mp3_name)
    # 获取铃声的下载地址：
    mp3_url = div_item.find("div",attrs={"title":"播放"})["data-mp3"]
    print(mp3_url)
    # 下载保存
    # 相对路径
    file_path = "abc"
    import os
    if os.path.exists(file_path):
        print("文件夹存在")
        pass
    else:
        os.makedirs(file_path)
        print("文件创建成功")
        pass
    urllib.request.urlretrieve(mp3_url,"abc/%s.mp3"%mp3_name);
    # 获取音乐
    i+=1;
    pass




