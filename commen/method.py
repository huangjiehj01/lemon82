import time #等待的库
#打开浏览器
def open_page(driver,url):
    driver.get(url)#打开URL地址网页
    driver.maximize_window()#最大化

#登录
def login_fun(driver,name,passwd):
    driver.find_element_by_id("username").send_keys(name)
    # 1.代码找到元素 找到id是username的元素--输入框 2.进行输入用户名内容的操作
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()  # 用xpath轴定位勾选记住账号
    driver.find_element_by_id("btnSubmit").click()  # 通过id找到按钮，进行点击操作登录

#搜索函数
def search_fun(driver,url,name,passwd,key):
    open_page(driver,url)
    login_fun(driver,name,passwd)#打开页面需要先登录 所以需要调用上面两个函数
    driver.find_element_by_xpath("//div[@id='leftMenu']//span[text()='零售出库']").click()
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")#获取id属性
    id_iframe=id+"-frame"#通过字符串的拼接 得到iframe id
    #通过id进行iframe切换
    #driver.switch_to.frame(id_iframe)#通过id（name）来进行iframe切换id
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    #通过webelement来进行iframe切换
    driver.find_element_by_id("searchNumber").send_keys(key) #在单据编号输入448
    driver.find_element_by_id("searchBtn").click()#点击查询按钮
    time.sleep(1)#隐式等待+强制等待
    num=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div')#获取编号的文本
    return num.text#定义返回值搜索出来的数据


