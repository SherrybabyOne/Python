
# [1]准备工作
import requests;
from bs4 import BeautifulSoup
import pymysql;
import os;
import time;
# [2]准备工作
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"};
# 网址的URL
yz_url = "https://search.uzai.com/%s/1/0/0/"
# 本地存储访问记录的文件夹
file_data = "访问记录";
# [3]获取当前系统时间
def GetNewTime():
    # %Y %m %d %H %M %S
    newtime = time.strftime("%H:%M:%S",time.localtime());
    return newtime;
    pass

# [7]数据解析模块

# [6]分页模块
def Get_page_data(requests_data):
    # 创建soup对象
    soup = BeautifulSoup(requests_data,"html.parser");
    # 查询总页数:data-invalidpageerrmsg="Page index is invalid"
    # data-pageparameter="page"
    div_pages =soup.find("div",attrs={"data-invalidpageerrmsg":"Page index is invalid","data-pageparameter":"page"})["data-pagecount"]
    print("当前旅游信息的总页数:",div_pages)
    pass

# [5]网络访问模块
def Get_Data_Url(url):
    # 5.1网络访问
    requests_url = requests.get(url,header);
    print(url)
    # 5.2判断是否网络访问成功
    if requests_url.status_code == 200:
        html_data = requests_url.content.decode("utf-8");
        # 5.3查询记录存储到本地 - 创建一个本地存储的文件夹
        if not os.path.exists(file_data):
            os.makedirs(file_data);
            print("路径创建成功");
            pass
        # 5.4存储到本地：
        file_add = open("%s\悠哉网网络范文记录.txt"%file_data,"a",1);
        st_01 = str(GetNewTime())+":"+url;
        print(st_01)
        file_add.write(st_01);
        file_add.close();
        # 返回请求到的数据
        return html_data;
        pass
    else:
        print("网络访问失败")
        pass
    pass

# [4]创建程序的入口
if __name__ == '__main__':
    print(GetNewTime(),"欢迎使用=悠哉网=旅游信息爬取插件");
    # 4.1请用户输入
    adderss = input("请用户输入要查询的城市或国家:按回车键结束输入");
    # 4.2 倒计时
    time_list = [5,4,3,2,1];
    for time_item in time_list:
        print(GetNewTime(),"倒计时:%d秒"%time_item);
        # 睡眠1秒
        # time.sleep(1);
        pass
    # 开始查询 - 网址的拼接
    new_url = yz_url%adderss;
    # 请求网络数据
    requests_data =  Get_Data_Url(new_url);
    # 查询分页详情
    Get_page_data(requests_data);
    pass





