from commen import method #从python包里导入 要把方法 文件导进来
from testdata import data
from selenium import webdriver#从selenium工具包中导入webdriver库
driver = webdriver.Chrome()#webdriver与chrome浏览器建立会话 赋值变量 注：Chrome开头要大写 会自动启动浏览器
driver.implicitly_wait(10)#隐式等待10s

#取数据 字典取值
url = data.data_t.get("url")
name = data.data_t["name"]
passwd = data.data_t["passwd"]
key = data.data_t["key"]

result = method.search_fun(driver=driver,url=url,name=name,passwd=passwd,key=key) #直接调用搜索函数 取值 接收返回值
if key in result:
    print("搜索成功！")